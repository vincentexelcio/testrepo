angka_awal = int(input("first number: "))
baris = 0
while baris == 0:        
    baris = int(input("how many row: "))
    if baris < 1:
        print('baris harus lebih dari satu')
else:        
    c = 0
    print("the sequence is: ")
    i = 0
    while i <= baris:
        hasil = angka_awal + c
        print(hasil)
        if hasil == 0:
            angka_awal = 1
        else:
            angka_awal = c
            c = hasil

        i += 1
