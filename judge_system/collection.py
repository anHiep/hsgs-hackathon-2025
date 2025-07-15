import glob
from handler.llm import call_llm

def collection_evaluation():
    print("\n[SYSTEM] Evaluating all collection and format quizzes")

    total = 0
    score = 0

    with open("judge_system/output/collection/result.txt", "w") as out_f:
        with open("judge_system/evaluation_prompts/collection.txt", "r") as f:
            eval_prompt = f.read()

        for filepath in glob.glob("tasks/collection-w-format/bank/*.txt"):
            with open(filepath, "r") as quiz_file:
                quiz_content = quiz_file.read()

            messages = [
                {"role": "system", "content": "You are an IELTS examiner. Be strict and honest."},
                {"role": "user", "content": f"Quiz:\n{quiz_content}"},
                {"role": "user", "content": f"{eval_prompt}"}
            ]

            feedback = call_llm(messages=messages, model="openai/gpt-4o-mini")

            if "Correct" in feedback:
                score += 1
                print(f"[LLM] {filepath}: Correct Format")
            else:
                print(f"[LLM] {filepath}: Wrong Format or Language & Grammar Error")

            total += 1
            out_f.write(f"{filepath}: {feedback}\n")

    average_score = score / total if total > 0 else 0
    print(f"[SYSTEM] Average score: {average_score:.2f}")
    return average_score
