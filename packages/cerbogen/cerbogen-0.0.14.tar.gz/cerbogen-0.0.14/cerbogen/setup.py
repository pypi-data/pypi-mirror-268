import sys
import os
import platform

def get_python_location():
    # Get the location of the Python interpreter
    return os.path.dirname(sys.executable)

def find_cerbogen_package():
    python_location = get_python_location()
    site_packages = os.path.join(python_location, 'lib', 'site-packages')
    cerbogen_path = os.path.join(site_packages, 'cerbogen')
    if os.path.exists(cerbogen_path):
        return cerbogen_path
    else:
        return None

def create_desktop_shortcut(ui_py_path):
    desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
    shortcut_path = os.path.join(desktop_dir, "cerbogen_ui.lnk" if platform.system() == "Windows" else "cerbogen_ui.desktop")
    python_exe = sys.executable
    if platform.system() == "Windows":
        # Create Windows shortcut
        from win32com.client import Dispatch
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = python_exe
        shortcut.Arguments = ui_py_path
        shortcut.WorkingDirectory = os.path.dirname(ui_py_path)
        shortcut.IconLocation = "/data/img/logo.ico"
        shortcut.save()
    else:
        # Create shortcut for Linux and macOS
        with open(shortcut_path, 'w') as shortcut_file:
            shortcut_file.write("[Desktop Entry]\n")
            shortcut_file.write("Name=Cerbogen UI\n")
            shortcut_file.write("Exec={} {}\n".format(python_exe, ui_py_path))
            shortcut_file.write("Type=Application\n")
            shortcut_file.write("Terminal=false\n")
        os.chmod(shortcut_path, 0o755)  # Add execute permission for Linux/macOS

if __name__ == "__main__":
    cerbogen_path = find_cerbogen_package()
    if cerbogen_path:
        ui_py_path = os.path.join(cerbogen_path, 'ui.py')
        if os.path.exists(ui_py_path):
            create_desktop_shortcut(ui_py_path)
            print("Desktop shortcut for Cerbogen UI created successfully!")
        else:
            print("ui.py not found in Cerbogen package.")
    else:
        print("Cerbogen package not found.")
