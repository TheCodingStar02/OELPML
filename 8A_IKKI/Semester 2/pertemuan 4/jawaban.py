for i in range(3):
    input_password = input("Masukkan password: ")

    # Validasi password
    if input_password == "password123":
        print("Device unlocked.")
        break
    else:
        print("Password salah.")
else:
    print("Password salah sebanyak 3x. Device terblokir.")



'''
SOAL

Tugas Mandiri:
Menghitung Total dari 5 angka

Terdapat sebuah perulangan for yang akan mengulang 5 kali. 
Deklarasi variabel Total dan buatlah input variabel untuk menerima angka
yang diberikan user. Masukan variabel tersebut kedalam variabel Total 
untuk menghitung total angka yang dimasukan dalam setiap loop. 
Program akan berhenti apabila user sudah memasukan angka sebanyak 5 kali. 
Program akan diakhiri dengan menampilkan value dari variabel Total.
Buatlah kode python untuk program diatas!
'''

'''
total=0
jumlah=int(input("Berapa jumlah angka? "))

for count in range(1,jumlah+1): #1 2 3 4 5
    angka=int(input(f"Masukkan angka ke-{count}: "))
    total+=angka
print("Total dari",jumlah,"angka =",total,".")
print(f"Total dari {jumlah} angka = {total}.")
'''

Total = 0
#     insiaisi awal,loop+1 = [Masukkan angka ke-1 : xx]
for loop in range(1,5+1):
    angka = int(input(f"Masukkan angka ke-{loop}: "))
    Total += angka

print("Total dari 5 angka adalah:", Total)

