"""Utils for finetuning API"""
import json
import os
import re
import uuid
from typing import List, Optional

from databricks.sdk import WorkspaceClient
from databricks.sdk import errors as dbx_errors
from datasets import get_dataset_split_names
from mcli.api.exceptions import ValidationError
from mlflow import MlflowClient
from packaging import version

from databricks_genai.types.finetuning.finetune_config import FinetuneTaskType

_UC_VOLUME_LIST_API_ENDPOINT = '/api/2.0/fs/list'
_UC_VOLUME_FILES_API_ENDPOINT = '/api/2.0/fs/files'
_UC_PERIMISSIONS_API_ENDPOINT = '/api/2.1/unity-catalog/effective-permissions'
MIN_DBR_VERSION = version.parse('12.2')
DB_CONNECT_DBR_VERSION = version.parse('14.1')
SAVE_FOLDER_PATH = 'dbfs:/databricks/mlflow-tracking/{mlflow_experiment_id}/{mlflow_run_id}/artifacts'


def validate_register_to(path: str) -> None:
    """
    Validates that the register_to input is one of three inputs
    1. catalog.schema
    2. catalog.schema.existing_model_name
    3. catalog.schema.new_model_name

    For 1 and 3, we must check that a user can create a model in the schema.
    For 2, we must see that the user can update the existing model.
    """
    split_path = path.split('.')
    model_name = None
    if len(split_path) == 2:
        catalog, schema_name = split_path
    elif len(split_path) == 3:
        catalog, schema_name, model_name = split_path
    else:
        raise ValidationError(f'register_to must be in the format '
                              f'catalog.schema or catalog.schema.model_name, but got {path}')
    for component in split_path:
        if len(component) == 0:
            raise ValidationError(f'register_to must be in the format '
                                  f'catalog.schema or catalog.schema.model_name, but got {path}')
    client = WorkspaceClient()
    if model_name is not None:
        try:
            model_info = client.registered_models.get(path)
        except dbx_errors.NotFound:
            # we will create the model in the next step
            pass
        except dbx_errors.PermissionDenied as e:
            raise ValidationError(f'User does not have permission to access model "{path}" for register_to.') from e
        except dbx_errors.DatabricksError:
            # we except this just in case the ResourceDoesNotExist error changes
            # assume this means that the user needs to create the model
            pass
        else:
            # User can access model, make sure that they would theoretically be able to make a new version.
            # Note: to create the new version, we would have to use the MLflow API and submit both a run_id
            # and model artifacts. This is too involved, so we will instead just check ownership and permissions.
            # See PR #45 for more details. TODO: replace with a dry run call once this is implemented
            if model_info.owner != client.current_user.me().user_name:
                raise ValidationError(f'User must be the owner of the model {path} to register to it.')
            validate_uc_permissions(catalog,
                                    'catalog', ['ALL_PRIVILEGES', 'USE_CATALOG'],
                                    input_name="register_to",
                                    client=client)
            validate_uc_permissions(f'{catalog}.{schema_name}',
                                    'schema', ['ALL_PRIVILEGES', 'USE_SCHEMA'],
                                    input_name="register_to",
                                    client=client)
            return
    else:
        model_name = f'databricks-finetuning-credentials-test-{uuid.uuid4()}'
    try:
        # TODO: replace with a dry run call once this is implemented
        model_attempt = client.registered_models.create(catalog_name=catalog, schema_name=schema_name, name=model_name)
        # if create goes through, delete should be safe (delete perms are a subset of create, and the user is the owner
        # since they just created the model)
        client.registered_models.delete(model_attempt.full_name)
    except dbx_errors.NotFound as e:
        # thrown in the case that at least one of catalog or schema is invalid
        raise ValidationError(f'Could not find UC catalog "{catalog}" or schema "{schema_name}" for register_to '
                              'input.') from e
    except dbx_errors.PermissionDenied as e:
        raise ValidationError(f'User does not have permission to register a model at {path}.') from e
    except Exception as e:
        raise ValidationError(f'Failed to create model for register_to at {path}.') from e


