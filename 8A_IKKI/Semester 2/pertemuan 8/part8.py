'''
#index      0       1
siswa=["brandon","hannah"]
print(siswa)
for count in range(2):
    print(siswa[count])

#INDEX  0       1       2       3       4       5
info=["Nama","Umur","Gender","Tinggi","OSIS","Eskul"]
dataBrandon=["Brandon",14,"Pria",158,False,"Dance"]
dataJosh=["Josh",14,"Pria",160,False,"Futsal"]
dataJagad=["Jagad",13,"Pria",158,True,"Gitar"]
#INDEX          0           1       2
listsiswa=[dataBrandon,dataJosh,dataJagad]
for siswa in range(0,3):
    for count in range(0,6): #0-5
        print(info[count]," : ",listsiswa[siswa][count])
    print("----------------")

merkhape=["samsung","oppo"]
#APPEND (Menambahkan 1 data ke dalam list)
merkhape.append("vivo")
print(merkhape)

merkmobil=["BMW","Toyota"]
mobil=input("Masukan merk mobil: ")
merkmobil.append(mobil)
print(merkmobil)

#EXTEND (menggabungkan 2 buah list)
mobilkorea=["Hyundai","KIA"]
merkmobil.extend(mobilkorea)
print(merkmobil)

#INSERT (Menyelipkan data ke dalam list)
# namalist.namametode(index,data)
merkmobil.insert(10,"Aston Martin")
print(merkmobil)

nama=["brandon",'josh',"anto","michelle","yera"]
eskul=["futsal","futsal","basket","dance","basket"]
#COUNT (Menghitung jumlah data yang diminta)
print("Siswa 8-A yang eskul basket sejumlah: ",eskul.count("basket"))
print("Siswa 8-A yang eskul futsal sejumlah: ",eskul.count("futsal"))
print("Siswa 8-A yang eskul dance sejumlah: ",eskul.count("dance"))

#SORT (Mengurutkan data)
#A-Z, kecil-besar
nama.sort()
print("A-Z",nama)
#Z-A, besar-kecil
nama.sort(reverse=True)
print("Z-A",nama)

#index  0         1      2       3          4
nama=["brandon",'josh',"anto","michelle","yera"]
nama.reverse()
print(nama)

nama=["anto","michelle","josh"]
hobi=["tidur","dance","futsal"]
inputnama=input("Masukan nama siswa: ")
index=nama.index(inputnama)
print("Nama",inputnama,"ada di index ke",index)
print("Hobi",inputnama,"=",hobi[index])

#Metode menghapus data menggunakan remove
nama.remove("josh")
print(nama)
#Metode menghapus data menggunakan pop (index)
hobi.pop() #isi dengan index, kosong= hapus last data
print(hobi)
'''
total=0
numberlist=[5,15,20,25]
for count in range(4):
    print(count)
    total=total+numberlist[count]
print("Total angka =",total)

'''
total=0
numberlist=[5,15,20,25]
for count in range(4):
    print(f"data ke-{count+1} adalah {numberlist[count]}")
    total=total+numberlist[count]
print(f"Total penjumlahan dari ke {len(numberlist)} angka tersebut adalah {total}")
'''



