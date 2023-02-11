#  if
jumlah_penumpang = 3

if jumlah_penumpang > 10:
    print("Mobil berjalan")

if jumlah_penumpang < 10:
    print("Menunggu penumpang lain")

print("Kondisi pertama: > 10", jumlah_penumpang>10)
print("Kondisi pertama: < 10", jumlah_penumpang<10)

# if else
# nilai = 50
nilai = int(input("Masukkan nilai anda: "))
if nilai > 75:
    print("Anda lulus!")
else:
    print("Anda tidak lulus!")

# elif -> else if
# elif = pengecekan menggunakan if lagi
if nilai == 100:
    print("Predikat A")
elif nilai > 75:
    print("Predikat B")
else:
    print("Predikat C")