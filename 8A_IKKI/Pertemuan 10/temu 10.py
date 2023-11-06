#sample while loop
'''
i = 1
while i <= 6:
  print(i)
  i += 1
'''

#statement break
'''
i = 1
while i < 10:
  print(i)
  if (i == 8):
    break
  i += 1
'''

#continiue
b = 0
while b < 6:
  b += 1
  if b == 3:
    continue
  print(b)

#Program menghitung total 5 ANGKA

loop=1
total=0
while loop<=5:
    angka=int(input("Masukkan Angka : "))
    loop=loop+1
    total=total+angka
print(total)