def validate_uc_permissions(uc_path: str,
                            uc_type: str,
                            one_of_permissions: List[str],
                            input_name: str,
                            client: Optional[any] = None):
    # user must have at least ONE of the permissions in the given list
    # https://docs.databricks.com/api/workspace/grants/geteffective
    if not client:
        client = WorkspaceClient()
    try:
        resp = client.api_client.do(method='GET',
                                    path=f'{_UC_PERIMISSIONS_API_ENDPOINT}/{uc_type}/{uc_path}',
                                    query={'principal': client.current_user.me().user_name},
                                    headers={'Source': 'mosaicml/finetuning'})
    except dbx_errors.NotFound as e:
        raise ValidationError(f'Could not find {uc_type} {uc_path} for input {input_name}.') from e
    except dbx_errors.PermissionDenied as e:
        raise ValidationError(f'User does not have permission to access {uc_type} {uc_path} for '
                              f'input {input_name}.') from e
    except Exception as a:
        raise ValidationError(f'Failed to check permissions on {uc_type} {uc_path} for input {input_name}.') from a
    for assignment in resp['privilege_assignments']:
        for privilege in assignment['privileges']:
            privilege_type = privilege['privilege']
            if privilege_type in one_of_permissions:
                return
    raise ValidationError(
        f'User does not have one of the necessary permissions ({one_of_permissions}) on {uc_type} {uc_path} for '
        f'input {input_name}.')


def validate_delta_table(path: str, input_type: str) -> None:
    split_path = path.split('.')
    if len(split_path) != 3:
        raise ValidationError(f'Delta table input to {input_type} must be in the format '
                              f'catalog.schema.table, but got {path}.')
    for component in split_path:
        if len(component) == 0:
            raise ValidationError(f'Delta table input to {input_type} must be in the format '
                                  f'catalog.schema.table, but got {path}.')
    client = WorkspaceClient()
    try:
        client.tables.get(path)
    except dbx_errors.NotFound as e:
        raise ValidationError(f'Could not find table "{path}" for input "{input_type}"') from e
    except dbx_errors.PermissionDenied as e:
        raise ValidationError(f'User does not have permission to access table "{path}" for input "{input_type}"') from e
    except Exception as e:
        raise ValidationError(f'Failed to access table "{path}" for input "{input_type}".') from e


def validate_experiment_path(experiment_path: str) -> None:
    try:
        client = MlflowClient(tracking_uri='databricks')
        experiment = client.get_experiment_by_name(experiment_path)
        if not experiment:
            client.create_experiment(experiment_path)
    except Exception as e:
        raise ValidationError(f'Failed to get or create MLflow experiment {experiment_path}. Please make sure '
                              'your experiment path is valid.') from e


def find_a_txt_file(object_path: str) -> bool:
    # comes from Composer UCObjectStore
    client = WorkspaceClient()

    try:
        resp = client.api_client.do(method='GET',
                                    path=_UC_VOLUME_LIST_API_ENDPOINT,
                                    data=json.dumps({'path': object_path}),
                                    headers={'Source': 'mosaicml/finetuning'})
    except Exception as exc:
        raise ValidationError(
            f'Failed to access Unity Catalog path {object_path}. Ensure continued pretrain input is a Unity '
            'Catalog volume path to a folder.') from exc

    # repeat GET on original path to avoid duplicate code
    stack = [object_path]

    while len(stack) > 0:
        current_path = stack.pop()

        # Note: Databricks SDK handles HTTP errors and retries.
        # See https://github.com/databricks/databricks-sdk-py/blob/v0.18.0/databricks/sdk/core.py#L125 and
        # https://github.com/databricks/databricks-sdk-py/blob/v0.18.0/databricks/sdk/retries.py#L33 .
        resp = client.api_client.do(method='GET',
                                    path=_UC_VOLUME_LIST_API_ENDPOINT,
                                    data=json.dumps({'path': current_path}),
                                    headers={'Source': 'mosaicml/finetuning'})

        assert isinstance(resp, dict), 'Response is not a dictionary'

        for f in resp.get('files', []):
            fpath = f['path']
            if f['is_dir']:
                stack.append(fpath)
            else:
                if f['path'].endswith('.txt'):
                    return True
    return False


