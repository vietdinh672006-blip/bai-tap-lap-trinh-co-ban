import turtle, random

# Danh sách các màu sẽ được sử dụng
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Thiết lập bút vẽ
painter = turtle.Turtle()
painter.pensize(3)
painter.speed(0) # Đặt tốc độ vẽ nhanh nhất

# Vòng lặp để vẽ 100 vòng tròn đan xen
for x in range(100):
    # Chọn màu ngẫu nhiên
    color = random.choice(colors)
    painter.pencolor(color)
    
    # Vẽ vòng tròn
    painter.circle(100)
    
    # Xoay bút vẽ để tạo hiệu ứng đan xen
    painter.right(6)
    
    # Lệnh dưới đây có thể không cần thiết để tạo hình ảnh cụ thể này,
    # nhưng được giữ nguyên theo mã nguồn gốc:
    painter.left(60) 
    
# Đưa bút vẽ về vị trí trung tâm (0, 0)
painter.setposition(0, 0)

# Giữ cửa sổ đồ họa mở
turtle.done()
