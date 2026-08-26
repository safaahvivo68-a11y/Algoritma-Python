nama_hp = input("masukan nama hp: ")
harga_hp = int(input("Maukan Harga hp: "))
ram = int(input("Masukan RAM (GB): "))
storage = int(input("Masukan storage (GB): "))
Baterai = int(input("masukan kapasitas baterai (MAH)" ))
stok = True

# menghitung harga setelah diskon
diskon = int(input("Masukan diskon (Rp): "))
harga_akhir = harga_hp - diskon
print("Harga Awal", harga_hp)
print("Diskon:", diskon)
print("Harga setelah diskon:", harga_akhir)

recomended_gaming = ram >=12 and storage_512 and baterai >= 6500 and stock
print(Recomended untuk gaming?, recomended_gaming)

terjangkau = harga <= 5000000 or ram >=12
print("HP terjangkau?", Terjangkau)

flagship = ram >=12 and storage >= 512 and harga 7000000
print("HP flagship?", flagship)