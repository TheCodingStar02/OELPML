#PROGRAM TEBAK PASSWORD
'''
Terdapat sebuah program perulangan untuk 
menebak password “RAHASIA”. 
Buatlah input yang diperlukan, 
masukan kondisi while. 
Apabila tebakan salah maka tampilkan 
pesan “Salah. Coba lagi.” 
Program hanya akan berhenti apabila user 
berhasil menebak password rahasia.
'''
#lower = kecil semua
#upper = besar semua
#capitalize = Huruf depan besar

key="larutan"
password=input("Password ? ").lower()
while password != key:
    print("Password bukan", password)
    password=input("Ulangi Password ? ").lower()
print("Selesai")




