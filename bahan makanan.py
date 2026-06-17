from datetime import datetime

#function

def cekexp(array_makanan):
    
    if len(array_makanan) == 0:
        print("Data kosong!")
        return

    sekarang = datetime.now().date()

    print("\n--- CEK BARANG EXPIRED ---")

    for data in array_makanan:

        str_tgl = data["tgl"]

        
        tgl_exp = datetime.strptime(str_tgl, "%d/%m/%Y").date()

        
        sisa_hari = (tgl_exp - sekarang).days

        if sisa_hari < 0:
            print(f" {data['makanan']} sudah EXPIRED!")
            print(f"   Stock : {data['stock']}")
            print(f"   Exp   : {str_tgl}")

        elif sisa_hari <= 7:
            print(f" {data['makanan']} mendekati expired!")
            print(f"   Stock : {data['stock']}")
            print(f"   Exp   : {str_tgl}")
            print(f"   Sisa  : {sisa_hari} hari lagi")

        else:
            print(f" {data['makanan']} masih aman")
            print(f"   Exp : {str_tgl}")
            print(f"   Sisa: {sisa_hari} hari lagi")

        print("-" * 35)



def tambahdata(array_makanan):
    while True:
        makanan = input("Masukkan Data Makanan: ")
        stock = int(input("Masukkan jumlah stock makanan: "))
        tgl = input("Masukkan tanggal kadaluarsannya (dd/mm/yyyy): ")
    
    
        array_makanan.append({
        
        "makanan":makanan,
        "tgl": tgl,
        "stock": stock
        
        })

        cek = input("Apakah ingin lanjut memasukkan data? (Y/N): ")
        if cek.lower() == "n":
            print("Data telah terupdate")
            break
        
        

def searchmakansquantial(array_makanan):
    ketemu = False   
    search = input("Masukkan makanan yang ingin dicari: ")
    for item in array_makanan:
            
        if item["makanan"].lower() == search.lower():
            print(f"Tersedia {item}")
            ketemu = True
                
    if not ketemu:
            print("Item tidak tersedia")
            
def searchmakanbinary(array_makanan):
    search = input("Masukkan Makanan yang ingin dicari: ").lower()
    
    array_makanan.sort(key=lambda x: x["makanan"].lower())
    kiri = 0
    kanan = len(array_makanan) - 1
    ketemu = False
    
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        nama_tengah = array_makanan[tengah]["makanan"].lower()
        
        if nama_tengah == search:
            print(f"Tersedia {search}")
            ketemu = True
            break
        elif nama_tengah < search:
            kiri = tengah + 1
            
        else:
            kanan = tengah - 1
            
            
    if not ketemu:
        print("Item tidak tersedia!")
        return
        
        

def hapusdata(array_makanan):
    data_lama(array_makanan)
    target = input("Masukkan Nama item yang ingin dihapus: ").lower()
    ketemu = False
    
    for i in range(len(array_makanan)):
        if array_makanan[i]["makanan"].lower() == target:
            
            data_delete = array_makanan.pop(i)
            ketemu = True
            print(f"item {data_delete["makanan"]} berhasil di delete")
            break
    if not ketemu:
        print("Item tidak ditemukan")
        
        

def mengubahdata(array_makanan):
    
    ketemu = False
    
    if len(array_makanan) == 0:
        print("Data kosong")
        return
    
    target = input("Masukkan nama data yang ingin diubah: ").lower()
    if target == "1":
        return
    else:
        
        data_lama(array_makanan)
        for i in range(len(array_makanan)):
            if array_makanan[i]["makanan"].lower() == target:        
                print("Jika tidak ingin mengubah data tersebut kosongkan dan langsung tekan Enter")
            
                nama_baru = input("Masukkan Nama baru: ")
                Stock_baru = input("Masukkan Stock baru: ")
                exp_baru = input("Masukkan tanggal kadaluarsa baru (dd/mm/yyyy): ")
            
                if nama_baru != "":
                    array_makanan[i]["makanan"] = nama_baru
                if Stock_baru != "":
                    array_makanan[i]["stock"] = int(Stock_baru)
                if exp_baru != "":
                    array_makanan[i]["tgl"] = exp_baru
                    
                print("Data berhasil diubah!")
                ketemu = True
                break
            
        if not ketemu:
            print(f"Data {target} tidak tersedia!") 



