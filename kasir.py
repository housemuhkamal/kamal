Menu = {
    "ayam goreng":1000,
    "burger     ":2500,
    "spacechiken":2000,
    "coca cola  ":5000,
    "kopi       ":5000,
}
print("=================daftar menu=================")
for i in Menu:
    print("daftar menu : ", i,"\t harga : ", Menu[i])
print("pembelian di atas Rp100000,- mendapatkan diskon 15%")
print("====================================================")
beli = input("pilih menu : ")
jumlah = int(input("jumlah pesanan : "))
bayar = jumlah * Menu[i]

if bayar > 100000:
    diskon = bayar*15/100
    total = bayar - diskon
else:
    total = bayar

print("=================detail bayar=================")
print("menu yang di pesan        : ",beli)
print("jumlah yang di pesan      : ",jumlah)
print("total biaya               : ",bayar)
print("total yang harus di bayar : ",total)