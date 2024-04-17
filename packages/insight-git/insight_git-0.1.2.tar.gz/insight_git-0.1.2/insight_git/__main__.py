from . import app


def main():
    """Start the Dash server with debug mode enabled and suppress callback exceptions.

    This function initializes the Dash web server. It's configured to run in debug
    mode for development purposes, allowing live updates on code changes. Additionally,
    it suppresses callback exceptions to prevent the app from crashing due to unhandled
    callback errors, improving the debugging experience.
    """
    app.run_server(debug=True)
    app.config.suppress_callback_exceptions = True


if __name__ == "__main__":
    main()
