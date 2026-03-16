import os
import sys
import subprocess
import venv
from pathlib import Path

def main():
    skill_dir = Path(__file__).parent.parent
    venv_dir = skill_dir / ".venv"
    req_file = skill_dir / "requirements.txt"

    # Create venv
    print(f"🔧 Creating virtual environment in {venv_dir}...")
    venv.create(venv_dir, with_pip=True)

    # Get venv pip
    if os.name == 'nt':
        pip_exe = venv_dir / "Scripts" / "pip.exe"
    else:
        pip_exe = venv_dir / "bin" / "pip"

    # Install requirements
    if req_file.exists():
        print(f"📦 Installing requirements from {req_file}...")
        subprocess.run([str(pip_exe), "install", "-r", str(req_file)], check=True)

    print("✅ Environment setup complete!")

if __name__ == "__main__":
    main()
