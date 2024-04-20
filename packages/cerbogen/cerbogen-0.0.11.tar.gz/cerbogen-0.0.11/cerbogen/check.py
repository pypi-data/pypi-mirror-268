import importlib.util
import subprocess
import sys

required_modules = [

    "tkinter", "matplotlib", "pydub", "numpy", "wave", "librosa" , "cerbogen"
]

def check_module(module_name):
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        return False
    return True

def install_module(module_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

def main():
    missing_modules = []
    for module in required_modules:
        if not check_module(module):
            missing_modules.append(module)

    if missing_modules:
        print("The following modules are missing and will be installed:")
        print(", ".join(missing_modules))
        for module in missing_modules:
            try:
                install_module(module)
            except subprocess.CalledProcessError as e:
                print(f"Error installing {module}: {e}")
                sys.exit(1)
    else:
        print("All required modules are installed.")

if __name__ == "__main__":
    main()
