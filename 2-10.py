import math

def Tinh(R):
    """Tính chu vi (C) và diện tích (S) hình tròn với bán kính R,
       và kiểm tra R >= 0."""
    
    # 1. Kiểm tra R hợp lệ
    if R < 0:
        return "Lỗi: Bán kính R phải là số không âm."
    
    # 2. Tính toán
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * (R ** 2)
    
    # 3. Trả về kết quả
    return chu_vi, dien_tich

# ----------------------------------------------------------------------
# Nhập R từ bàn phím và xử lý lỗi

try:
    # Nhập R và ép kiểu sang float
    R_input = input("Nhập bán kính R: ")
    R = float(R_input)
    
    # Gọi hàm và xử lý kết quả
    ket_qua = Tinh(R)
    
    if isinstance(ket_qua, str):
        # In thông báo lỗi nếu R < 0
        print(ket_qua) 
    else:
        # In kết quả nếu R hợp lệ
        chu_vi, dien_tich = ket_qua
        print(f"\n Với R = {R}:")
        print(f"   Chu vi (C): {chu_vi:.4f}")
        print(f"   Diện tích (S): {dien_tich:.4f}")
        
except ValueError:
    print(f" Lỗi: Giá trị '{R_input}' không phải là một số hợp lệ.")
