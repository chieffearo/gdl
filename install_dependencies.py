import subprocess
import sys
import os

def install_requirements():
    requirements_file = "requirements.txt"

    if not os.path.exists(requirements_file):
        print(f"Error: The file '{requirements_file}' does not exist in the current directory.")
        return

    try:
        print("Installing required libraries...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("✅ All required libraries have been installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Installation failed with error code {e.returncode}.")
        print(f"Details: {e.output}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    install_requirements()
