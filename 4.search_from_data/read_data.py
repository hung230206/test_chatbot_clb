from pathlib import Path

file_path = Path("../data/clb_members.txt")

text = file_path.read_text(encoding="utf-8")

print("=== NỘI DUNG FILE ===")
print(text)

print("\n=== SỐ KÝ TỰ ===")
print(len(text))