pajak = 10
diskon = 15

barang = ["caffe americano", "caramel macchiato", "asian dolce latte", "caramel latte", "vanilla latte", "caffe latte", "capuccino", "coffe mocha"]
harga = [37000, 59000, 55000, 52000, 52000, 48000, 48000, 55000]

print('Selamat datang di Alfan Caffe')
print('=' *40)
print("Berikut Adalah Menu Dan Harganya:")
for i in range(len(barang)):
    print(f"{i+1}. {barang[i]} - Rp{harga[i]}")
print('=' *40)


while True:
    try:
        pilihan = int(input("Masukkan nomor kopi yang ingin dibeli (0 untuk keluar): "))
        if pilihan < 0 or pilihan > len(barang):
            raise ValueError
        break
    except ValueError:
        print("Pilihan anda tidak ada, silahkan pilih yang lain", len(barang), "atau 0 untuk keluar.")

if pilihan == 0:
    print("Terima kasih telah berkunjung di alfan caffe, datang lagi ya")
else:
    jumlah = int(input("Masukkan jumlah minuman yang ingin dibeli: "))

    harga_awal = jumlah * harga[pilihan-1]

    pajak_tambahan = harga_awal * pajak / 100

    harga_sebelum_diskon = harga_awal + pajak_tambahan

    if harga_sebelum_diskon > 350000:
        potongan_diskon = harga_awal * diskon / 100
        harga_setelah_diskon = harga_awal - potongan_diskon
    else:
        potongan_diskon = 0
        harga_setelah_diskon = harga_awal

    total_harga = harga_awal + pajak_tambahan + harga_setelah_diskon

    print(f"Harga awal: Rp{harga_awal}")
    print(f"Diskon ({diskon}%): Rp{potongan_diskon}")
    print(f"Pajak ({pajak}%): Rp{pajak_tambahan}")
    print(f"Total harga: Rp{total_harga}")
