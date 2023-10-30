'''
Buat sebuah program untuk menampilkan minuman berdasarkan input angka.
1. Menampilkan kalimat (Selamat datang di kedai ….) beserta list minuman
2. Membuat input pilih minuman

Apabila input angka adalah 1 maka tampilkan “Kopi”, 
Apabila input angka adalah 2 maka tampilkan “Teh”,
Apabila input angka adalah 3 maka tampilkan “Susu”,
Diluar itu tampilkan “Minuman menu tidak tersedia”
Silahkan tunggu, pesanan segera dibuat :)


print("Selamat datang di kedai Uncle Mutu \n**LIST MENU**\n1. Kopi\n2. Teh\n3. Susu")
menu=int(input("Pilih angka menu yang anda mau : "))
if menu==1:
    print("Anda pesan kopi")
elif menu==2:
    print("Anda pesan Teh")
elif menu==3:
    print("Anda pesan Susu")
else:
    print("Maaf menu tidak tersedia")
print("Silahkan tunggu, pesanan segera dibuat :)")



Terdapat sebuah program untuk menentukan generasi seseorang. 
Generasi X (1965-1976)
Generasi Milenial (1977-1994)
Generasi Z (1995-2010)
Generasi Alpha (2011-2025)
User diminta untuk melakukan input nama dan tahun kelahiran, kemudian menampilkan nama, tahun lahir dan generasinya.
Contoh output : “Jojo lahir pada tahun 2000 tergolong generasi Z.”
'''

nama=input("Masukkan Nama anda : ")
tahunlahir=int(input("Masukkan tahun lahir anda : "))
if tahunlahir>=1965 and tahunlahir<=1976:
    gen="Tergolong Generasi X"
elif tahunlahir>=1977 and tahunlahir<=1994:
    gen="Tergolong Generasi Milenial"
elif tahunlahir>=1995 and tahunlahir<=2010:
    gen="Tergolong Generasi Z"
elif tahunlahir>=2011 and tahunlahir<=2025:
    gen="Tergolong Generasi Alpha"
else:
    gen="Generasi belum ada"
print(nama, "lahir pada tahun", tahunlahir, gen)
print("{0} lahir pada tahun {1} {2}".format(nama,tahunlahir,gen))







