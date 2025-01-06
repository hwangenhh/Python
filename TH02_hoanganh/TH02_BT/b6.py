#xác định nguyên âm/phụ âm
n = input("Nhập vào một ký tự chữ cái: ")
n = n.lower()

vowels = "aeiou"

if n in vowels:
    print(f"{n} là nguyên âm.")
else:
    print(f"{n} là phụ âm.")