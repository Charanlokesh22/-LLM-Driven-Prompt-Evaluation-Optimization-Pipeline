 LLM-Driven Prompt Evaluation & Optimization Pipeline

 Project Overview

This project is an automated pipeline designed to create, evaluate, and optimize prompt versions for large language models (LLMs) used in financial AI applications. It enables continuous improvement of prompt quality by generating, scoring, and selecting the best prompts to maximize accuracy and reduce hallucinations. This pipeline supports AI agents handling transaction analysis, financial reporting, and customer communication, ensuring precise and reliable output.

 Features

- Prompt Versioning: Create and manage multiple prompt variants to test and improve model responses.  
- Automated Scoring: Evaluate prompt outputs using a custom heuristic to detect hallucinations and uncertainty.  
- Performance Metrics: Compute average scores on sample financial queries for objective prompt comparison.  
- Best Prompt Selection: Automatically select the highest performing prompt for deployment.  
- Modular Design: Easily integrates with OpenAI’s GPT models and can be extended to other LLM providers or datasets.  
- Sample Financial Data: Includes example transaction data for prompt testing.

 Tech Stack

- Python 3.8+  
- OpenAI GPT-3 API (text-davinci-003 engine)  
- Python libraries: langchain (optional), requests  
- Development Tools: Git, virtual environments

 Getting Started

 Prerequisites

- Python 3.8 or higher  
- OpenAI API key (sign up at https://beta.openai.com/signup/)  
- Git installed

 Clone the Repository

bash
git clone https://github.com/Charanlokesh22/llm-prompt-eval-optimization-pipeline.git
cd llm-prompt-eval-optimization-pipeline

Setup Virtual Environment and Install Dependencies

-python -m venv venv
-source venv/bin/activate       
-venv\Scripts\activate          
-pip install -r requirements.txt

Configure API Key
- OPENAI_API_KEY = "your-openai-api-key-here"

Run the Pipeline
-python app.py

