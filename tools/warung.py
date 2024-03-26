import main
from sevices import db

def add():
    kode_barang = input("Kode barang : ")
    nama_barang = input("Nama barang : ")
    harga_barang = int(input("Harga barang : "))
    stok_barang = int(input("Stok barang : "))

    db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)
    
def chek():
    items = db.fetch_item()
    print("\nList Barang")
    print("==========================")
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        print(f'''kode - {kode_barang}
{nama_barang} | Rp. {harga_barang}
stok : {stok_barang}''')
        print("--------------------------")

def start():
    print("\nWARUNG FLYPY")
    while True:
        menu = int(input("\nMenu:\n\n1. Tambah Barang\n2. Check Barang\n3. Kembali\n\nSilahkan Pilih : "))

        if menu == 1:
            add()
        elif menu == 2:
            chek()
        elif menu == 3:
            main.menu()
        else:
            break

if __name__ == "__main__":
    start()