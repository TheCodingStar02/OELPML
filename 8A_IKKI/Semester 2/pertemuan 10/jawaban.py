'''
nums=[79,34,2,10,86,54,25]
print(f"ini adalah len")
print(len(nums)) #menghitung banyak data

print(f"ini adalah max")
print(max(nums)) #mencari data tertinggi

print(f"ini adalah max")
print(min(nums)) #mencari data terkecil

print(f"ini adalah sum")
print(sum(nums)) #menghitung jumlah total keseluruhan

print(f"ini adalah hasil dari sum dibagi len")
print(f"{sum(nums)} : {len(nums)} =")
print(sum(nums)/len(nums)) #menghitung rata-rata


#jawaban soal 1
ListAngka = []

for i in range(5):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    ListAngka.append(angka)
else:
    print("Input selesai. Sum dari ListAngka:", sum(ListAngka))
'''
    
#jawaban tugas 1

#Inisialisasi dua list kosong untuk menyimpan nama dan nilai siswa
nama = []
nilai = []
#Loop tak terbatas untuk meminta input nama dan nilai siswa
while True:
    input_nama = input("Masukkan nama siswa (ketik 'stop' untuk berhenti): ")
    if input_nama.lower() == 'stop': 
        break #berhenti ketika ada user input stop
    else: #selain kata stop, lanjut masukkan nilai
        #Meminta input nilai siswa dan mengubahnya menjadi float
        input_nilai = float(input("Masukkan nilai siswa: "))
        #Menambahkan nama dan nilai siswa ke dalam list masing-masing
        nama.append(input_nama) #menyimpan setdata nama ke list nama
        nilai.append(input_nilai) #menyimpan setdata nilai ke list nilai
#Memeriksa apakah ada input nilai atau tidak
if nilai: 
    # Mencari indeks nilai tertinggi dan terendah dalam list nilai
    index_max = nilai.index(max(nilai))
    index_min = nilai.index(min(nilai))
    # Menghitung rata-rata nilai menggunakan fungsi sum() dan len()
    rata_rata = sum(nilai) / len(nilai)
    
    # Menampilkan nama dan nilai siswa dengan nilai tertinggi
    print("\nSiswa dengan nilai tertinggi:")
    print("Nama:", nama[index_max])
    print("Nilai:", nilai[index_max])
    # Menampilkan nama dan nilai siswa dengan nilai terendah
    print("\nSiswa dengan nilai terendah:")
    print("Nama:", nama[index_min])
    print("Nilai:", nilai[index_min])
    # Menampilkan rata-rata nilai
    print("\nRata-rata nilai:", rata_rata)
else:
    print("Tidak ada input nilai.")# Menampilkan pesan jika tidak ada input nilai (stop)

