from sentence_transformers import SentenceTransformer

print("Đang tải model...")

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

print("Load model thành công!")

text = "Câu lạc bộ tổ chức cuộc thi lập trình"

embedding = model.encode(text)

print("Text:")
print(text)

print("\nVector:")
print(embedding)

print("\nKích thước vector:")
print(embedding.shape)