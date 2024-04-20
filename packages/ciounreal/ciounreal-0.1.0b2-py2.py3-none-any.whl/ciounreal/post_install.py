import os
import sys
import errno
import shutil
import zipfile
import re

def fslash(path):
    return path.replace("\\", "/")


PACKAGE_DIR = fslash(os.path.dirname(os.path.abspath(__file__)))
CIO_DIR = os.path.dirname(PACKAGE_DIR)
HOME = fslash(os.path.expanduser("~"))

DEFAULT_BASE_PATH = r"C:\Program Files\Epic Games"



PLUGIN_NAME = "Conductor"

INIT_SCRIPT_CONTENT = f"""
import sys

CIO_DIR = "{CIO_DIR}"

if CIO_DIR not in sys.path:
    sys.path.append(CIO_DIR)

from ciounreal import ConductorExecutor

print("APPENDED CIO_DIR to sys.path: ", CIO_DIR)
print("Imported ConductorExecutor.py")
"""


def main(project_path=None):
    print(f"CIO_DIR: {CIO_DIR}")
    ue_plugin_directories = []
    if project_path:
        if os.path.exists(project_path):
            ue_plugin_directories = [os.path.join(project_path, "Plugins")]
        else:
            print(f"The provided project path does not exist: {project_path}")
            print("Plugin will not be installed.")
    else:
        ue_plugin_directories = find_unreal_engine_plugins()

    for plugin_directory in ue_plugin_directories:
        print(f"Installing the {PLUGIN_NAME} plugin to {plugin_directory}")
        install_into_unreal(plugin_directory)

    print("Completed Unreal tool setup!")


def find_unreal_engine_plugins():
    """
    Scans for Unreal Engine installations and retrieves the paths to their plugin directories.

    This function looks for Unreal Engine installations by examining the base path specified by the 'UE_ROOT' environment variable, or a default base path if 'UE_ROOT' is not set. It searches for directories that match the pattern of Unreal Engine versions, specifically those starting with 'UE_5'.

    If no installations are found under the base path, it prints a message indicating this and returns an empty list. Otherwise, it attempts to locate the 'Plugins' directory within each detected Unreal Engine installation.

    If the 'Plugins' directory does not exist, the function will try to create it using `ensure_directory` function. Any errors encountered during this process are printed, and the function continues to the next installation.

    After processing all installations, the function prints the number of plugin directories found and their full paths.

    Returns:
        list: A list of strings, where each string is the full path to a plugin directory of an Unreal Engine installation.
    """

    base_path = os.environ.get("UE_ROOT", DEFAULT_BASE_PATH)
    rx = ".*UE_5(\.\d)+$"
    
    engine_paths = []
    if re.match(rx, os.path.basename(base_path)):
        engine_paths.append(base_path)
    else:
        engine_paths = [
            os.path.join(base_path, d) for d in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, d)) and d.startswith("UE_5")
        ]

    if not engine_paths:
        print("No Unreal Engine installations found.")
        return []
 
    plugin_paths = []
    for engine_path in engine_paths:
        plugins_path = os.path.join(engine_path, "Engine", "Plugins")
        if not os.path.exists(plugins_path):
            try:
                ensure_directory(plugins_path)
                plugin_paths.append(plugins_path)
            except Exception as ex:
                print(f"Failed to find or create plugins directory: {plugins_path}. Reason: {ex}")
                continue
        else:
            plugin_paths.append(plugins_path)

    print(f"Found {len(plugin_paths)} Unreal Engine plugin directories")
    # Print the full paths
    for path in plugin_paths:
        print(path)
    return plugin_paths


def install_into_unreal(plugins_directory):
    ensure_directory(plugins_directory)
    # Delete existing installation if it exists.
    plugin_directory = os.path.join(plugins_directory, PLUGIN_NAME)
    # Create or empty a folder for the plugin.
    try:
        if os.path.isdir(plugin_directory):
            shutil.rmtree(plugin_directory)
    except Exception as e:
        print(f"Failed to remove existing {plugin_directory}. Reason: {e}")
        return

    zipped = os.path.join(CIO_DIR, "Plugins", "Conductor.zip")
    target = os.path.join(plugins_directory, "Conductor")
    ensure_directory(target)
    with zipfile.ZipFile(zipped, "r") as zip_ref:
        zip_ref.extractall(target)

    with open(os.path.join(target, "Content", "Scripts", "init_unreal.py"), "w") as f:
        f.write(INIT_SCRIPT_CONTENT)


def ensure_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as ex:
        if ex.errno == errno.EEXIST and os.path.isdir(directory):
            pass
        else:
            raise


if __name__ == "__main__":
    # give a path to a project to install into. If not provided, it will install into the default Unreal Engine plugins directory.
    
    project_path = sys.argv[1] if len(sys.argv) > 1 else None
    main(project_path=project_path)
