'''
Buat sebuah program untuk menampilkan kondisi ruangan berdasarkan suhu 
ruangan.
Apabila suhu ruangan lebih besar dari 26 derajat celcius, 
maka tampilkan kalimat “Ruangan panas. Nyalakan AC”
'''

#if else suhu ruangan
suhu=int(input("Masukkan Suhu Ruangan : "))
if suhu>26:
    print("Ruangan Panas. Nyalakan AC")
else:
    print("Program Selesai")