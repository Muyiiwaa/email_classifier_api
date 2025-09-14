# FastAPI Project Setup with `uv`

This guide walks you through setting up a new FastAPI project using `uv`, a fast Python package installer and resolver.

### **Step 1: Initialize Your Project**

First, create a new project directory and initialize it with `uv`. Replace `your_project_name` with the desired name for your project.

```sh
uv init your_project_name
cd your_project_name
```

### **Step 2: Activate the Virtual Environment**

`uv` automatically creates a virtual environment (`.venv`) in your project directory. Activate it to start installing dependencies.

-   **On Linux, macOS, or GitHub Codespaces:**
    ```sh
    source .venv/bin/activate
    ```

-   **On Windows (using PowerShell):**
    ```sh
    .venv\Scripts\activate
    ```

### **Step 3: Add Dependencies**

With the virtual environment active, you can add your required Python libraries. Let's add `fastapi` and `uvicorn` (the ASGI server to run the app).

```sh
uv add fastapi uvicorn
```

You can add any other libraries you need by listing them in the same command.

### **Step 4: Sync Your Dependencies**

After adding dependencies, it's a good practice to ensure your environment is perfectly in sync with your `pyproject.toml` file.

```sh
uv sync
```

### **Step 5: Write Your Application Code**

Create a `main.py` file and write your FastAPI application code. Here is a simple "Hello World" example to get you started:

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

### **Step 6: Run the Development Server**

Finally, run your application using `uvicorn`. The server will be accessible at `http://127.0.0.1:8000`.

```sh
uvicorn main:app --reload
```

-   `main`: Refers to the `main.py` file.
-   `app`: Refers to the `app` object created inside `main.py`.
-   `--reload`: Makes the server restart automatically whenever you make changes to the code.

