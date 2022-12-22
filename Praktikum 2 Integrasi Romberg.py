from scipy import integrate 

function = input("Masukkan Fungsi : ")

def f(x):
    f = eval(function)
    return f

x = float(input("Masukkan batas bawah : "))
y = float(input("Masukkan batas atas : "))

romberg = integrate.romberg(f, x, y, show = True) 
print(romberg) 