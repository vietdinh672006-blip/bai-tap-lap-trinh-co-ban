from tkinter import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry("350x200")

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

def clicked():
    # Cập nhật văn bản của Label khi nút được nhấp
    lbl.configure(text="Button was clicked !!")

# Tạo Button và thêm thuộc tính màu:
# bg="green" (background: màu nền nút)
# fg="yellow" (foreground: màu chữ)
btn = Button(window, text="Click Me", command=clicked, bg="green", fg="yellow")

btn.grid(column=1, row=0)

window.mainloop()
