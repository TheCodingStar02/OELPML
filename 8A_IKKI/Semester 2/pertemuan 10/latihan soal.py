'''
Terdapat sebuah program perulangan untuk 
menerima input angka sebanyak 5x dan 
masukan  kedalam ListAngka.  Buatlah for loop yang 
akan berhenti apabila sudah berhasil mengulang 5x, 
lalu tampilkan Sum dari ListAngka.
Buatlah kode python untuk program diatas!
'''
listangka=[]
for loop in range(5):
    angka=int(input(f"masukkan angka data ke-{loop+1}: "))
    listangka.append(angka)
else:
    print(f"Input selesai, Sum dari listangka adalah : {sum(listangka)}")