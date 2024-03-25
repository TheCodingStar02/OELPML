#LIST PART 3

#Built-in Function
#digunakana untuk memanipulasi dan memproses data list di python

angka = [90, 7, 34, 10, 23, 15, 24]

#menghitung banyak data (len)
print(len(angka)) #tanpa informasi
print(f"byk dt : {len(angka)}") #ada informasi

#mencari data tertinggi (max)
print(f"dt tertinggi : {max(angka)}")

#mencari data terendah (min)
print(f"dt terendah : {min(angka)}")

#menghitung jumlah total keseluruhan (sum)
print(f"jumlah total data : {sum(angka)}")

#menghitung rata-rata (sum)/(len)
print(sum(angka)/len(angka))
print(f"ini avg {sum(angka)/len(angka)}")


#operator pada list

#1 - SLicing [x:y] => memilih data dari sebuah set data
#logic [start:stop] => stop tidak tampil dalam slicing
#set data = kumpulan data di dalam list
#       0           1        2      3
#        -4        -3      -2       -1
data=["anjing", "kucing", "babi", "burung"]
print(data[0:2]) #output anjing - kucing
print(data[0:7])
print(data[-4:-1])

#2 membership
#Membership  = menguji apakah suatu 
# urutan disajikan dalam suatu objek

#in = apakah data berada pada list tsb
#not in = apakah data tidak ada pada list tersebut

#Hasil dari operator membership ialah Boolean (True or False).

takjil=["2", "lontong", "bubul_cumcum", "kolak", 2]
print(2 in takjil)
print("pizza" in takjil)
print("kolak" not in takjil)