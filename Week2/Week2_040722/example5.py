# Ham hoan doi key va value cua Dictionary

def hoandoi_(D):
    D_kq = {}
    for i in D: 
        if D[i] not in D_kq:
            D_kq[D[i]] = i
        else:
            return None
    return D_kq

D = {"Tieng anh":"Hello","Tieng viet":"Xin chao","Tieng phap":"Bonjour","TV":"Xin chao"}
print(hoandoi_(D))