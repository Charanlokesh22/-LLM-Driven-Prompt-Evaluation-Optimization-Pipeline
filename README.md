LLM-Driven Prompt Evaluation & Optimization Pipeline
Project Overview
This project implements an automated pipeline designed to create, evaluate, and optimize prompt versions for large language models (LLMs) used in financial AI applications. The pipeline enables continuous improvement of prompt quality by scoring LLM outputs, detecting hallucinations, and selecting the best performing prompts to enhance response accuracy and reliability.

This solution supports finance-focused AI agents by improving the fidelity of answers related to transaction analysis, reporting, and client communications. The modular design facilitates easy integration with OpenAI’s GPT models and can be extended with advanced evaluation heuristics for production-grade use.

Key Features
Prompt Versioning: Easily create and manage multiple prompt variants to test different wording and instructions.

Automated Evaluation: Generate answers using LLMs and score them using a custom heuristic to detect hallucinations or uncertainty.

Performance Metrics: Calculate average prompt scores over sample financial queries for objective comparison.

Best Prompt Selection: Automatically identify the highest performing prompt to deploy in AI workflows.

Modular & Extensible: Designed for integration with OpenAI API and easy adaptation to other LLM providers or datasets.

Sample Financial Dataset: Included sample transactions for prompt testing and evaluation.

Tech Stack & Tools
Programming Language: Python 3.8+

APIs: OpenAI GPT-3 (text-davinci-003 engine)

Libraries:

langchain (optional, for future extensions)

requests (for API calls)

Development Tools: Git, virtual environments

Getting Started
Prerequisites
Python 3.8 or higher installed

OpenAI API key (sign up at OpenAI)

Git installed for cloning the repo

Clone the Repository
bash
Copy code
git clone https://github.com/your-username/llm-prompt-eval-optimization-pipeline.git
cd llm-prompt-eval-optimization-pipeline
Setup Virtual Environment and Install Dependencies
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate       # For Linux/macOS
venv\Scripts\activate          # For Windows
Install required Python packages:

bash
Copy code
pip install -r requirements.txt
Configuration
Add your OpenAI API key to the config.py file:

python
Copy code
OPENAI_API_KEY = "your-openai-api-key-here"
Running the Pipeline
Start the evaluation and optimization pipeline by running:

bash
Copy code
python app.py
The script will:

Load the sample financial transaction dataset.

Create multiple prompt versions.

Generate answers to financial queries using OpenAI GPT.

Score the answers for accuracy and hallucination detection.

Output average scores per prompt version.

Display the best prompt to use in production.
