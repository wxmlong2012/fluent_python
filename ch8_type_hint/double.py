from typing import Any, Optional


def double(x: Any) -> Any:
    return x * 2


def double_object(x: object) -> object:
    return x * 2


def double_float(x: Optional[float] = None) -> float:
    if isinstance(x, float):
        return x * 2
    else:
        return 1.0


