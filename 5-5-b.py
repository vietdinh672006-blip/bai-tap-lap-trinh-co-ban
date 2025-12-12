import tkinter as tk

root = tk.Tk()
root.title("Programming Languages")

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
         padx = 20).pack(pady=10)

# 4. Vòng lặp để tạo các Indicator
for language, val in languages:
    # Sử dụng Radiobutton nhưng tùy chỉnh để trông như nút bấm chỉ báo
    tk.Radiobutton(root, 
                   text=language,
                   indicatoron = 0,     # QUAN TRỌNG: Tắt chỉ báo hình tròn (biến thành nút bấm)
                   width = 20,          # Thiết lập chiều rộng (để các nút bằng nhau)
                   padx = 20, 
                   pady = 5,            # Thêm đệm dọc để nút to hơn
                   variable=v,          # Biến liên kết là 'v'
                   command=ShowChoice,  # Gọi hàm xử lý khi được chọn
                   value=val,
                   relief=tk.RAISED     # Thêm hiệu ứng nổi (Raised) cho giống nút bấm 3D
                   ).pack(anchor=tk.W, padx=10) 
                   
root.mainloop()
