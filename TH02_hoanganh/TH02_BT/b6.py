letter = input("Nhập vào một ký tự chữ cái: ")
letter = letter.lower()

vowels = "aeiou"

if letter in vowels:
    print(f"{letter} là nguyên âm.")
else:
    print(f"{letter} là phụ âm.")