#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def get_venv_python():
    skill_dir = Path(__file__).parent.parent
    venv_dir = skill_dir / ".venv"
    if os.name == 'nt':
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"

def ensure_venv():
    skill_dir = Path(__file__).parent.parent
    venv_dir = skill_dir / ".venv"
    setup_script = skill_dir / "scripts" / "setup_environment.py"
    if not venv_dir.exists():
        subprocess.run([sys.executable, str(setup_script)], check=True)
    return get_venv_python()

def main():
    if len(sys.argv) < 2:
        print("Usage: python run.py <script_name> [args...]")
        sys.exit(1)

    script_name = sys.argv[1]
    if not script_name.endswith('.py'):
        script_name += '.py'
    
    skill_dir = Path(__file__).parent.parent
    script_path = skill_dir / "scripts" / script_name
    
    if not script_path.exists():
        print(f"❌ Script not found: {script_name}")
        sys.exit(1)

    python_exe = ensure_venv()
    subprocess.run([str(python_exe), str(script_path)] + sys.argv[2:])

if __name__ == "__main__":
    main()
