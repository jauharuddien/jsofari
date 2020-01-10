print ("List Program JSofari")

print ("1. Hitung luas persegi")
print ("2. Hitung luas kubus")
print ("3. Kasir sederhana")
print ("4. Exit")

pilih = input("Masukan pilihan anda : ")

if pilih == 1:
    print ("Program hitung luas persegi (satuan cm)")

    panjang = input("Masukan panjang : ")
    lebar = input("Masukan lebar : ")

    jumlah = (panjang*lebar)

    print ("Luasnya adalah : "),jumlah,("cm")

if pilih == 2:
    print ("Program hitung luas kubus (satuan cm)")

    panjang = input("Masukan panjang : ")
    lebar = input("Masukan lebar : ")
    tinggi = input("Masukan tinggi : ")

    jumlah = (panjang*lebar*tinggi)

    print ("Luas kubus tersebut adalah : "),jumlah,("cm")

if pilih == 3:
    print ("Program kasir sederhana")

    barang = raw_input("Masukan nama barang : ")
    harga = input("Masukan harga barang : ")
    satuan = input("Masukan jumlah barang : ")
    uang = input("Jumlah uang yang dibayar : ")

    jumlah = (harga*satuan)
    total = (uang-jumlah)

    print ("Pembelian "),barang,(" Telah sukses diproses")
    print ("Jumlah kembaliannya adalah Rp."),total

if pilih == 4:
    quit()