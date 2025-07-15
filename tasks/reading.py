from handler.llm import call_llm

# Nhiệm vụ của bạn chỉ bao gồm trong file này, bạn có thể tạo thêm hàm, sửa đổi nội dung trong hàm này.
# Bạn KHÔNG được thay đổi tên hàm generate_reading_part. 
# Bạn CÓ thể sử dụng thư viện ngoài hoặc bất kỳ công cụ gì bạn muốn, không chỉ giới hạn ở việc sử dụng LLM. 

def generate_reading_part1():
    sample_prompt = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": "Hello! How can I assist you today?"},
            {"role": "user", "content": "Create for me a reading comprehension task based on IELTS part 1. Only return the task, do not return any other text."},
        ]

    response = call_llm(messages=sample_prompt, model="openai/gpt-4o-mini")
    return response 

def generate_reading_part2():
    sample_prompt = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": "Hello! How can I assist you today?"},
            {"role": "user", "content": "Create for me a reading comprehension task based on IELTS part 2. Only return the task, do not return any other text."},
        ]

    response = call_llm(messages=sample_prompt, model="openai/gpt-4o-mini")
    return response 

def generate_reading_part3():
    sample_prompt = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": "Hello! How can I assist you today?"},
            {"role": "user", "content": "Create for me a reading comprehension task based on IELTS part 3. Only return the task, do not return any other text."},
        ]

    response = call_llm(messages=sample_prompt, model="openai/gpt-4o-mini")
    return response 