'''
Buat sebuah program untuk menampilkan kondisi ruangan berdasarkan suhu 
ruangan.
Apabila suhu ruangan lebih besar dari 26 derajat celcius, 
maka tampilkan kalimat “Ruangan panas. Nyalakan AC”
'''

#if then suhu ruangan
suhu=int(input("Masukkan Suhu Ruangan : "))
if suhu>26:
    print("Ruangan Panas. Nyalakan AC")
print("Program Selesai")

'''
Buat sebuah program untuk menampilkan kondisi ruangan berdasarkan suhu ruangan.
Apabila suhu ruangan lebih besar dari 26 derajat celcius, maka tampilkan kalimat 
“Ruangan panas. Nyalakan AC”. Apabila tidak, tampilkan kalimat “Matikan AC.”

'''
#if then else suhu ruangan
suhuruang=int(input("Masukkan Suhu Ruangan : "))
if suhuruang>26:
    print("Ruangan Panas. Nyalakan AC")
else:
    print("Matikan AC.")
print("Program Selesai")
