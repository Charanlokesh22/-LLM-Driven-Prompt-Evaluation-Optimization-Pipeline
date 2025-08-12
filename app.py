# app.py
import json
from config import OPENAI_API_KEY
from prompt_manager import PromptManager
from evaluation import evaluate_prompt

def main():
    # Load sample financial questions for testing
    with open('data/financial_dataset.json', 'r') as f:
        data = json.load(f)

    base_prompt = "You are a financial AI agent. Answer the questions accurately."

    prompt_manager = PromptManager(base_prompt)

    # Create some prompt versions
    mod1 = "Please be concise and factual."
    mod2 = "Avoid speculation and clearly state if you don't know."

    prompt_manager.create_new_version(mod1)
    prompt_manager.create_new_version(mod2)

    # Evaluate each prompt version
    for i, prompt in enumerate(prompt_manager.versions):
        total_score = 0
        print(f"\nEvaluating Prompt Version {i}:")
        for entry in data:
            question = entry['description']
            answer, score = evaluate_prompt(prompt, question, OPENAI_API_KEY)
            print(f"Q: {question}\nA: {answer}\nScore: {score}\n")
            total_score += score
        avg_score = total_score / len(data)
        prompt_manager.record_score(avg_score)
        print(f"Average Score for Prompt Version {i}: {avg_score}")

    best_prompt = prompt_manager.get_best_prompt()
    print("\nBest Prompt Found:")
    print(best_prompt)

if __name__ == "__main__":
    main()
