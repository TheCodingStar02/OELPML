#jawaban tugas 1
nama = []
umur = []

while True:
    input_nama = input("Input nama (katakan 'syudah' untuk berhenti): ")
    if input_nama.lower() == 'syudah':
        break
    else:
        input_umur = float(input("Input umur : "))
        nama.append(input_nama)
        umur.append(input_umur)

if umur:  # Periksa jika daftar umur tidak kosong
    print("Umur tertua:", max(umur))
    print("Umur termuda:", min(umur))
    print("Rata-rata umur:", sum(umur) / len(umur))
else:
    print("Tidak ada data umur yang dimasukkan.")