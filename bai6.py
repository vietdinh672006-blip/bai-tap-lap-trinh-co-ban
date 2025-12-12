class IOString:
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())


# Chạy chương trình
str1 = IOString()
str1.get_String()
str1.print_String()
