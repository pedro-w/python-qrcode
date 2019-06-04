try:
    import unittest2 as unittest
except ImportError:  # pragma: no cover
    import unittest
try:
    from unittest import mock
except ImportError:  # pragma: no cover
    import mock

from qrcode import run_example


class ExampleTest(unittest.TestCase):

    @mock.patch('PIL.Image.Image.show')
    def runTest(self, mock_show):
        run_example()
        mock_show.assert_called_with()
