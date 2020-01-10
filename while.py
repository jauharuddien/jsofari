# Contoh perulangan while

jawab = 'ya'
hitung = 0

while (jawab == 'ya'):
    hitung += 1
    jawab = raw_input("Ulangi lagi tidak?")

print("Total perulangan :",str(hitung))