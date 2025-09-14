# Email Classifier API

A FastAPI application for serving an ML email classifier with additional utility endpoints. This project demonstrates how to build, configure, and deploy a FastAPI application using the modern Python package manager `uv`.

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- uv package manager

## 📦 Installation & Setup

### 1. Install uv Package Manager

**Option A: Using the official installer (recommended)**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Option B: Using pip**
```bash
pip install uv
```

**Option C: Using Homebrew (macOS)**
```bash
brew install uv
```

### 2. Initialize a New Project (for new projects)

If you're starting from scratch, create a new project:

```bash
# Initialize a new project
uv init email-classifier-api
cd email-classifier-api
```

### 3. Clone and Setup This Repository

```bash
# Clone the repository
git clone https://github.com/Muyiiwaa/email_classifier_api.git
cd email_classifier_api/email_api
```

### 4. Install Dependencies

```bash
# Install all dependencies and create virtual environment
uv sync
```

This command will:
- Create a virtual environment (`.venv`)
- Install all dependencies specified in `pyproject.toml`
- Generate/update the lock file (`uv.lock`)

### 5. Activate Virtual Environment

**Linux / macOS / GitHub Codespaces:**
```bash
source .venv/bin/activate
```

**Windows PowerShell:**
```bash
.venv\Scripts\activate
```

**Windows Command Prompt:**
```bash
.venv\Scripts\activate.bat
```

### 6. Run the Application

```bash
# Development mode with auto-reload
uvicorn main:app --reload

# Production mode
uvicorn main:app --host 0.0.0.0 --port 8000

# Custom host and port with reload
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

The application will be available at:
- **Main application**: http://localhost:8000
- **Interactive API docs**: http://localhost:8000/docs
- **Alternative API docs**: http://localhost:8000/redoc

## 🏗️ Project Structure

```
email_classifier_api/
├── email_api/                 # Main application directory
│   ├── main.py               # FastAPI application entry point
│   ├── schema.py             # Pydantic models (currently empty)
│   ├── utils.py              # Utility functions (currently empty)
│   ├── pyproject.toml        # Project configuration and dependencies
│   ├── uv.lock              # Dependency lock file
│   ├── .python-version      # Python version specification
│   └── README.md            # This documentation
├── README.md                 # Root README
└── .gitignore               # Git ignore rules
```

## 🔧 Dependencies Management

### Adding New Dependencies

```bash
# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Add a specific version
uv add "package-name>=1.0.0,<2.0.0"

# Add from a specific index
uv add package-name --index-url https://pypi.org/simple/
```

### Removing Dependencies

```bash
# Remove a dependency
uv remove package-name
```

### Current Dependencies

- **FastAPI[all]** (>=0.116.1): Modern web framework for building APIs
- **PyTorch** (>=2.8.0): Machine learning framework
- **Transformers** (>=4.56.1): Hugging Face transformers library
- **Uvicorn**: ASGI server for running FastAPI applications

## 🌐 API Endpoints

### 1. Home Endpoint
- **URL**: `/`
- **Method**: GET
- **Description**: Health check endpoint
- **Response**: `{"message": "We are live!!"}`

**Example:**
```bash
curl http://localhost:8000/
```

### 2. Currency Converter
- **URL**: `/converter/`
- **Method**: POST
- **Description**: Converts Nigerian Naira to US Dollars
- **Parameters**:
  - `naira` (float): Amount in Naira
  - `rate` (float, optional): Exchange rate (default: 1520)

**Example:**
```bash
curl -X POST "http://localhost:8000/converter/?naira=1000&rate=1520"
```

**Response:**
```json
{"dollar": "$0.66"}
```

### 3. Tithe Calculator
- **URL**: `/tithe_calculator/`
- **Method**: POST
- **Description**: Calculates tithe amount (10% of salary)
- **Parameters**:
  - `salary` (float): Salary amount

**Example:**
```bash
curl -X POST "http://localhost:8000/tithe_calculator/?salary=50000"
```

**Response:**
```json
{"tithe_value": 5000.0}
```

## 📖 Interactive Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: Visit http://localhost:8000/docs
- **ReDoc**: Visit http://localhost:8000/redoc

These interfaces allow you to:
- Explore all available endpoints
- Test API calls directly from the browser
- View request/response schemas
- Download OpenAPI specification

## 🧪 Testing the API

### Using curl

```bash
# Test home endpoint
curl http://localhost:8000/

# Test currency converter
curl -X POST "http://localhost:8000/converter/?naira=5000&rate=1600"

# Test tithe calculator
curl -X POST "http://localhost:8000/tithe_calculator/?salary=100000"
```

### Using Python requests

```python
import requests

# Home endpoint
response = requests.get("http://localhost:8000/")
print(response.json())

# Currency converter
response = requests.post("http://localhost:8000/converter/?naira=5000&rate=1600")
print(response.json())

# Tithe calculator
response = requests.post("http://localhost:8000/tithe_calculator/?salary=100000")
print(response.json())
```

## 🔄 Development Workflow

### 1. Making Changes

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # Linux/macOS
   # or
   .venv\Scripts\activate     # Windows
   ```

2. Make your code changes in `main.py`, `schema.py`, or `utils.py`

3. The development server will automatically reload if you started it with `--reload` flag

### 2. Adding Dependencies

```bash
# Add new dependencies
uv add new-package

# Sync to install
uv sync
```

### 3. Environment Management

```bash
# Create a fresh environment
uv sync --reinstall

# Export requirements (compatible with pip)
uv export --format requirements-txt > requirements.txt

# Show installed packages
uv pip list
```

## 🐳 Docker Deployment (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy project files
COPY . .

# Install dependencies
RUN uv sync --no-dev

# Expose port
EXPOSE 8000

# Run the application
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t email-classifier-api .
docker run -p 8000:8000 email-classifier-api
```

## 🔧 Troubleshooting

### Common Issues

1. **Module not found error**
   ```bash
   # Ensure virtual environment is activated
   source .venv/bin/activate
   
   # Re-sync dependencies
   uv sync
   ```

2. **Port already in use**
   ```bash
   # Use a different port
   uvicorn main:app --reload --port 8001
   ```

3. **Permission denied (Windows)**
   ```bash
   # Enable script execution in PowerShell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. **UV command not found**
   ```bash
   # Add to PATH or reinstall uv
   pip install --upgrade uv
   ```

### Viewing Logs

```bash
# Run with verbose logging
uvicorn main:app --reload --log-level debug

# View detailed error information
uvicorn main:app --reload --access-log
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add dependencies with `uv add package-name`
5. Test your changes: `uvicorn main:app --reload`
6. Commit your changes: `git commit -am 'Add feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [troubleshooting section](#🔧-troubleshooting)
2. Visit the interactive docs at http://localhost:8000/docs
3. Create an issue in the GitHub repository
4. Check the [FastAPI documentation](https://fastapi.tiangolo.com/)
5. Check the [uv documentation](https://docs.astral.sh/uv/)

