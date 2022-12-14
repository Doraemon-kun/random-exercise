# First semester test example program (more complicated one)
# Written by AM on 15 Dec 22
def bai1():
    try: import numpy
    except ModuleNotFoundError: print("WARN: Thu vien can dung (numpy) khong duoc tim thay, quay ve cach tinh cu"); insted = 0
    else: insted = 1
    while True:
        s1 = input("Nhap so diem dau tien: ")
        try: s1 = float(s1)
        except ValueError: print("Diem khong dung dinh dang")
        if isinstance(s1, float) and 0 <= s1 and s1 <= 10: break
        elif isinstance(s1, float): print("Diem phai tu 0 den 10")
        else: continue
    while True:
        s2 = input("Nhap so diem thu hai: ")
        try: s2 = float(s2)
        except ValueError: print("Diem khong dung dinh dang")
        if isinstance(s2, float) and 0 <= s2 and s2 <= 10: break
        elif isinstance(s2, float): print("Diem phai tu 0 den 10")
        else: continue
    while True:
        s3 = input("Nhap so diem thu ba: ")
        try: s3 = float(s3)
        except ValueError: print("Diem khong dung dinh dang")
        if isinstance(s3, float) and 0 <= s3 and s3 <= 10: break
        elif isinstance(s3, float): print("Diem phai tu 0 den 10")
        else: continue
    if insted == 0:
        av = round((s1 + s2 + s3) / 3, 4)
        if av >= 5: print(f"Diem trung binh la: {av}\nQua mon")
        elif av < 5: print(f"Diem trung binh la {av}\nKhong qua mon")
    elif insted == 1:
        lis = [s1, s2, s3]
        av = numpy.round(numpy.average(lis), 4)
        if av >= 5: print(f"Diem trung binh la: {av}\nQua mon")
        elif av < 5: print(f"Diem trung binh la {av}\nKhong qua mon")
    else: print("Loi khong xac dinh")
    return None

def bai2():
    while True:
        n = input("Nhap gia tri n nguyen: ")
        try: n = int(n)
        except ValueError: print("n khong phai so nguyen")
        if isinstance(n, int): break
        else: continue
    print(f"So gap doi: {n * 2}")
    return None

def bai3():
    name = input("Ho va ten: ")
    while True:
        chiso1 = input("Nhap chi so thang truoc: ")
        try: chiso1 = int(chiso1)
        except ValueError: print("Chi so khong dung dinh dang")
        if isinstance(chiso1, int): break
        else: continue
    while True:
        chiso2 = input("Nhap chi so thang nay: ")
        try: chiso2 = int(chiso2)
        except ValueError: print("Chi so khong dung dinh dang")
        if isinstance(chiso2, int): break
        else: continue
    diff = chiso2 - chiso1
    print(f"Ho va ten: {name}")
    if diff <= 60: print(f"Tien phai tra la: {diff * 5}")
    elif diff > 60 and diff <= 160: print(f"Tien phai tra la: {(diff - 60) * 8 + 60 * 5}")
    elif diff >= 160: print(f"Tien phai tra la: {(diff - 160) * 10 + 100 * 8 + 60 * 5}")
    else: print("Loi khong xac dinh")
    return None

def bai4():
    while True:
        a = input("So diem bi tru trong mot truong hop khong deo the hoc sinh: ")
        try: a = int(a)
        except ValueError: print("Du lieu khong dung dinh dang")
        if isinstance(a, int): break
        else: continue
    while True:
        b = input("So diem bi tru trong mot truong hop noi truyen trong lop: ")
        try: b = int(b)
        except ValueError: print("Du lieu khong dung dinh dang")
        if isinstance(b, int): break
        else: continue
    while True:
        c = input("So diem bi tru trong mot truong hop di hoc muon: ")
        try: c = int(c)
        except ValueError: print("Du lieu khong dung dinh dang")
        if isinstance(c, int): break
        else: continue
    while True:
        t = input("So truong hop khong deo the duoc ghi nhan: ")
        try: t = int(t)
        except ValueError: print("Du lieu khong dung dinh dang")
        if isinstance(t, int): break
        else: continue
    while True:
        n = input("So truong hop noi truyen trong lop duoc ghi nhan: ")
        try: n = int(n)
        except ValueError: print("Du lieu khong dung dinh dang")
        if isinstance(n, int): break
        else: continue
    while True:
        m = input("So truong hop di hoc muon duoc ghi nhan: ")
        try: m = int(m)
        except ValueError: print("Du lieu khong dung dinh dang")
        if isinstance(m, int): break
        else: continue
    total = a * t + b * n + c * m
    print(f"Tong diem bi tru: {total}")
    return None

def main():
    while True:
        print("-----------------------------------------")
        bai = input("Chon bai tap can chay (1-4): ")
        match bai:
            case "1": bai1()
            case "2": bai2()
            case "3": bai3()
            case "4": bai4()
            case _: print("Khong co bai tap nay")
        ask1 = input("Lam lai? (Y/N) ")
        if ask1 == "Y" or ask1 == "y":
            continue
        elif ask1 == "N" or ask1 =="n":
            break
        else: print("Loi khong xac dinh"); break
    return None
    
if __name__ == "__main__":
    main()