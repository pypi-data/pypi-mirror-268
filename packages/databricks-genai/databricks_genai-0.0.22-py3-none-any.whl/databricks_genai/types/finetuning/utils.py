"""
Utils for use in finetuning types.
"""

from typing import Union

PROGRESS = [
    "□□□□□□□□□□", "■□□□□□□□□□", "■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□", "■■■■■■□□□□", "■■■■■■■□□□",
    "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■"
]


def seconds_to_str(seconds: Union[int, float]) -> str:
    """Converts seconds to a human-readable string

    Args:
        seconds: Number of seconds

    Returns:
        Human-readable string
    """
    if seconds < 60:
        return f'{int(seconds)}s'
    elif seconds < 3600:
        return f'{int(seconds/60)}min'
    elif seconds < 24 * 3600:
        return f'{int(seconds/3600)}hr'
    else:
        return f'{int(seconds/3600/24)}d'
