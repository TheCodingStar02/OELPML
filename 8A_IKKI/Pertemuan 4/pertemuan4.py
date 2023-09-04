'''
Buatlah sebuah program untuk menghitung rata-rata harga dari 3 barang belanja.
1. Program dimulai dengan meminta 1 input untuk menyimpan nama pelanggan
2. Buat 3 input variabel untuk harga pertama, harga kedua dan harga ketiga.
3. Deklarasi Variable Total lalu masukan rumus menghitung total harga.
4. Deklarasi Variabel Average lalu masukan rumus menghitung rata-rata
5. Tampilkan Variabel nama digabungkan dengan variabel Average menjadi sebuah kalimat. 
Contoh: “Rata-rata harga barang Joni sebesar Rp 135000.”
'''
'''
nama=input("Nama Pelanggan? ")
harga1=int(input("Masukkan Harga pertama : "))
harga2=int(input("Masukkan Harga kedua : "))
harga3=int(input("Masukkan Harga ketiga : "))
total=harga1+harga2+harga3
average=total/3
print("Rata-rata harga barang",nama,"sebesar Rp",int(average))
print("Rata-rata harga barang {0} sebesar Rp {1} totalnya {2}".format(nama,average,total))
'''

#Tugas Mandiri 2:Rata-rata nilai
'''
Buatlah sebuah program untuk menghitung rata-rata dari 2 nilai.
1. Program dimulai dengan meminta 1 input untuk menyimpan nama siswa
2. Buat 2 input variabel untuk nilai pertama dan nilai kedua.
3. Deklarasi Variable Total lalu masukan rumus menghitung total nilai.
4. Deklarasi Variabel Average lalu masukan rumus menghitung rata-rata
5. Tampilkan Variabel nama digabungkan dengan variabel Average menjadi sebuah kalimat. 
Contoh: “Nilai rata-rata Andi sebesar 86.”
'''
#jawaban Tugas Mandiri 2

nama_siswa=input("Nama Siswa : ")
nilai_1=input("Masukkan Nilai 1 : ")
nilai_2=input("Masukkan Nilai 2 : ")

total_nilai=int(nilai_1)+int(nilai_2)
rata2_nilai=float(total_nilai)/2
print("Nilai rata-rata {0} sebesar {1}.".format(nama_siswa,rata2_nilai))
print("Nilai rata-rata",nama_siswa,"sebesar",rata2_nilai,".")
