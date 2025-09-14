# Email Classifier API

Please refer to the main [README.md](../README.md) in the root directory for complete setup and usage instructions.

## Quick Start for Development

If you're already in this directory:

```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows

# Run the application
uvicorn main:app --reload
```

The application will be available at http://localhost:8000 with interactive docs at http://localhost:8000/docs.
