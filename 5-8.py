import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi nút 'Click Me' được bấm
def show_selection():
    # Lấy giá trị hiện tại của radio button (1, 2, hoặc 3)
    selected_value = v.get()
    
    # Lấy thông tin từ các ô nhập liệu
    ho_ten = entry_ten.get()
    ngay_sinh = entry_ngay_sinh.get()
    mssv = entry_mssv.get()
    nganh_hoc = entry_nganh_hoc.get()
    
    # Hiển thị thông tin đã nhập
    info_message = f"Thông tin đã nhập:\n" \
                   f"Họ tên: {ho_ten}\n" \
                   f"Ngày sinh: {ngay_sinh}\n" \
                   f"MSSV: {mssv}\n" \
                   f"Ngành học: {nganh_hoc}\n\n" \
                   f"Lựa chọn Radio Button (Welcome/First/Second/Third): {selected_value}"
                   
    # In ra giá trị của Radio Button (theo yêu cầu đề bài)
    print(f"Giá trị Radio Button đã chọn: {selected_value}")
    
    # Hiển thị thông báo tổng hợp
    messagebox.showinfo("Kết quả", info_message)


# ----------------------------------------------------
# 1. Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Form Thông tin & Radio Buttons")

# ----------------------------------------------------
# A. Khung Thông tin Cá nhân (Sử dụng Frame để nhóm)
# ----------------------------------------------------
info_frame = tk.LabelFrame(root, text="Thông tin Cá nhân", padx=10, pady=10)
info_frame.pack(padx=10, pady=10, fill="x")

# Tạo các Label và Entry cho Thông tin Cá nhân
# Họ tên
tk.Label(info_frame, text="Họ tên:").grid(row=0, column=0, sticky="w", pady=2)
entry_ten = tk.Entry(info_frame, width=30)
entry_ten.grid(row=0, column=1, padx=5, pady=2)

# Ngày tháng năm sinh
tk.Label(info_frame, text="Ngày sinh:").grid(row=1, column=0, sticky="w", pady=2)
entry_ngay_sinh = tk.Entry(info_frame, width=30)
entry_ngay_sinh.grid(row=1, column=1, padx=5, pady=2)

# MSSV
tk.Label(info_frame, text="MSSV:").grid(row=2, column=0, sticky="w", pady=2)
entry_mssv = tk.Entry(info_frame, width=30)
entry_mssv.grid(row=2, column=1, padx=5, pady=2)

# Ngành học
tk.Label(info_frame, text="Ngành học:").grid(row=3, column=0, sticky="w", pady=2)
entry_nganh_hoc = tk.Entry(info_frame, width=30)
entry_nganh_hoc.grid(row=3, column=1, padx=5, pady=2)


# ----------------------------------------------------
# B. Khung Radio Button & Button (Theo hình mẫu)
# ----------------------------------------------------
radio_frame = tk.LabelFrame(root, text="Lựa chọn", padx=10, pady=10)
radio_frame.pack(padx=10, pady=10, fill="x")

# 1. Biến điều khiển cho Radio Button
v = tk.IntVar()
v.set(1) # Giá trị mặc định là 1 (Welcome)

# 2. Tạo các Radio Button (sử dụng pack để căn chỉnh ngang)
rb_welcome = tk.Radiobutton(radio_frame, text="Welcome", variable=v, value=1)
rb_welcome.pack(side=tk.LEFT, padx=5)

rb_first = tk.Radiobutton(radio_frame, text="First", variable=v, value=2)
rb_first.pack(side=tk.LEFT, padx=5)

rb_second = tk.Radiobutton(radio_frame, text="Second", variable=v, value=3)
rb_second.pack(side=tk.LEFT, padx=5)

rb_third = tk.Radiobutton(radio_frame, text="Third", variable=v, value=4) # Thêm 'Third' theo hình
rb_third.pack(side=tk.LEFT, padx=5)

# 3. Tạo Button 'Click Me'
btn_click = tk.Button(radio_frame, text="Click Me", command=show_selection)
btn_click.pack(side=tk.LEFT, padx=15)


root.mainloop()
