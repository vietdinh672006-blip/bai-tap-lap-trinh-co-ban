class py_solution:
    def roman_to_int(self, s: str) -> int:
        """
        Chuyển một chuỗi La Mã (ví dụ: "MCMXLIV") sang số nguyên.
        Trả về 0 hoặc raise ValueError nếu chuỗi rỗng/không hợp lệ.
        """
        if not s or not isinstance(s, str):
            raise ValueError("Input must be a non-empty string")

        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s.upper()
        total = 0
        for i in range(len(s)):
            if s[i] not in rom:
                raise ValueError(f"Invalid Roman numeral character: {s[i]}")
            val = rom[s[i]]
            # nếu ký tự tiếp theo có giá trị lớn hơn -> trừ (ví dụ IV -> -1 + 5)
            if i + 1 < len(s) and rom.get(s[i + 1], 0) > val:
                total -= val
            else:
                total += val
        return total

    def reverse_words(self, s: str) -> str:
        """
        Đảo ngược chuỗi theo từ (tách theo whitespace).
        Ví dụ: "hello .py" -> ".py hello"
        Giữ nguyên các khoảng trắng giữa các từ bằng cách split() bình thường.
        """
        if s is None:
            raise ValueError("Input must be a string")
        # split() mặc định tách theo bất kỳ số lượng whitespace nào
        words = s.split()
        return " ".join(reversed(words))
# Ví dụ sử dụng
if __name__ == "__main__":
    solver = py_solution()

    # Thử chuyển La Mã -> số
    examples = ["III", "IV", "IX", "LVIII", "MCMXCIV", "MMXXV"]
    for rom in examples:
        print(f"{rom} -> {solver.roman_to_int(rom)}")




