from pathlib import Path
from sentence_transformers import SentenceTransformer

# 1. Đọc dữ liệu
file_path = Path("../data/clb_members.txt")
text = file_path.read_text(encoding="utf-8")

# 2. Chunking
chunks = [
    line.strip()
    for line in text.splitlines()
    if line.strip()
]

print(f"Số chunk: {len(chunks)}")

# 3. Load embedding model
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# 4. Chuyển chunks → vectors
embeddings = model.encode(chunks)

print(f"Kích thước embeddings: {embeddings.shape}")

# 5. Kiểm tra thử
for i, (chunk, embedding) in enumerate(zip(chunks, embeddings), start=1):
    print(f"\nChunk {i}:")
    print(chunk)
    print("Vector:", embedding[:5], "...")