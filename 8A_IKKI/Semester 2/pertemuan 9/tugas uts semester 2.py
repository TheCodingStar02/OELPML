
#Program While Loop 
#ListKota berisi Kota di Indonesia
'''
Terdapat sebuah program perulangan untuk menerima input kota yang hanya 
akan berhenti apabila  user memasukan kata “selesai”.  
Apabila  loop sudah berhenti, maka tampilkan value dari ListKota.
Buatlah kode python untuk program diatas!


listkota=[]

while True:
    kota=input("Masukkan Nama Kota yang kalian kunjungi : ")
    if kota.lower() == "selesai":
        break
    listkota.append(kota.capitalize())
print("List Kota yang dimasukkan :")
for kota in listkota:
    print(kota)
'''

#Program While Loop
#Listnegara yang akan kamu kunjungi
'''
Terdapat sebuah program perulangan untuk menerima input negara 
yang akan berhenti apabila  user memasukan negara sebanyak 3 kali.  
Apabila  user telah mengisi 3 negara tersebut, maka tampilkan value dari Listnegara.
Buatlah kode python untuk program diatas!

Hint : menggunakan len untuk list negara
'''

listnegara=[]

while len(listnegara) < 3:
    negara=input("Masukkan nama negara : ")
    listnegara.append(negara)
print("list negara yang kamu pilih : ")
for negara in listnegara:
    print(negara)
#vrycie wuz here
#vrycie : 0 - 1
#vrycie : hello, good evening


#Tugas Mandiri:
#ListMember berisi Nama Member
'''
Terdapat sebuah program perulangan untuk menerima input nama yang hanya 
akan berhenti apabila  user memasukan kata “stop”.  
User dapat melakukan input  sebanyak mungkin ke dalam list bernama ListMember. 
Apabila  loop sudah berhenti, maka buat ListMember menjadi berurut sesuai A-Z. 
Tampilkan value akhir dari ListMember.
Buatlah kode python untuk program diatas!
'''

'''
example results :
Masukkan nama : Yoyo
Masukkan nama : Valenci
Masukkan nama : Claudia
Masukkan nama : stop
List nama member yang diurutkan:
Claudia
Gideon
Valen
Yoyo
'''

