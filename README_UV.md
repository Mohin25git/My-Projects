# MiniChatBot with UV

This project uses [uv](https://github.com/astral-sh/uv) for extremely fast dependency management.

## Setup

1.  **Install uv** (if you haven't already):
    ```powershell
    pip install uv
    # OR via PowerShell script
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

2.  **Run the Chatbot**:
    You don't need to manually create a virtual environment. `uv` handles it for you.
    ```powershell
    uv run streamlit run MiniChatBot.py
    ```

3.  **Add new packages**:
    ```powershell
    uv add <package_name>
    ```

## Project Structure

- `MiniChatBot.py`: Main application
- `pyproject.toml`: Project configuration and dependencies
- `uv.lock`: Exact versions of installed dependencies (generated after first run)
