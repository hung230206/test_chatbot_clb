import os
from dotenv import load_dotenv
from openai import OpenAI

# Đọc file .env
load_dotenv()

# Lấy API key
api_key = os.getenv("OPENAI_API_KEY")

# Tạo client
client = OpenAI(api_key=api_key)

# Gửi câu hỏi tới AI
response = client.responses.create(
    model="gpt-5.6",
    input="Xin chào! Hãy giới thiệu ngắn gọn về CanTho ITClub của Đại học Cần Thơ."
)

# In câu trả lời
print(response.output_text)