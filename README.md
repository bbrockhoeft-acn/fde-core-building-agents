# Project Summary
The source in this project corresponds to Full Stack FDE - Core training course focused on *Building Agents*. All module exercises are copyrighted by Udacity subject to its license. Trainee project is for learning verification purposes.

## UdaPlay — Project Overview
UdaPlay is an AI-powered research agent for the video game industry, built as the capstone project for Course 3 (Building Agents). The project is split into two parts:

### Part 1 · Offline RAG
Build a vector database using ChromaDB to store and retrieve video game information. Each game document contains Name, Platform, Genre, Publisher, Description, and Year of Release.

### Part 2 · AI Agent
Build an intelligent agent that combines local knowledge with web search. Capabilities:
1. Answer questions using internal knowledge (RAG)
2. Fall back to web search when needed
3. Maintain conversation state
4. Return structured outputs

**Agent Tools:**
- `retrieve_game` — Searches the local ChromaDB vector database
- `evaluate_retrieval` — Scores the usefulness of retrieved documents
- `game_web_search` — Web search fallback via Tavily

See [`project/starter/README.md`](project/starter/README.md) for full project specifications and rubric details.

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
    - `nbstripout --install` (configure git filters for clean notebook commits — optional, see Development Notes)

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
- **nbstripout** is configured via `.gitattributes` to strip outputs only from `*starter*.ipynb` files.
  Solution notebooks (`*solution*.ipynb`) intentionally preserve cell outputs so reviewers can verify successful runs.
- To enable output stripping during active development (reduces diff noise in starter notebooks):
  ```
  nbstripout --install
  git config filter.nbstripout.required false
  ```
- To disable stripping entirely: `nbstripout --uninstall`
- Vector database files are gitignored (regenerate from source data)
- Use solution notebooks for grading/submission; use starter notebooks for development

