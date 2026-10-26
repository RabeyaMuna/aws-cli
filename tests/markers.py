import platform

import pytest


def skip_if_windows(reason):
    """Decorator to skip tests that should not be run on windows.

    Example usage:

        @skip_if_windows("Not valid")
        def test_some_non_windows_stuff(self):
            self.assertEqual(...)

    """
    return pytest.mark.skipif(
        platform.system() not in ['Darwin', 'Linux'],
        reason=reason,
    )


def if_windows(reason):
    """Decorator to skip tests should only be ran for windows.

    Example usage:

        @if_windows("Only supported on windows")
        def test_some_windows_stuff(self):
            self.assertEqual(...)

    """
    return pytest.mark.skipif(
        platform.system() in ['Darwin', 'Linux'],
        reason=reason,
    )
