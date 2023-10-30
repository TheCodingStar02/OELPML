nama=input("Nama ? ")
nilai=int(input("Nilai ? "))
if nilai>84 and nilai<101:
    grade="Mendapat Predikat A"
elif nilai>69 and nilai<85:
    grade= "MendapatPredikat B"
elif nilai>54 and nilai<70:
    grade="Mendapat Predikat C"
elif nilai>53 and nilai<1:
    grade="Mendapat Predikat D"
else:
    grade="eror"
print("Siswa", nama, "dengan nilai", nilai, grade)