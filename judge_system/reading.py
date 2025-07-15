from tasks.reading import generate_reading_task
from handler.llm import call_llm
import re

def extract_score(text):
    matches = list(re.finditer(r'\b([0-9]{1,2}|100)\b', text))
    if matches:
        return int(matches[-1].group())
    return 0

def reading_evaluation():
    scores = []

    print("")
    for i in range(3):
        print(f"[SYSTEM] Evaluating reading task iteration {i + 1}")
        task = generate_reading_task()

        with open("judge_system/evaluation_prompts/reading.txt", "r") as f:
            eval_prompt = f.read()

            messages = [
                {"role": "developer", "content": "You are an IELTS examiner. Be strict and honest."},
                {"role": "user", "content": f"{task}"},
                {"role": "user", "content": f"{eval_prompt}"}
            ]

            score1 = call_llm(messages=messages, model="google/gemini-2.5-flash")
            score1 = extract_score(score1)
            print(f"[LLM] Score by google/gemini-2.5-flash: {score1}")
            score2 = call_llm(messages=messages, model="google/gemini-2.0-flash-001")
            score2 = extract_score(score2)
            print(f"[LLM] Score by google/gemini-2.0-flash-001: {score2}")
            score3 = call_llm(messages=messages, model="openai/gpt-4o-mini")
            score3 = extract_score(score3)
            print(f"[LLM] Score by openai/gpt-4o-mini: {score3}")

            score = min(int(score1), int(score2), int(score3))

            scores.append(int(score))
            print(f"[SYSTEM] Score: {score}\n")

    print(f"[SYSTEM] Average score: {sum(scores) / len(scores)}")

    return sum(scores) / len(scores)