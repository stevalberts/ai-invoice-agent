# AI Invoice Agent

An intelligent system for automated invoice processing using multi-agent approaches and computer vision.

## Overview

This project implements an autonomous invoice processing system that combines computer vision, natural language processing, and multi-agent coordination to automate the extraction and processing of information from invoice documents.

## Features

- 🤖 Multi-agent system for invoice processing
- 📷 Computer vision-based document analysis
- 🔄 Automated data extraction and validation
- 🌐 REST API with FastAPI
- 🤖 ERP & CRM integration
- 🎯 Interactive UI with Streamlit
- 🔍 Support for multiple invoice formats

## Tech Stack

- Python 3.9+
- FastAPI
- Streamlit
- OpenCV
- Langchain
- PyTesseract
- Docker

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker (optional)
- UV package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-invoice-agent.git
cd ai-invoice-agent
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
uv venv
uv pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Running the Application

1. Start the API server:
```bash
python run.py --api
```

2. Start the Streamlit interface:
```bash
python run.py --ui
```

Or run both simultaneously:
```bash
python run.py --all
```

### Docker Deployment

Build and run with Docker:
```bash
docker build -t invoice-agent .
docker run -p 8000:8000 -p 8501:8501 invoice-agent
```

## Project Structure

```
ai_agent_project/
├── api/                 # FastAPI backend
├── frontend/           # Streamlit UI
├── tests/             # Test cases
├── scripts/           # Utility scripts
├── dataset/           # Training and test data
└── docs/              # Documentation
```

## Development

### Running Tests
```bash
pytest tests/
```

### Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- ICDAR 2019 SROIE dataset - https://github.com/zzzDavid/ICDAR-2019-SROIE/tree/master/data/img
- Mendeley Invoice Dataset - https://data.mendeley.com/datasets/tnj49gpmtz/2
