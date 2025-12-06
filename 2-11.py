def benefit(t, n, k):
    """Tính tổng tiền (lãi kép) sau k tháng. t là lãi suất %/tháng, n là vốn, k là số tháng."""
    
    # Kiểm tra tính hợp lệ cơ bản
    if t < 0 or n <= 0 or k < 0:
        return "Lỗi: Dữ liệu đầu vào không hợp lệ (Lãi suất và Số tháng không âm, Vốn > 0)."
    
    # Công thức Lãi kép: A = n * (1 + t/100)^k
    r = t / 100  # Lãi suất dạng thập phân
    tong_tien = n * ((1 + r) ** k)
    
    return tong_tien

# ----------------------------------------------------------------------
# Nhập dữ liệu và in kết quả

try:
    # Nhập t, n, k
    t = float(input("Nhập lãi suất t (%/tháng): "))
    n = float(input("Nhập số vốn ban đầu n: "))
    k = int(input("Nhập số tháng gửi k: "))
    
    # Gọi hàm
    ket_qua = benefit(t, n, k)
    
    # In kết quả
    if isinstance(ket_qua, str):
        print(f" {ket_qua}")
    else:
        print(f"\n Tổng số tiền nhận được sau {k} tháng: {ket_qua:,.2f} VNĐ")
        
except ValueError:
    print("Lỗi: Vui lòng nhập các giá trị là số hợp lệ.")
