from collections.abc import Callable


def output_answer[**P, R](problem: str) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            result: R = func(*args, **kwargs)
            print(f"{problem} answer: {result}")
            return result

        return wrapper

    return decorator
