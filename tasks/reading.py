from handler.llm import call_llm

def generate_reading_task():
    
    # Nhiệm vụ của bạn chỉ bao gồm trong file này, bạn có thể tạo thêm hàm, sửa đổi nội dung trong hàm này.
    # Bạn KHÔNG được thay đổi tên hàm generate_reading_task. 
    # Bạn CÓ thể sử dụng thư viện ngoài hoặc bất kỳ công cụ gì bạn muốn, không chỉ giới hạn ở việc sử dụng LLM. 

    sample_prompt = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": "Hello! How can I assist you today?"},
            {"role": "user", "content": "Create for me a reading comprehension task based on IELTS. Only return the task, do not return any other text."},
        ]

    response = call_llm(messages=sample_prompt, model="gpt-4o-mini")

    return response 