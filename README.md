
# AI-Powered Text Generation and Analysis

## Project Overview
This project uses the Google Gemini API to generate
text from user prompts and analyze the generated output
using Python.

## Features
- Generate text using user prompts
- Calculate character and word counts
- Count sentences and unique words
- Measure response generation time
- Compare two generated text outputs
- Handle API errors

## Technologies Used
- Python
- Google Gemini API
- Google GenAI Python SDK
- python-dotenv

## Project Structure

```text
AITextGenerationAnalysis/
├── main.py
├── .env
├── .gitignore
├── README.md
└── venv/
```

## Requirements
- Python 3.10 or later
- Internet connection
- Google Gemini API key

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Padma416/AI-Text-Generation-Analysis.git
cd AI-Text-Generation-Analysis
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install google-genai python-dotenv
```

### 4. Configure the API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_actual_api_key_here
```

Replace the placeholder with your own API key.
Never upload your API key to GitHub.

### 5. Run the application

```bash
python main.py
```

Enter a prompt when requested. You can optionally
generate a second response to compare the outputs.

## Analysis Metrics
- Character count
- Word count
- Sentence count
- Unique word count
- Response generation time

## Limitations
Basic text statistics do not fully measure factual
accuracy, relevance, clarity, or semantic quality.

## Future Improvements
- Structured JSON output
- Advanced quality evaluation
- CSV export of analysis results
- Automated tests

## Author
Padma Sri

## GitHub Repository
https://github.com/Padma416/AI-Text-Generation-Analysis
