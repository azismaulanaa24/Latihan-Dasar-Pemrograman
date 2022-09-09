print(">>>TUGAS TRUE FALSE<<<")
print(" ")

print("Deskripsi")
print("1. Jika Bilangan satu dan bilangan Dua terdapat nilai 5 Maka Hasil Akan TRUE")
print("2. Jika Jumlah Kedua Bilangan Tersebut 5 Hasil Akan TRUE")
print("3. Jika Selisih Kedua Bilangan Tersebut 5 Hasil Akan TRUE")
print("Selain kondisi yang terdapat di DESKRIPSI maka hasil akan FALSE")

print("")
n1 =input("Masukan Nilai Ke-Satu	: ")
n2 =input("Masukan Nilai Ke-Dua	: ")

n1=int(n1)
n2=int(n2)

if n1 == 5:
	print("TRUE")
elif n2 == 5:
	print("TRUE")
elif n1+n2 == 5:
	print("TRUE")
elif n1-n2 == 5:
	print ("TRUE")
elif n2-n1 == 5:
	print ("TRUE")
else:
	print("FALSE")