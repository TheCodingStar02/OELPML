'''
Terdapat sebuah program untuk membandingkan tinggi badan kita dengan 
oran lain. Buatlah 2 input (Nama kita dan Dia).
Apabila tinggi Kita lebih besar dari Dia maka tampilkan 
“tinggi kita lebih dari dia”.
Apabila tinggi Dia lebih besar dari Kita maka tampilkan 
"tinggi dia lebih dari kita“.

Buatlah gambar flowchart dan kode python untuk program diatas!

'''
saya=int(input("Masukkan tinggi saya : "))
dia=int(input("Masukkan tinggi dia : "))

if saya > dia :
    print("Tinggi saya lebih dari dia")
elif saya == dia :
    print("Tinggi kita sama")
else:
    print("Tinggi dia lebih dari saya")
