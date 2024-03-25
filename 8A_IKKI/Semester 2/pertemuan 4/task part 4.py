'''
Program : Menghitung total dari jumlah angka yang ditentukan

1. Terdapat sebuah perulangan for yang akan menghitung jumlah total dari angka yang akan user masukkan. 
“Misal user masukkan 10, maka sistem akan mengeksekusi 10 angka tersebut.”

2. Deklarasi variabel Total dan buatlah input variabel untuk menerima jumlah angka yang diberikan user. 
3. Buat for loop range, dimana program akan menghitung jumlah angka yang telah dipilih user
4. Buat input variabel untuk masukkan angka yang akan di hitung
5. Proses Variabel total dengan Variabel no.4 (total+=angka)
6. Program akan diakhiri dengan menampilkan value dari variabel Total.
7. Program akan berhenti apabila angka yang ditentukan user sudah selesai di input.
Buatlah kode python untuk program diatas!
'''

total = 0

jumlah_angka = int(input("Masukkan jumlah angka yang akan dihitung: "))

for loop in range(jumlah_angka):
    angka = int(input(f"Masukkan angka ke-{loop + 1}: "))
    total += angka

print(f"Total dari angka yang dimasukkan: {total}")


# Deklarasi variabel Total dan input untuk menerima jumlah angka dari user
total = 0

# Input berapa banyak data yang akan di eksekusi
jumlah_angka = int(input("Masukkan jumlah angka yang akan dihitung: "))

# For loop untuk menghitung jumlah angka yang dimasukkan user
for loop in range(jumlah_angka):
    # Input variabel untuk memasukkan angka yang akan dihitung
    angka = int(input("Masukkan angka: "))
    # Proses penambahan angka ke total
    total += angka


# Menampilkan total dari angka yang dimasukkan user
print("Total dari angka yang dimasukkan:", total)
print(f"Total dari angka yang dimasukkan: {total}")