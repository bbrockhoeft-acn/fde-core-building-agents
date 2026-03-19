# UdaPlay — AI Game Research Agent

## Project Overview
UdaPlay is an AI-powered research agent for the video game industry. This project is divided into two parts that build a sophisticated AI agent capable of answering questions about video games using both local knowledge and web search.

## Part 1 · Offline RAG (Retrieval-Augmented Generation)
Build a vector database using ChromaDB to store and retrieve video game information efficiently.

Key tasks:
- Set up ChromaDB as a persistent client
- Create a collection with appropriate embedding functions
- Process and index game data from JSON files
- Each game document contains:
  - Name
  - Platform
  - Genre
  - Publisher
  - Description
  - Year of Release

## Part 2 · AI Agent Development
Build an intelligent agent that combines local knowledge with web search capabilities.

The agent will:
1. Answer questions using internal knowledge (RAG)
2. Search the web when needed
3. Maintain conversation state
4. Return structured outputs
5. Store useful information for future use

Required tools to implement:
1. `retrieve_game` — Search the vector database for game information
2. `evaluate_retrieval` — Assess the quality of retrieved results
3. `game_web_search` — Perform web searches for additional information

## Getting Started

1. Follow the local environment setup in the [workspace README](../../README.md)
2. Create your `.env` file in this folder (see API Configuration below)
3. Run the notebooks in order:
   - `Udaplay_01_starter_project.ipynb` — Build the vector database
   - `Udaplay_02_starter_project.ipynb` — Implement the AI agent

## API Configuration
Create a `.env` file in `project/starter/` with:
```
OPENAI_API_KEY="your-vocareum-key"
OPENAI_API_BASE="https://openai.vocareum.com/v1"
CHROMA_OPENAI_API_KEY="your-vocareum-key"
TAVILY_API_KEY="your-tavily-key"
```
- Vocareum workspace must be activated for API access
- Sign up for a free Tavily account at https://app.tavily.com/

## Project Structure
```
project/starter/
├── Udaplay_01_starter_project.ipynb    # Part 1: RAG implementation (student working copy)
├── Udaplay_01_solution_project.ipynb   # Part 1: Clean RAG solution (for submission)
├── Udaplay_02_starter_project.ipynb    # Part 2: Agent implementation (student working copy)
├── Udaplay_02_solution_project.ipynb   # Part 2: Clean agent solution (for submission)
├── games/                              # Game data JSON files (25 titles)
├── lib/                                # Shared library code
│   ├── agents.py                       # Agent state machine
│   ├── llm.py                          # LLM abstractions
│   ├── messages.py                     # Message handling
│   └── tooling.py                      # Tool decorator
├── .env                                # API configuration (gitignored)
└── chromadb/                           # Persistent vector database (gitignored)
```

## Testing Your Implementation
After completing both parts, test your agent with questions like:
- "Which games are set in a fantasy world and involve dragons?"
- "Which gaming platform has a nostalgic collection of classic console games?"
- "Which games are still actively developed and have periodic releases?"
- "Recommend games that are immersive and have strong storytelling elements."

## Advanced Features (Optional)
After completing the basic implementation, consider extending the agent with:
- Long-term memory (persisting new facts discovered via web search)
- A state machine with tools as explicit graph nodes
- Structured JSON output for downstream consumption

## Built With
- [ChromaDB](https://www.trychroma.com/) — Persistent vector database for local RAG
- [OpenAI](https://platform.openai.com/) — Embeddings and LLM (via Vocareum proxy)
- [Tavily](https://app.tavily.com/) — Web search API
- [python-dotenv](https://github.com/theskumar/python-dotenv) — Environment variable management
- [Pydantic](https://docs.pydantic.dev/) — Data validation for tool outputs

## Notes
- Use **solution notebooks** for grading/clean submission; use **starter notebooks** for development
- Notebooks are configured with `nbstripout` to strip outputs/metadata on commit
- Vector database files are gitignored — regenerate by running Part 1
- Never hardcode API keys directly in notebook cells before uploading for submission

## License
[License](../../LICENSE.md)
