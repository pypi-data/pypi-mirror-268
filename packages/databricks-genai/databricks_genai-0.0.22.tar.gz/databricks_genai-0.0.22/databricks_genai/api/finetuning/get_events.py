"""List events for a finetuning run"""

from time import sleep
from typing import Union

from IPython import get_ipython
from IPython.display import HTML, clear_output, display
from mcli.config import MCLIConfig

from databricks_genai.api.config import configure_request
from databricks_genai.api.engine import get_return_response, run_plural_mapi_request
from databricks_genai.types.common import ObjectList
from databricks_genai.types.finetuning import FinetuningEvent, FinetuningRun

QUERY_FUNCTION = 'getFinetuneEvents'
VARIABLE_DATA_NAME = 'getFinetuneEventsData'
# This returns the same data that the create_run function returns
# for consistency when rendering the describe output

QUERY = f"""
query GetFinetuneEvents(${VARIABLE_DATA_NAME}: GetFinetuneEventsInput!) {{
  {QUERY_FUNCTION}({VARIABLE_DATA_NAME}: ${VARIABLE_DATA_NAME}) {{
    eventType
    eventTime
    eventMessage
  }}
}}"""


def is_running_in_notebook() -> bool:
    """
    Tested that this holds true for Databricks, Colab, and Jupyter notebooks
    Tested this is false when ran from python or from an ipython shell.

    Returns:
        bool: True if running in a notebook, False otherwise.
    """
    try:
        if 'IPKernelApp' not in get_ipython().config:  # Check if not in IPython shell
            return False
    except Exception:  # pylint: disable=W0718
        return False
    return True


@configure_request
def get_events(finetuning_run: Union[str, FinetuningRun], follow: bool = False) -> ObjectList[FinetuningEvent]:
    """List finetuning runs

    Args:
        finetuning_run (Union[str, FinetuningRun]): The finetuning run to get events for.

    Returns:
        List[FinetuningEvent]: A list of finetuning events. Each event has an event
            type, time, and message.
    """
    finetuning_run_name = finetuning_run.name if isinstance(finetuning_run, FinetuningRun) else finetuning_run

    variables = {
        VARIABLE_DATA_NAME: {
            'name': finetuning_run_name,
        },
    }

    cfg = MCLIConfig.load_config()
    cfg.update_entity(variables[VARIABLE_DATA_NAME])

    if follow:
        ft_events = []

        while not ft_events or not ft_events[-1].is_terminal_state():
            new_events = get_events(finetuning_run)
            if len(new_events) > len(ft_events):
                if is_running_in_notebook():
                    clear_output()
                    display(HTML(new_events._repr_html_()))  # pylint: disable=protected-access
                else:
                    for event in new_events[len(ft_events):]:
                        print(event)

            ft_events = new_events

            # don't unnecessarily sleep if run has completed
            if not ft_events[-1].is_terminal_state():
                sleep(5)

        # final cleanup before displaying in notebook
        if is_running_in_notebook():
            clear_output()

    else:
        response = run_plural_mapi_request(
            query=QUERY,
            query_function=QUERY_FUNCTION,
            return_model_type=FinetuningEvent,
            variables=variables,
        )
        ft_events = get_return_response(response)

    return ft_events
