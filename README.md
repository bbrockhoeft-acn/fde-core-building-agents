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
- Installed core packages in venv:
    - `pip install python-dotenv`
    - `pip install pydantic`
    - `pip install openai`
- Installed project-specific packages:
    - `pip install chromadb` (for vector database and RAG)
    - `pip install tavily-python` (for web search API)
- Installed development tools:
    - `pip install nbstripout` (for cleaning Jupyter notebook metadata)
    - `nbstripout --install` (configure git filters for clean notebook commits)

## API Configuration
- Create `.env` file in `project/starter/` with API keys:
  ```
  OPENAI_API_KEY="your-vocareum-key"
  OPENAI_API_BASE="https://openai.vocareum.com/v1"
  CHROMA_OPENAI_API_KEY="your-vocareum-key"
  TAVILY_API_KEY="your-tavily-key"
  ```
- Vocareum workspace must be activated for API access
- Sign up for free Tavily account at https://app.tavily.com/

## Project Structure
```
/project/starter/
├── Udaplay_01_starter_project.ipynb    # Working RAG implementation
├── Udaplay_01_solution_project.ipynb   # Clean RAG solution
├── Udaplay_02_starter_project.ipynb    # Working agent implementation
├── Udaplay_02_solution_project.ipynb   # Clean agent solution
├── games/                              # Game data JSON files
├── .env                                # API configuration (gitignored)
└── chromadb/                           # Vector database (gitignored)

/project/lib/                           # Shared library code
```

## Development Notes
- Notebooks are configured with nbstripout to strip metadata/outputs on commit
- Vector database files are gitignored (regenerate from source data)
- Use solution notebooks for grading/clean demos, starter notebooks for development

