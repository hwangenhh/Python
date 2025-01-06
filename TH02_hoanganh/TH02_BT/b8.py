#Xác định mùa trong năm
thang = float(input("Nhập tháng: "))
if thang <= 3:
    print("Bạn sinh vào Mùa xuân")
elif thang <= 6:
        print("Bạn sinh vào Mùa hạ")
elif thang <= 9:
        print("Bạn sinh vào Mùa thu")
elif thang <=12:
       print("Bạn sinh vào Mùa đông")
elif thang < 1 or thang > 12:
       print("Tháng sinh nhập vào không đúng")


    