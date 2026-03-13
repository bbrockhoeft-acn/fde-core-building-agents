# Project Summary
The source in this project corresponds to Full Stack FDE - Core training course focused on *Building Agents*. All module exercises are copyrighted by Udacity subject to its license. Trainee project is for learning verification purposes.

# Setup
## Local Windows workstation setup steps:
- Install VS Code
- Install PowerShell 7 using `winget` and configure as default terminal in VS Code
- Install git for Windows
- Install the latest stable Python runtime (v3.14.3) using `winget`
- Install VS Code extensions from Microsoft: Python (ms-python.python), Jupyter ms-toolsai.jupyter

## Workspace environment setup:
The following changes & steps were made for local development of the module exercises and project:
- Allowed VS Code to create a virtual environment in the `/.venv` workspace folder
- Activated the virtual environment via PowerShell 7 terminal: `.\.venv\Scripts\Activate.ps1`
- Allowed VS Code to install Jupyter kernel package & register in venv:
    - `pip install ipykernel`
    - `python -m ipykernel install --user --name fde-agents --display-name "Python (fde-agents)"`
    - Selected virtual Python runtime for Juptyer kernel selector drop-down
- Installed 3rd party packages in venv:
    - `pip install python-dotenv`
    - `pip install pydantic`
    - `pip install openai`

