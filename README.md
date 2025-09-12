# FastAPI Project Setup with uv


1. Initialize project
uv init project_name
cd project_name

2. Add first dependency
uv add first_library

3. Activate virtual environment
- Linux / macOS /github codespaces
 source .venv/bin/activate
- Windows PowerShell
.venv\Scripts\activate

4. Add other libraries including FastAPI and Uvicorn
uv add fastapi uvicorn any_other_library

5. Sync dependencies
uv sync

6. write your code in main.py

7. run the app
uvicorn main:app --reload

