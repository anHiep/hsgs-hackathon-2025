from config import TASK_ID

if TASK_ID not in [1, 2, 3, 4]:
    print("[SYSTEM] Invalid TASK_ID. Please set it to 1 (READING), 2 (LISTENING), or 3 (COLLECTION & FORMAT) in config.")
    exit(1)

print(f"[SYSTEM] Running task with name: {'READING' if TASK_ID == 1 else 'LISTENING' if TASK_ID == 2 else 'COLLECTION & FORMAT' if TASK_ID == 3 else 'VOCABULARY'}")

if TASK_ID == 1:
    from judge_system.reading import reading_evaluation
    overall_score = reading_evaluation()

if TASK_ID == 2:
    from judge_system.listening import listening_evaluation
    overall_score = listening_evaluation()

if TASK_ID == 3:
    from judge_system.collection import collection_evaluation
    overall_score = collection_evaluation()

if TASK_ID == 4:
    from judge_system.vocabulary import vocabulary_evaluation
    overall_score = vocabulary_evaluation()