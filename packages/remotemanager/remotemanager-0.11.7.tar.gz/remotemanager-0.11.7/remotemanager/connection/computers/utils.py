from typing import Union


def format_time(time: Union[int, str]) -> Union[str, None]:
    """
    Take integer seconds and generate a HH:MM:SS timestring

    Args:
        time (int):
            seconds
    Returns:
        (str):
            HH:MM:SS format timestamp
    """
    if time is None:
        return None
    if not isinstance(time, int):
        # if given a string, assume format is already valid and return
        try:
            time = int(time)
        except ValueError:
            return time
    mins = time // 60
    hours = mins // 60

    secstring = str(time % 60).rjust(2, "0")
    minstring = str(mins % 60).rjust(2, "0")
    hourstring = str(hours).rjust(2, "0")

    return f"{hourstring}:{minstring}:{secstring}"


def time_to_s(time: str) -> int:
    """Convert back from HH:MM:SS to integer seconds"""
    hh, mm, ss = time.split(":")

    return int(hh) * 3600 + int(mm) * 60 + int(ss)
