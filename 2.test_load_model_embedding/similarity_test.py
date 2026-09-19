from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

texts = [
    "CLB tổ chức cuộc thi lập trình",
    "Câu lạc bộ có tổ chức contest code",
    "Hôm nay tôi đi ăn cơm"
]

embeddings = model.encode(texts)

similarity = cosine_similarity(embeddings)

for i in range(len(texts)):
    for j in range(i + 1, len(texts)):
        print(f"\nCâu {i+1}: {texts[i]}")
        print(f"Câu {j+1}: {texts[j]}")
        print(f"Similarity: {similarity[i][j]:.4f}")