# GenAI Projects

A collection of Generative AI projects demonstrating LLM chains, Streamlit applications, and Google GenAI integration.

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Windows/Linux/macOS

## Project Structure

```
GenAI/
├── project_01_basic_llm_chain/
│   └── app.ipynb
├── env-example.md
└── Readme.md
```

## Setup Instructions

### 1. Install UV (Package Manager)

Install UV globally using pip:

```bash
pip install uv
```

### 2. Create Virtual Environment

Create a virtual environment using UV:

```bash
uv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Required Dependencies

Install the core dependencies for LangChain, Google GenAI, and Streamlit:

```bash
uv pip install streamlit langchain-google-genai google-genai python-dotenv
```

### 5. Install Jupyter (Optional)

If you plan to work with Jupyter notebooks:

```bash
uv pip install jupyter ipykernel
```

## Getting Started

1. Navigate to the project directory
2. Ensure your virtual environment is activated
3. Create a `.env` file based on `env-example.md` with your API credentials
4. Run Jupyter notebooks or Streamlit apps as needed

## Usage

### Running Jupyter Notebooks

```bash
jupyter notebook
```

Navigate to `project_01_basic_llm_chain/app.ipynb`

### Running Streamlit Applications

```bash
streamlit run app.py
```

## Dependencies

- **streamlit**: Web app framework
- **langchain-google-genai**: LangChain integration with Google Generative AI
- **google-genai**: Google's generative AI SDK
- **python-dotenv**: Environment variable management
- **jupyter**: Interactive notebook environment (optional)
- **ipykernel**: IPython kernel for Jupyter (optional)

## Environment Configuration

Create a `.env` file in the root directory with your API keys:

```
GOOGLE_API_KEY=your_api_key_here
```

Refer to `env-example.md` for additional configuration options.

## Support

For issues or questions, please refer to the documentation of the respective libraries:
- [LangChain Documentation](https://python.langchain.com/)
- [Google GenAI Documentation](https://ai.google.dev/)
- [Streamlit Documentation](https://docs.streamlit.io/)