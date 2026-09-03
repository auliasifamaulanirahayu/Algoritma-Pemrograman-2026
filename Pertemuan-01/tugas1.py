import math

def hitung_lingkaran(r):
    luas = math.pi * (r ** 2)
    keliling = 2 * math.pi * r
    return luas, keliling

# Input dari pengguna
r = float(input("Masukkan panjang jari-jari lingkaran (r): "))

# Proses
luas, keliling = hitung_lingkaran(r)

# Output
print(f"Luas Lingkaran     : {luas:.2f}")
print(f"Keliling Lingkaran : {keliling:.2f}")