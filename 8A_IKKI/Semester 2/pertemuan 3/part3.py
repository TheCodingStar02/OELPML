#1-5
for i in range(1,5):
    print(i)


'''
Terdapat sebuah perulangan for yang akan mengulang 5kali. 
Deklarasi variabel Total dan buatlah input variabel 
untuk menerima angka yang diberikan user. 
Masukan variabel tersebut kedalam variabel Total 
untuk menghitung total angka yang dimasukan dalam 
setiap loop. Program akan berhenti apabila user sudah 
memasukan angka sebanyak 5 kali. 

Program akan diakhiri dengan menampilkan value dari 
variabel Total.
Buatlah kode python untuk program diatas!
'''
total=0


for loop in range(5):
    angka=int(input("Masukkan angka = "))
    total+=angka
print(total)
print(f"hasil dari penjumlahan angka diatas adalah {total}")



