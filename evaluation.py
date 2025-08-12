# evaluation.py
import openai

def evaluate_prompt(prompt, question, openai_api_key):
    openai.api_key = openai_api_key
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{prompt}\nQuestion: {question}\nAnswer:",
            max_tokens=150,
            temperature=0
        )
        answer = response.choices[0].text.strip()
        score = score_answer(answer)
        return answer, score
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return None, 0

def score_answer(answer):
    # Simple heuristic: penalize hallucinations by checking for phrases like "I don't know"
    negative_phrases = ["I don't know", "cannot answer", "not sure", "unknown"]
    score = 1.0
    for phrase in negative_phrases:
        if phrase in answer.lower():
            score -= 0.5
    # Score normalized between 0 and 1
    return max(score, 0)
