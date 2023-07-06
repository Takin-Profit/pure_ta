from dataclasses import dataclass


@dataclass(frozen=True)
class ErrMsg:
    """an error message."""

    msg: str
