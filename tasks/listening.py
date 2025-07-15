from handler.llm import call_llm

# Nhiệm vụ của bạn chỉ bao gồm trong file này, bạn có thể tạo thêm hàm, sửa đổi nội dung trong hàm này.
# Bạn KHÔNG được thay đổi tên hàm generate_listening_part. 
# Bạn CÓ thể sử dụng thư viện ngoài hoặc bất kỳ công cụ gì bạn muốn, không chỉ giới hạn ở việc sử dụng LLM. 

def generate_listening_part1():
    sample_prompt = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": "Hello! How can I assist you today?"},
            {"role": "user", "content": "Generate a sample IELTS Listening part 1 test, providing the script of dialogue (and the speakers, e.g {Announcer, Bob, Eric}). Generate the questions and provide the answers; the questions should be weaved between conversation and announcer's dialogue. Make the test follow the format mentioned in https://github.com/gpoore/text2qti/blob/master/README.md. The test has two tasks: Multiple Choice Questions (5) and Information Matching(5). Refer to online resources for more accurate portraits of the IELTS Listening part 1 test"},
        ]
    response = call_llm(messages=sample_prompt, model="openai/gpt-4o-mini")
    return response 

def generate_listening_part2():
    sample_prompt = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": "Hello! How can I assist you today?"},
            {"role": "user", "content": "Generate a sample IELTS Listening part 2 test, providing the script of dialogue (and the speakers, e.g {Announcer, Bob, Eric}). Generate the questions and provide the answers; the questions should be weaved between conversation and announcer's dialogue. Make the test follow the format mentioned in https://github.com/gpoore/text2qti/blob/master/README.md. The test has two tasks: Multiple Choice Questions (5) and Information Matching(5). Refer to online resources for more accurate portraits of the IELTS Listening part 2 test"},
        ]
    response = call_llm(messages=sample_prompt, model="openai/gpt-4o-mini")
    return response 

def generate_listening_part3():
    sample_prompt = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": "Hello! How can I assist you today?"},
            {"role": "user", "content": "Generate a sample IELTS Listening part 3 test, providing the script of dialogue (and the speakers, e.g {Announcer, Bob, Eric}). Generate the questions and provide the answers; the questions should be weaved between conversation and announcer's dialogue. Make the test follow the format mentioned in https://github.com/gpoore/text2qti/blob/master/README.md. The test has two tasks: Multiple Choice Questions (5) and Information Matching(5). Refer to online resources for more accurate portraits of the IELTS Listening part 3 test"},
        ]
    response = call_llm(messages=sample_prompt, model="openai/gpt-4o-mini")
    return response 

def generate_listening_part4():
    sample_prompt = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": "Hello! How can I assist you today?"},
            {"role": "user", "content": "Generate a sample IELTS Listening part 4 test, providing the script of dialogue (and the speakers, e.g {Announcer, Bob, Eric}). Generate the questions and provide the answers; the questions should be weaved between conversation and announcer's dialogue. Make the test follow the format mentioned in https://github.com/gpoore/text2qti/blob/master/README.md. The test has two tasks: Multiple Choice Questions (5) and Information Matching(5). Refer to online resources for more accurate portraits of the IELTS Listening part 4 test"},
        ]
    response = call_llm(messages=sample_prompt, model="openai/gpt-4o-mini")
    return response 