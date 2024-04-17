from unittest.mock import patch

from insight_git import __main__


def test_main_calls_run_server_with_debug_true():
    """
    Test if main function starts Dash server with debug mode enabled.

    This test checks whether the 'run_server' method of the 'app' object
    is called with 'debug=True' when the 'main' function is executed.
    It uses patching to mock the 'run_server' method and assert it's called
    with expected arguments.
    """
    with patch.object(__main__.app, "run_server") as mock_run_server:
        # Call the 'main' function
        __main__.main()

        # Assert 'run_server' was called once with 'debug=True'
        mock_run_server.assert_called_once_with(debug=True)
