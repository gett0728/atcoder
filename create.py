import os

folder_name = input()
files = ["A.py", "B.py", "C.py", "D.py", "E.py", "F.py", "G.py", "memo.md"]
content = """□A問題


□B問題


□C問題


□D問題


□E問題


□F問題


□G問題

"""

try:
    os.makedirs(folder_name)
    print(f"{folder_name}を生成しました。")
except FileExistsError:
    print(f"{folder_name}は既に存在しています。") 
    exit()

for name in files:
    path = os.path.join(folder_name, name)
    with open(path, "w", encoding="utf-8") as file:
        if name == "memo.md":
            file.write(content)
    print(f"{name}を生成しました。")