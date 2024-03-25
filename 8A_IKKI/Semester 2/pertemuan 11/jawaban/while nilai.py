nama = []
nilai = []

while True:
    input_nama = input("Masukkan nama siswa (ketik 'stop' untuk berhenti): ")
    if input_nama.lower() == 'stop':
        break
    else:
        input_nilai = float(input("Masukkan nilai siswa: "))
        nama.append(input_nama)
        nilai.append(input_nilai)

if nilai:
    index_max = nilai.index(max(nilai))
    index_min = nilai.index(min(nilai))
    rata_rata = sum(nilai) / len(nilai)
    
    print(f"\nSiswa dengan nilai tertinggi:")
    print("Nama:", nama[index_max])
    print("Nilai:", nilai[index_max])

    print(f"\nSiswa dengan nilai terendah:")
    print("Nama:", nama[index_min])
    print("Nilai:", nilai[index_min])

    print(f"\nRata-rata nilai:", rata_rata)
else:
    print("Tidak ada input nilai.")

