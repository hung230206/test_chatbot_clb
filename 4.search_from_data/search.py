from pathlib import Path

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# 1. Đọc data
file_path = Path("../data/clb_members.txt")

text = file_path.read_text(encoding="utf-8")

chunks = [
    line.strip()
    for line in text.splitlines()
    if line.strip()
]



 # 2. Load embedding model
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)



# 3. Tạo embedding cho chunks


chunk_embeddings = model.encode(chunks)


while True:

    # Queêry

    query = input("Bạn hỏi: ")


    # 5. Embedding câu hỏi


    query_embedding = model.encode([query])



    # 6. Tính similarity


    scores = cosine_similarity(
        query_embedding,
        chunk_embeddings
    )[0]



    # 7. Sort similảity


    results = sorted(
        zip(chunks, scores),
        key=lambda x: x[1],
        reverse=True
    )


    # KQ

    print("\n-----------KẾT QUẢ-----------------")

    for i, (chunk, score) in enumerate(results[:5], start=1):
        print(f"\n{i}. Similarity: {score:.4f}")
        print(f"   {chunk}")

        # Cần tối ưu