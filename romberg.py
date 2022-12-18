from scipy import integrate

def rmbg(x): 
    return 1 / (1 + 9 + x)

batas_bawah = int(input())
batas_atas = int(input())

res = integrate.romberg(rmbg, batas_bawah, batas_atas, show=True)
print(res)
