import random
angka=random.randint(1,10)
percobaan=1
while True:
    tebak =input("Silahkan tebak angka dari 1-100: ")
    if angka == int(tebak):
        print("Selamat anda berhasil menebak. Jawaban =",angka)
        break
    else:
        print("Jawaban anda salah.")
        percobaan=percobaan+1
    if angka>int(tebak):
        print("Tebak angka yang lebih besar.")
    else:
        print("Tebak angka yang lebih kecil.")
print("Anda berhasil menebak benar dalam",percobaan,"kali percobaan")      
