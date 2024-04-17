import pytest

from insight_git.callbacks import validate_input


# Test for validate_input function
def test_validate_input():
    """
    Test the validate_input function to ensure it returns appropriate error messages
    based on the input provided.
    """
    # Example inputs for the test
    test_cases = [
        (
            None,
            "",
            [],
            "Please enter a repository URL.",
            "Please select at least one plugin.",
        ),
        (1, "https://github.com/example/repo", ["plugin1"], "", ""),
    ]

    # Iterate through the test cases
    for (
        n_clicks,
        url,
        selected_plugins,
        expected_url_error,
        expected_plugin_error,
    ) in test_cases:
        # Call the function under test
        url_error, plugin_error = validate_input(n_clicks, url, selected_plugins)

        # Assert the expected outcomes
        assert (
            url_error == expected_url_error
        ), "URL validation error message did not match expected"
        assert (
            plugin_error == expected_plugin_error
        ), "Plugin selection validation error message did not match expected"
