from pathlib import Path

file_path = Path("../data/clb_members.txt")

text = file_path.read_text(encoding="utf-8")

# Chia theo từng dòng
chunks = [
    line.strip()
    for line in text.splitlines()
    if line.strip()
]

print(f"Số chunk: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}:")
    print(chunk)