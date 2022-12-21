from scipy import integrate

def f(x): 
    return 1 / (1 + 9 + x)

print("\n---------- INTEGRASI ROMBERG ----------")
print("Masukkan batas bawah integrasi : ", end='')
batas_bawah = int(input())
print("Masukkan batas atas integrasi : ", end='')
batas_atas = int(input())

res = integrate.romberg(f, batas_bawah, batas_atas, show=True)
print(res)
