import tkinter as tk

root = tk.Tk()

# 1. Khai báo biến control Int để theo dõi lựa chọn
v = tk.IntVar() 
v.set(1) # Thiết lập giá trị mặc định là 1 (Python)

# Danh sách các ngôn ngữ: (Tên hiển thị, Giá trị gán cho biến v)
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C#", 5)
]

# 2. Định nghĩa hàm xử lý khi có lựa chọn
def ShowChoice():
    # In ra giá trị số của lựa chọn hiện tại (1, 2, 3, 4, hoặc 5)
    print(v.get()) 

# 3. Tạo Label tiêu đề
tk.Label(root, 
         text="""***Choose your favourite
programming language:***""",
         justify = tk.LEFT,
         padx = 20).pack()

# 4. Vòng lặp để tạo các Radio Button
# 'val' là chỉ số (0, 1, 2...), 'language' là tuple ('Python', 1)
for language, val in languages:
    tk.Radiobutton(root, 
                   text=language,       # Tên hiển thị trên Radio Button
                   padx = 20,           # Khoảng đệm ngang
                   variable=v,          # Biến liên kết là 'v' (IntVar)
                   command=ShowChoice,  # Gọi hàm ShowChoice khi được chọn
                   value=val).pack(anchor=tk.W) # Giá trị gán cho 'v' khi được chọn, căn lề trái (tk.W)

root.mainloop()
