'''
Buat sebuah program untuk menampilkan kondisi ruangan berdasarkan suhu ruangan.
Apabila suhu ruangan lebih besar dari 26 derajat celcius, maka tampilkan kalimat “Ruangan panas. Nyalakan AC”.
Apabila tidak, tampilkan kalimat “Matikan AC.”
'''

suhuruang=int(input("Berapa Suhu Ruangan : "))
if suhuruang>26:
    print("Ruangan Panas. Nyalakan AC")
else:
    print("Matikan AC")


'''
Program angka positif

Terdapat sebuah program untuk menentukan apakah sebuah 
angka bilangan positif atau bilangan negatif. 
Apabila angka lebih besar dari 0 maka tampilkan 
“Angka adalah bilangan positif”. Apabila tidak lebih besar 
maka tampilkan “Angka adalah bilangan negatif”.
Buatlah gambar flowchart dan kode python untuk program diatas!

'''

angka=int(input("Masukkan Angka anda : "))
if angka>0:
    print("Angka adalah bilangan positif")
elif angka==0:
    print("Angka adalah bilangan Netral")
else:
    print("Angka adalah bilangan Negatif")