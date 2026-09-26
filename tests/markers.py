import platform

import pytest


def skip_if_windows(reason=None):
    """Decorator to skip tests that should not be run on windows.

    Can be used as a bare decorator::

        @skip_if_windows
        def test_func():
            ...

    Or with a custom reason::

        @skip_if_windows("Custom reason")
        def test_func():
            ...
    """
    if callable(reason):
        # Used as @skip_if_windows (bare decorator)
        decorator = pytest.mark.skipif(
            platform.system() not in ['Darwin', 'Linux'],
            reason="This test does not run on windows.",
        )
        return decorator(reason)
    # Used as @skip_if_windows("reason") or @skip_if_windows()
    actual_reason = reason if reason else "This test does not run on windows."
    return pytest.mark.skipif(
        platform.system() not in ['Darwin', 'Linux'],
        reason=actual_reason,
    )


def if_windows(reason=None):
    """Decorator to skip tests that should only be run on windows.

    Can be used as a bare decorator::

        @if_windows
        def test_func():
            ...

    Or with a custom reason::

        @if_windows("Custom reason")
        def test_func():
            ...
    """
    if callable(reason):
        # Used as @if_windows (bare decorator)
        decorator = pytest.mark.skipif(
            platform.system() in ['Darwin', 'Linux'],
            reason="This test only runs on windows.",
        )
        return decorator(reason)
    # Used as @if_windows("reason") or @if_windows()
    actual_reason = reason if reason else "This test only runs on windows."
    return pytest.mark.skipif(
        platform.system() in ['Darwin', 'Linux'],
        reason=actual_reason,
    )
