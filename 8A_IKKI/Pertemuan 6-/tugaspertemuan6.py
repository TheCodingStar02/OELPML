'''
Terdapat sebuah program untuk menentukan apakah siswa lulus atau gagal 
sebuah ujian dengan KKM 70. Buatlah input Nama dan Nilai dari siswa tersebut. 
Apabila nilai siswa lebih besar sama dengan 70 maka tampilkan “Selamat “,Nama,” lulus ujian”. 
Apabila tidak lebih besar maka tampilkan “Maaf  “,Nama,” belum lulus ujian”.
Buatlah gambar flowchart dan kode python untuk program diatas!


nama=input("Masukkan nama siswa : ")
nilai=int(input("Massukkan nilai siswa : "))
if nilai>=70:
    print("Selamat",nama,"lulus ujian")
else:
    print("Maaf",nama,"belum lulus ujian")
'''


'''
Terdapat sebuah program untuk membandingkan tinggi badan kita dengan 
oran lain. Buatlah 2 input (Nama kita dan Dia).
Apabila tinggi Kita lebih besar dari Dia maka tampilkan 
“tinggi kita lebih dari dia”.
Apabila tinggi Dia lebih besar dari Kita maka tampilkan 
"tinggi dia lebih dari kita“.

Buatlah gambar flowchart dan kode python untuk program diatas!

'''

me = int(input("Masukkan tinggi anda : "))
you = int(input("Masukkan tinggi dia : "))

if me > you :
    print("tinggi anda lebih dari dia")
elif you == me :
    print("tinggi kita sama")
else:
    print("tinggi dia lebih tinggi dari anda")