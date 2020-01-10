import math
import random

# Program Sederhana ujian matematika
# Dibuat untuk bahan tes diri sendiri

print("Ujian Matematika 10 Soal")
print("========================")

def ujian():
    jumlah = 0
    nilai = 0
    print("Jawablah semua soal dibawah ini")
    while jumlah <= 10:
        angka1 = random.randint(0,100)
        angka2 = random.randint(1,50)
        hasil = angka1+angka2

        print"Berapa jumlah dari",angka1,"+",angka2,"= ?"
        jawab = input("Jawabanmu ==>")
        if (jawab == hasil):
            print("Jawabanmu benar !!!")
            nilai += 1
        else:
            print("Jawabanmu salah :(( ")
        jumlah += 1
    print"Selamat kamu sudah menyelesaikan ujian ini dengan nilai",nilai
    print"============================================================"
    print''

pilih = 0
while pilih != 2:
    print("1. Mulai")
    print("2. Exit")
    pilih = input("===>")
    if(pilih == 1):
        ujian()