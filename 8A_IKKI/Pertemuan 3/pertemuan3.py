#Soal 1 Luas Persegi Panjang
'''
Terdapat sebuah program untuk menghitung Luas Persegi Panjang.
1. Program dimulai dengan meminta 2 input variabel untuk lebar dan panjang.
2. Deklarasi Variable Luas lalu masukan rumus menghitung Luas.
3. Tampilkan hasil perhitungan Luas menjadi sebuah kalimat.
	Contoh : Luas Persegi Panjang adalah 10 cm2.

#jawaban soal 1 
l=int(input("Masukkan Lebar Persegi : "))
p=int(input("Masukkan Panjang Persegi : "))
luas=p*l
print("Luas Persegi panjang adalah",luas,"cm2.")
'''

#Soal Luas Segitiga
'''
#Menghitung luas Segitiga

alas_segitiga=int(input("Masukkan alas Segitiga: "))
tinggi_segitiga=int(input("Masukkan Tinggi Segitiga : "))

#Proses Luas Segitiga
luas_segitiga=float(alas_segitiga*tinggi_segitiga)/2
print("luas Segitiga adalah",luas_segitiga,"cm2.")
'''

#Soal Keliling Segitiga

'''
Terdapat sebuah program untuk menghitung Keliling Segitiga.
1. Program dimulai dengan meminta 3 input variabel untuk sisi A, sisi B dan sisi C segitiga.
2. Deklarasi Variable Keliling lalu masukan rumus menghitung Keliling segitiga.
3. Tampilkan hasil perhitungan Keliling Segitga.
4. Tampilkan Variabel keliling menjadi sebuah kalimat. 
	Contoh : Keliling Segitiga tersebut adalah 10 cm.
'''
#jawaban soal Keliling Segitiga

a=int(input("Masukkan Sisi A : "))
b=int(input("Masukkan Sisi B : "))
c=int(input("Masukkan Sisi C : "))
#proses hitung keliling Segitiga
keliling=a+b+c
print("Keliling segitiga tersebut adalah",keliling,"cm.")