def sortdata(array_makanan):
    if len(array_makanan) == 0:
        print("Data Kosong")
        return
    
    menusort()
    targetsort = int(input("Pilih Menu (Angka): "))
    
    menuUD()
    targetad = int(input("Pilih Menu (Angka): "))
    
    if targetsort == 1: 
        if targetad == 1:
            array_makanan.sort(key=lambda x: x["makanan"].lower())
            print("\nData berhasil di sort")
        elif targetad == 2:
            array_makanan.sort(key=lambda x: x["makanan"].lower(), reverse = True)
            print("\nData berhasil di sort")
        else:
            print("\nMenu tidak tersedia")
            return
                
    elif targetsort == 2:
        if targetad == 1:
            array_makanan.sort(key=lambda x: x["stock"])
            print("\nData berhasil di sort")
        elif targetad == 2:
            array_makanan.sort(key=lambda x: x["stock"], reverse = True)
            print("\nData berhasil di sort")
        else:
            print("\nMenu tidak tersedia")
            return
    
    elif targetsort == 3:
        if targetad == 1:
            array_makanan.sort(key=lambda x: datetime.strptime(x["tgl"], "%d/%m/%Y"))
            print("\nData berhasil di sort")
        elif targetad == 2:
            array_makanan.sort(key=lambda x: datetime.strptime(x["tgl"], "%d/%m/%Y"), reverse = True)
            print("\nData berhasil di sort")  
        else:
            print("\nMenu tidak tersedia")
            return                  
            
            
            
    
    


def data_lama(array_makanan):
    
    for i, item in enumerate(array_makanan, start = 1):
        print(f"{i}. {item["makanan"]} stock: {item["stock"]} exp: {item["tgl"]}")
        


# Void Function
def menu():
    print("\n╔══════════════════════════════════════╗")
    print("║          🏠 DATABASE MENU              ║")
    print("╠══════════════════╦═════════════════════╣")
    print("║ 1️⃣ Tambah Data  ║ 4️⃣ Search Data      ║")
    print("║ 2️⃣ Ubah Data    ║ 5️⃣ Sort Data        ║")
    print("║ 3️⃣ Hapus Data   ║ 6️⃣ Data Lama        ║")
    print("╠══════════════════╩═════════════════════╣")
    print("║ 7️⃣ Cek Expired ║ 8️⃣ Exit             ║")
    print("╚════════════════════════════════════════╝")


def menusort():
    print("\n---Menu Sort---")
    print("\n1. Nama" "\n2. Stock" "\n3. Tanggal Expired")

def menuUD():
    print("\n1. Ascending (A-Z)" "\n2. Descending (Z-A)")
        
        
def menus():
    print("\n---Metode Search---\n" "\n1. Sequantial \n2. Binary")    



# main

data_makanan = []

while True:
    menu()
    a = (input("Pilih menu: "))
    if a == "1":
        tambahdata(data_makanan)
        continue
    
    elif a == "2":
        print("\n---Menu Mengubah---" "\n*ketik 1 untuk cancle")
        data_lama(data_makanan)
        mengubahdata(data_makanan)
        continue
    
    elif a =="3":
        hapusdata(data_makanan)
        continue
    
    elif a == "4":
        menus()
        option = int(input("\nPilih metode search: "))
        if option == 1:
            hasil1 = searchmakansquantial(data_makanan)
            continue
        elif option == 2:
            hasil2 = searchmakanbinary(data_makanan)
            continue
        
        cek = input("Apakah ingin lanjut mencari data? (Y/N): ")
        if cek.lower() == "n":
            break
    
    elif a == "5":
        sortdata(data_makanan)
        continue
    
    elif a == "6":
        while True:
            data_lama(data_makanan)
            cek = input("Apakah ingin kembali ke menu utama (Y/N): ")
            if cek.lower() == "y":
                break
            
        
    elif a == "7":
        cekexp(data_makanan)
        continue
    
    elif a == "8":
        print("Program berhenti!")
        break