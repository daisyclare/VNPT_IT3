#Viet chuong trinh nhap so luong mon an va in hoa don

print("Chao mung den voi nha hang thuc an nhanh!")
print("Moi ban nhap so luong mon: ")
print()
sl_garan = int(input("Ga ran: "))
sl_ham = int(input("Hamburger: "))
sl_coca = int(input("Cocacola: "))
print()

def dinhdang(s):
    while len(s) < 20:
        s += " "
    return s

print("HOA DON: ")
print(dinhdang("Ga ran") + "30.000 x " + str(sl_garan))
print(dinhdang("Hamburger") + "25.000 x " + str(sl_ham))
print(dinhdang("Cocacola") + "10.000 x " + str(sl_coca))
print()
print("Tong: ")

def phancachngan(a):
    a = str(a)
    i = len(a) - 3
    while i > 0:
        a = a[:i] + "." + a[i:]
        i -= 3
    return a 
print(dinhdang("Ga ran") + phancachngan(30000*sl_garan) + " VND")
print(dinhdang("Hamburger") + phancachngan(25000*sl_ham) + " VND")
print(dinhdang("Cocacola") + phancachngan(10000*sl_coca) + " VND")
tong = 30000*sl_garan + 25000*sl_ham + 10000*sl_coca
print(dinhdang("Tong truoc thue: ") + phancachngan(tong) + " VND")
print(dinhdang("Thue (5%)")+ phancachngan(int(tong*0.05)) + " VND")
print(dinhdang("Tong sau thue: ")+ phancachngan(int(tong*1.05)) + " VND")