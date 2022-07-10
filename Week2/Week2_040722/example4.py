# Nhap vao list L, xay dung list K theo yeu cau 

L = input("Nhap L: ")
L = L.split(",")
for i in range(len(L)):
    if L[i].isnumeric():
        L[i] = int(L[i])
if len(L) % 2 == 0:
    kq = True 
    for i in range(len(L) - 1):
        if not ((type(L[i]) is str and type(L[i + 1]) is int) or (type(L[i]) is int and type(L[i + 1]) is str)) :
            kq = False 
            break 
    if kq:
        K = []
        for i in range(0,len(L)//2,2):
            K.append(L[i]*L[i+1])
        print("K = ",K)
    else:
        print("Khong the xay dung list K vi list L khong phai dang chuoi so xen ke!")
else:
    print("Khong the xay dung list K vi phan tu cua L la le")