def validate_uc_path(uc_path: str, task_type: FinetuneTaskType) -> None:
    """
    Validates the user's read access to a Unity Catalog path. If `task_type!=CONTINUED_PRETRAIN`, ensures
    that the path ends with a jsonl file. Else, ensures that the path is a folder that contains a txt file.
    """
    if not uc_path.startswith('dbfs:/Volumes'):
        raise ValidationError('Databricks Unity Catalog Volumes paths should start with "dbfs:/Volumes".')
    path = os.path.normpath(uc_path[len('dbfs:/'):])
    dirs = path.split(os.sep)
    if len(dirs) < 4:
        raise ValidationError(f'Databricks Unity Catalog Volumes path expected to start with ' \
            f'`dbfs:/Volumes/<catalog-name>/<schema-name>/<volume-name>`. Found path={uc_path}')
    object_path = '/' + path
    if task_type == FinetuneTaskType.CONTINUED_PRETRAIN:
        if not find_a_txt_file(object_path):
            raise ValidationError(
                f'Could not find a .txt file in Unity Catalog path {uc_path}. Continued pretrain input must be a '
                'folder containing a .txt file.')
    else:
        if not object_path.endswith('.jsonl'):
            raise ValidationError(f'Unity Catalog input for instruction finetuning must be a jsonl file. Got {uc_path}')
        try:
            client = WorkspaceClient()
            client.api_client.do(method='HEAD', path=os.path.join(_UC_VOLUME_FILES_API_ENDPOINT, path))
        except Exception as e:
            raise ValidationError(f'Failed to access Unity Catalog path {uc_path}.') from e


def validate_hf_dataset(dataset_name_with_split: str) -> None:
    print(f'Assuming {dataset_name_with_split} is a Hugging Face dataset (not in format `dbfs:/Volumes` or '
          '`/Volumes`). Validating...')
    split_dataset_name = dataset_name_with_split.split('/')
    if len(split_dataset_name) < 2:
        raise ValidationError(
            f'Hugging Face dataset {dataset_name_with_split} must be in the format <dataset>/<split> or '
            '<entity>/<dataset>/<split>.')
    dataset_name, split = '/'.join(split_dataset_name[0:-1]), split_dataset_name[-1]
    try:
        splits = get_dataset_split_names(dataset_name)
    except Exception as e:
        raise ValidationError(
            f'Failed to access Hugging Face dataset {dataset_name_with_split}. Please make sure that the split '
            'is valid and that your dataset does not have subsets.') from e
    if split not in splits:
        raise ValidationError(f'Failed to access Hugging Face dataset {dataset_name_with_split}. Split not found.')
    print('Hugging Face dataset validation successful.')


def validate_data_prep(data_prep_cluster: Optional[str] = None):
    if data_prep_cluster is None:
        raise ValidationError(
            'Providing a delta table for train data or eval data requires specifying a data_prep_cluster.')
    user_has_access_to_cluster(data_prep_cluster)


def validate_custom_weights_path(custom_weights_path: str):
    mlflow_dbfs_path_prefix = 'dbfs:/databricks/mlflow-tracking/'
    # dbfs will be prepended before this if the user input `/databricks`
    mlflow_custom_weights_regex = (r'^dbfs:\/databricks\/mlflow-tracking'
                                   r'\/[0-9]+\/[0-9a-z]+\/artifacts($|\/[\/a-zA-Z0-9 ()_\\\-.]*$)')
    if not re.match(mlflow_custom_weights_regex, custom_weights_path):
        raise ValidationError('Custom weights path must be in the format [dbfs:]/databricks/mlflow-tracking/'
                              '<experiment_id>/<run_id>/artifacts/<path>. '
                              f'Found {custom_weights_path}')
    subpath = custom_weights_path[len(mlflow_dbfs_path_prefix):]
    _, run_id, _, artifact_path = subpath.split('/', maxsplit=3)
    artifact_dir = os.path.dirname(artifact_path)
    client = MlflowClient(tracking_uri='databricks')
    for artifact in client.list_artifacts(run_id, artifact_dir):
        if artifact.path == artifact_path:
            return
    raise ValidationError(f'Could not find file for custom_weights_path {custom_weights_path}')


