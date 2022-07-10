# Nhap vao mot chuoi, kiem tra chuoi co phai la mat khau manh hay khong 

chuoi = input("Nhap chuoi: ")
ktdodai = len(chuoi) > 6
ktdacbiet = ktinthuong = ktinhoa = ktso = False

for i in chuoi:
    if i.isnumeric():
        ktsp = True
    elif i.isupper():
        ktinhoa = True
    elif i.islower():
        ktinthuong = True
    else: 
        ktdacbiet = True
if ktdodai and ktso and ktinhoa and ktinthuong and ktdacbiet:
    print("Mat khau manh!")
else:
    print("Mat khau khong manh!")
    
