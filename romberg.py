from scipy import integrate

def f(x): 
    return 1 / (1 + 9 + x)

print("\n---------- INTEGRASI ROMBERG ----------")
batas_bawah = int(input("Masukkan batas bawah integrasi : "))
batas_atas = int(input("Masukkan batas atas integrasi : "))

res = integrate.romberg(f, batas_bawah, batas_atas, show=True)
print(res)