def user_has_access_to_cluster(cluster_id: str):
    if cluster_id == 'serverless':
        return  # TODO can PrPr users access this?
    w = WorkspaceClient()
    try:
        w.clusters.get(cluster_id=cluster_id)
    except Exception as e:
        raise ValidationError(
            f'You do not have access to the cluster you provided: {cluster_id}. Please try again with another cluster.'
        ) from e


def is_cluster_sql(cluster_id: str) -> bool:
    # Returns True if DBR version < 14.1 and requires SqlConnect
    # Returns False if DBR version >= 14.1 and can use DBConnect
    if cluster_id == 'serverless':
        return False
    w = WorkspaceClient()
    cluster = w.clusters.get(cluster_id=cluster_id)
    stripped_runtime = re.sub(r'[a-zA-Z]', '', cluster.spark_version.split('-scala')[0].replace('x-snapshot', ''))
    runtime_version = re.sub(r'[.-]*$', '', stripped_runtime)
    if version.parse(runtime_version) < MIN_DBR_VERSION:
        raise ValidationError(
            'The cluster you provided is not compatible: please use a cluster with a DBR version > {MIN_DBR_VERSION}')
    if version.parse(runtime_version) < DB_CONNECT_DBR_VERSION:
        return True
    return False


def validate_create_finetuning_run_inputs(train_data_path: str,
                                          register_to: Optional[str] = None,
                                          experiment_path: Optional[str] = None,
                                          eval_data_path: Optional[str] = None,
                                          data_prep_cluster: Optional[str] = None,
                                          custom_weights_path: Optional[str] = None,
                                          task_type: FinetuneTaskType = FinetuneTaskType.INSTRUCTION_FINETUNE) -> None:
    delta_table_used = False
    validate_path(train_data_path, task_type, 'train_data_path')
    if register_to:
        validate_register_to(register_to)
    if experiment_path:
        validate_experiment_path(experiment_path)
    if eval_data_path is None:
        pass
    else:
        validate_path(eval_data_path, task_type, 'eval_data_path')
    if delta_table_used:
        validate_data_prep(data_prep_cluster)
    if custom_weights_path:
        validate_custom_weights_path(custom_weights_path)


def format_path(path: str) -> str:
    """
    Prepends `dbfs:` in front of paths that start with `/Volumes` or `/databricks`.
    """
    if isinstance(path, str) and (path.startswith('/Volumes') or path.startswith('/databricks')):
        return f'dbfs:{path}'
    else:
        return path


def validate_path(data_path: str, task_type: FinetuneTaskType, data_path_type: str) -> None:
    """
    Validates the given data path in UC volume format, HF dataset format, or Delta table format.

    Args:
        data_path: The data path to validate.
        task_type: The finetuning task type.
        data_path_type: The type of data path, either 'train_data_path' or 'eval_data_path' for error messages.
    """
    if task_type == FinetuneTaskType.CONTINUED_PRETRAIN:
        validate_uc_path(data_path, task_type)
    else:  # 'INSTRUCTION_FINETUNE' or 'CHAT_COMPLETION' tasks
        if data_path.startswith('dbfs:/'):
            validate_uc_path(data_path, task_type)
        elif '/' in data_path:  # assume HF dataset TODO state this assumption in docs
            validate_hf_dataset(data_path)
        else:
            validate_delta_table(data_path, data_path_type)
