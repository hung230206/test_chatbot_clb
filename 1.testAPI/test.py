import os
from dotenv import load_dotenv
from openai import OpenAI

# Đọc file .env
load_dotenv()

# Lấy API key
api_key = os.getenv("OPENAI_API_KEY")

# Tạo client
client = OpenAI(api_key=api_key)
while True:
    question = input("Bạn: ").strip()

    if question.lower() == "exit":
        break

    if not question:
        print("Bot: Bạn chưa nhập câu hỏi ?!???!?!")
        continue

    response = client.responses.create(
        model="gpt-5.6",
        input=question
    )

    print("Bot:", response.output_text)