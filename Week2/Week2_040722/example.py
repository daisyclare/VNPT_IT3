# Giai phuong trinh ax^2 + bx + c = 0

a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
c = float(input("Nhap so c: "))
print("Phuong trinh " + str(a) + "x^2 + "+ str(b) + "x + " + str(c) + " = 0" )
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem")
        else: 
            print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co mot nghiem:",c/b)
else: 
    d = b**2 - 4*a*b
    if d > 0:
        cand = d**0.5
        x1 = (-b + cand)/(2*a)
        x2 = (-b - cand)/(2*a)
        print("Phuong trinh co hai nghiem la: ",x1," va ", x2)
    elif d == 0:
        print("Phuong trinh co mot nghiem kep: ",-b/(2*a))
    else: 
        print("Phuong trinh vo nghiem")