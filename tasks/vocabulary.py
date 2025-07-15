from handler.llm import call_llm

# Nhiệm vụ của bạn chỉ bao gồm trong file này, bạn có thể tạo thêm hàm, sửa đổi nội dung trong hàm này.
# Bạn KHÔNG được thay đổi tên hàm generate_vocabulary_quiz. 
# Bạn CÓ thể sử dụng thư viện ngoài hoặc bất kỳ công cụ gì bạn muốn, không chỉ giới hạn ở việc sử dụng LLM. 

def generate_vocabulary_quiz():
    vocabs_list = [
        "abandon", "ability", "able", "about", "above", "abroad", "absence", "absolute",
        "absorb", "abstract", "abundance", "academic", "acceptance", "access", "accident",
        "accommodation", "accompany", "accomplish", "according to", "account for",
        "accuracy", "achieve", "acknowledge"
    ]

    sample_prompt = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": "Hello! How can I assist you today?"},
            {"role": "user", "content": f"I have these vocabulary words: {', '.join(vocabs_list)}."},
            {"role": "user", "content": "Create for me 10 vocabulary quizzes based on the above vocabs. Only return the task, do not return any other text."},
        ]

    response = call_llm(messages=sample_prompt, model="openai/gpt-4o-mini")
    return vocabs_list, response 