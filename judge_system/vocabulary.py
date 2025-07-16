from tasks.vocabulary import generate_vocabulary_quiz
from handler.llm import call_llm
import re

def extract_score(text):
    cleaned_text = re.sub(r'\s*/\s*100\b', '', text)
    matches = list(re.finditer(r'\b(?:100|[0-9]{1,2})([.,][0-9]+)?\b', cleaned_text))
    if matches:
        last_match = matches[-1].group().replace(',', '.')
        return float(last_match)
    return 0.0

def vocabulary_evaluation():
    scores = []

    print("")
    for i in range(3):
        print(f"[SYSTEM] Evaluating vocabulary quiz iteration {i + 1}")
        vocabs_set, task  = generate_vocabulary_quiz()
        
        with open(f"judge_system/output/vocabulary/quiz{i + 1}.txt", "w", encoding="utf-8") as out_f:
            out_f.write(str(task))

        with open("judge_system/evaluation_prompts/vocabulary.txt", "r", encoding="utf-8") as f:
            eval_prompt = f.read()

            messages = [
                {"role": "developer", "content": "You are an IELTS examiner. Be strict and honest."},
                {"role": "user", "content": f"Regarding the given Vocabulary Quiz on the given Vocab and Phrases Set."},
                {"role": "user", "content": f"Vocab and Phrases Set: {', '.join(vocabs_set)}"},
                {"role": "user", "content": f"Quizzes: {task}"},
                {"role": "user", "content": f"{eval_prompt}"}
            ]

            score1 = call_llm(messages=messages, model="google/gemini-2.5-flash")
            score2 = call_llm(messages=messages, model="google/gemini-2.0-flash-001")
            score3 = call_llm(messages=messages, model="google/gemini-2.5-pro")

            with open(f"judge_system/output/vocabulary/quiz{i+1}_llm_feedback.txt", "w", encoding="utf-8") as out_f:
                out_f.write(str(score1) + "\n=====\n" + str(score2) + "\n=====\n" + str(score3))

            score1 = extract_score(score1)
            score3 = extract_score(score3)
            score2 = extract_score(score2)
            print(f"[LLM] Score by google/gemini-2.5-flash: {score1}")
            print(f"[LLM] Score by google/gemini-2.0-flash-001: {score2}")
            print(f"[LLM] Score by google/gemini-2.5-pro: {score3}")

            score = sorted([float(score1), float(score2), float(score3)])[1]

            scores.append(float(score))
            print(f"[SYSTEM] Score: {score}\n")

    print(f"[SYSTEM] Average score: {sum(scores) / len(scores)}")

    return sum(scores) / len(scores)