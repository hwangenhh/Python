def count_telex_vietnamese_letters(s):
    i = 0
    count = 0
    n = len(s)

    # Các cặp đại diện cho chữ có dấu
    pairs = ['aw', 'aa', 'dd', 'ee', 'oo', 'ow']
    while i < n:
        # Kiểm tra nếu có thể lấy được 2 ký tự để xét cặp
        if i + 1 < n:
            two_chars = s[i] + s[i + 1]
            if two_chars in pairs:
                count += 1
                i += 2  # bỏ qua cặp đã xử lý
                continue
        # Nếu ký tự đơn là 'w' (ứng với ư)
        if s[i] == 'w':
            count += 1
        i += 1

    return count

#Nhập thông tin 
input_str = "haaddteeasbcoow"
print(count_telex_vietnamese_letters(input_str))  
