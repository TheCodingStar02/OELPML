#GAME TEBAK KATA
Nama="Eve"
katarahasia="sapi"
print("Hi",Nama,"! Mari bermain tebak kata!\nKata terdiri dari 4 huruf dengan tema hewan.")
print("Kalian dapat menebak huruf sebanyak 5x. Setelah itu tebak kata rahasia.")
for count in range(1,6):
    print("Tebakan ke -",count)
    huruf=input("Masukan huruf : ")
    if huruf in katarahasia:
        print("Huruf",huruf,"ADA didalam kata rahasia.")
    else:
        print("Huruf TIDAK ADA didalam kata rahasia")
jawaban=input("Berdasarkan huruf yang didapatkan, silahkan tebak kata rahasia: ")
if jawaban == katarahasia:
    print("Selamat tebakan anda benar")
else:
    print("Salah! Jawaban benar adalah",katarahasia)
