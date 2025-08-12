# prompt_manager.py
import copy

class PromptManager:
    def __init__(self, base_prompt):
        self.base_prompt = base_prompt
        self.versions = [base_prompt]
        self.scores = []

    def create_new_version(self, modification):
        new_prompt = self.base_prompt + "\n" + modification
        self.versions.append(new_prompt)
        return new_prompt

    def record_score(self, score):
        self.scores.append(score)

    def get_best_prompt(self):
        if not self.scores:
            return None
        max_index = self.scores.index(max(self.scores))
        return self.versions[max_index]
