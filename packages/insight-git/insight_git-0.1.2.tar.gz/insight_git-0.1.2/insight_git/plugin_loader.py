from importlib import metadata


def load_plugins():
    """
    Loads plugins using entry points.

    This function discovers and loads plugins registered under the
    "insight_git.plugins" entry point, associating each plugin with its
    corresponding function.

    Returns:
        A dictionary where keys are plugin names and values are the loaded plugin functions.
    """
    plugins = {}
    # Discover and load the plugins registered under the "insight_git.plugins" entry point
    for entry_point in metadata.entry_points(group="insight_git.plugins"):
        try:
            # Load the plugin and associate it with its corresponding function
            plugins[entry_point.name] = entry_point.load()
        except Exception as e:
            print(f"Warning: could not load the plugin {entry_point.name}: {e}")
    return plugins
