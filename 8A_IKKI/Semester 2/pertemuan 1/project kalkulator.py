'''
buatlah sebuah program kalkulator sederhana dengan 4 operasi matematika
1. penjumlahan
2. pengurangan
3. perkalian
4. pembagian

user dapat memilih salah satu dari operasi matematika diatas yang akan di proses
dengan memasukkan 2 bilangan saja menggunakan metode percabangan (if elif else)


#output program :
    
=========================
Operasi Matematika
  1. Jumlah      [+]
  2. Kurang      [-]
  3. Kali        [*]
  4. Bagi        [/]
=========================
Pilih operasi (1/2/3/4): 1
Masukkan angka pertama: 10
Masukkan angka kedua: 5
=========================
Hasil operasi dari 10 + 5 = 15
'''

print('=' * 25)
print('Operasi Matematika')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Kali \t [*]')
print('  4. Bagi \t [/]')
print('=' * 25)

operasi = input('Pilih operasi (1/2/3/4): ')
angka_pertama = int(input('Masukkan angka pertama: '))
angka_kedua = int(input('Masukkan angka kedua: '))

if operasi == '1':
  hasil = angka_pertama + angka_kedua
  print(f'{hasil}')
elif operasi == '2':
  hasil = angka_pertama - angka_kedua
  print(f'{hasil}')
elif operasi == '3':
  hasil = angka_pertama * angka_kedua
  print(f'{hasil}')
elif operasi == '4':
  hasil = angka_pertama / angka_kedua
  print(f'{hasil}')
else:
  print('Eror')
