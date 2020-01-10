import random
import math 

def game():
    print("Tebak angka mulai dari 1 - 100")
    def randomnumber():
        number = random.randrange(1,100)
        return number
    def userinput():
        putar = True
        while putar:
            jawab = input("Masukan angka tebakan ==> ")
            try:
                number = int(jawab)
            except ValueError:
                print("Input harus berupa angka")
            except NameError:
                print("Jawab yang benar !!!")
            else:
                return int(jawab)
                putar = False
    def main():
        tebak = True
        number = randomnumber()
        jawaban = userinput()
        tot_tebak = 0
        while tebak:
            tot_tebak += 1
            if(jawaban == number):
                print"Tebakan benar, angkanya adalah %d" % number
                print"Terjawab dalam %d tebakan" % tot_tebak
                tebak = False
            elif (jawaban < number):
                print("Angka terlalu kecil")
                jawaban = userinput()
            else:
                print("Angka terlalu besar")
                jawaban = userinput()
        print ("Terimakasih sudah bermain")
    main()

def kasir():
    print ("Program kasir sederhana")

    barang = raw_input("Masukan nama barang : ")
    harga = input("Masukan harga barang : ")
    satuan = input("Masukan jumlah barang : ")
    uang = input("Jumlah uang yang dibayar : ")

    jumlah = (harga*satuan)
    total = (uang-jumlah)

    print ("Pembelian "),barang,(" Telah sukses diproses")
    print ("Jumlah kembaliannya adalah Rp."),total

def luaskubus():
    print ("Program hitung luas kubus (satuan cm)")

    panjang = input("Masukan panjang : ")
    lebar = input("Masukan lebar : ")
    tinggi = input("Masukan tinggi : ")

    jumlah = (panjang*lebar*tinggi)

    print ("Luas kubus tersebut adalah : "),jumlah,("cm")

def luaspersegi():
    print ("Program hitung luas persegi (satuan cm)")

    panjang = input("Masukan panjang : ")
    lebar = input("Masukan lebar : ")

    jumlah = (panjang*lebar)

    print ("Luasnya adalah : "),jumlah,("cm")

def ujianmtk():
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
    ujian()

print ("List Program JSofari")

def menu():
    pilih = 0
    while pilih != 6:
        print ("1. Hitung luas persegi")
        print ("2. Hitung luas kubus")
        print ("3. Kasir sederhana")
        print ("4. Game Tebak Angka")
        print ("5. Ujian Matematika")
        print ("6. Exit")

        pilih = input("Masukan pilihan anda : ")

        if pilih == 1:
            luaspersegi()

        if pilih == 2:
            luaskubus()

        if pilih == 3:
            kasir()

        if pilih == 4:
            game()

        if pilih == 5:
            ujianmtk()

        if pilih == 6:
            quit()
menu()