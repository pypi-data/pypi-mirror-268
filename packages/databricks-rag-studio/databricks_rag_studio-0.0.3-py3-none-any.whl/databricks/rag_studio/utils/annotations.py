import re
import warnings
from functools import wraps


def _get_min_indent_of_docstring(docstring_str: str) -> str:
    """
    Get the minimum indentation string of a docstring, based on the assumption
    that the closing triple quote for multiline comments must be on a new line.
    Note that based on ruff rule D209, the closing triple quote for multiline
    comments must be on a new line.

    Args:
        docstring_str: string with docstring

    Returns:
        Whitespace corresponding to the indent of a docstring.
    """

    if not docstring_str or "\n" not in docstring_str:
        return ""

    return re.match(r"^\s*", docstring_str.rsplit("\n", 1)[-1]).group()


def deprecated(alternative=None, since=None, impact=None):
    """Annotation decorator for marking APIs as deprecated in docstrings and raising a warning if
    called.

    Args:
        alternative: (Optional string) The name of a superseded replacement function, method,
            or class to use in place of the deprecated one.
        since: (Optional string) A version designator defining during which release the function,
            method, or class was marked as deprecated.
        impact: (Optional boolean) Indication of whether the method, function, or class will be
            removed in a future release.

    Returns:
        Decorated function.
    """

    def deprecated_decorator(func):
        since_str = f" since {since}" if since else ""
        impact_str = (
            impact if impact else "This method will be removed in a future release."
        )

        notice = (
            "``{qual_function_name}`` is deprecated{since_string}. {impact}".format(
                qual_function_name=".".join([func.__module__, func.__qualname__]),
                since_string=since_str,
                impact=impact_str,
            )
        )
        if alternative is not None and alternative.strip():
            notice += f" Use ``{alternative}`` instead."

        @wraps(func)
        def deprecated_func(*args, **kwargs):
            warnings.warn(notice, category=FutureWarning, stacklevel=2)
            return func(*args, **kwargs)

        if func.__doc__ is not None:
            indent = _get_min_indent_of_docstring(deprecated_func.__doc__)
            deprecated_func.__doc__ = (
                indent + ".. Warning:: " + notice + "\n" + func.__doc__
            )

        return deprecated_func

    return deprecated_decorator
