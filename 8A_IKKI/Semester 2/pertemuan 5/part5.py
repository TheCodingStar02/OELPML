#TOPIC 6 - PYTHON LIST

'''
#tes variable
nama="yoyo"
nama="rangga"
print(nama)

#list = tempat menyimpan beberapa value dalam 1 variable

paslon=["amin","wogib","gamud"]
print(paslon)
'''

#cara penulisan deklarasi list
'''
nama_array=[jumlah_elemen]

ex :
umur=[15,16,17] -> list integer
status=[True, False] -> list boolean
nama=["prabowo","anies","ganjar"] -> list string
hobi=[] -> list kosong : untuk masukkan data
'''

'''
#cara akses Value List
#nama list =   0           1        2
#nama list =   -3          -2      -1
pemainbola=["Ronaldo", "Neymar", "Arhan"]
print(pemainbola[0])        #output positive = Ronaldo
print(pemainbola[-3])       #output negative = Arhan

#Neymar adalah pemain terbaik di dunia
print(pemainbola[-2], "adalah pemain terbaik didunia")
print(f"{pemainbola[1]} dan {pemainbola[0]} adalah pemain langganan bpjs")

#Cara akses Value Nested List

anime=["One Piece", "AOT", "JJK", ["Naruto", "Boruto", "Saruto"], "Bleach"]

#menghitung jumlah list di anime
print(len(anime)) #len = menghitung jumlah data 

#menghitung jumlah list di dalam list
print(len(anime[3])) 
#   list luar,list dalam
print(anime[3][1])


#ganti Value
kpop=["Black Pink", "NCT", "New-Jeans", "BigBang", "GG"]
kpop[0]="Twice"
print(kpop)
'''


'''
Pilih 1 group band atau club olahraga kesukaan kalian, Contoh:
MemberBTS = [“Jin”, ”Suga”, ”J-Hope”, ”RM”, ”Jimin”, ”V”, ”Jungkook”]
PosisiBTS = [“Vocal”, ”Rapper”, ”Rapper”, ” Rapper”, ” Vocal”, ”Vocal”, ”Vocal”]
Tampilkan hasil output menjadi seperti dibawah ini,
	“Member BTS bernama Jin memiliki posisi sebagai Vocal”
Buatlah kode python untuk program diatas!
'''


#jawaban
member_BTS = ["Jin", "Suga", "J-Hope", "RM", "Jimin", "V", "Jungkook"]
posisi_BTS = ["Vocal", "Rapper", "Rapper", "Rapper", "Vocal", "Vocal", "Vocal"]

for loop in range(len(member_BTS)):
    print(f"Member BTS bernama {member_BTS[loop]} memiliki posisi sebagai {posisi_BTS[loop]}")
