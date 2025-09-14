#!/bin/bash

# Email Classifier API - Setup and Test Script
# This script demonstrates the workflow described in the README

echo "🚀 Email Classifier API Setup Script"
echo "====================================="

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if uv is installed
if command_exists uv; then
    echo "✅ uv is already installed"
    uv --version
else
    echo "❌ uv not found. Installing uv..."
    pip install uv
    export PATH="$PATH:$HOME/.local/bin"
fi

echo ""
echo "📦 Installing dependencies..."
uv sync

echo ""
echo "🔧 Activating virtual environment and starting server..."
echo "You can now run: source .venv/bin/activate && uvicorn main:app --reload"
echo ""
echo "🌐 Available endpoints after starting the server:"
echo "  - Home: http://localhost:8000/"
echo "  - API Docs: http://localhost:8000/docs"
echo "  - Currency Converter: POST http://localhost:8000/converter/"
echo "  - Tithe Calculator: POST http://localhost:8000/tithe_calculator/"
echo ""
echo "🧪 Test commands:"
echo "  curl http://localhost:8000/"
echo "  curl -X POST 'http://localhost:8000/converter/?naira=5000&rate=1600'"
echo "  curl -X POST 'http://localhost:8000/tithe_calculator/?salary=100000'"
echo ""
echo "✨ Setup complete! Follow the commands above to start and test your application."