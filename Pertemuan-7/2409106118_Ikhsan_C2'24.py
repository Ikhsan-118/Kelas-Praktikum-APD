# def mhs():
#     print("Hello")

# mhs()

# Membuat Fungsi
# def salam():
#     print ("Selamat Pagi, FT Muda")
# def kali():
#     x = 6*4
#     print(x)
# Pemanggilan Fungsi
# salam()
# kali()

# F(x) = x+2
#  F(22) = (22) + 2
# = 24

# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print ("luas_persegi_panjang:", luas)

# luas_persegi_panjang(6,2)

# def mhs(nama, nim, *arr):
#     print(nama)
#     print(nim)
#     print(arr)
    
# mhs()

# import os
# data_mahasiswa =[
#     {
#         "Nama" : "Andi",
#         "Nim" : "123"
#     },
#     {
#         "Nama" : "Budi",
#         "Nim" : "124"
#     },
#     {
#         "Nama" : "Ucup",
#         "Nim" : "125"
#     }
# ]

# def lihat_data():
#     print("===Lihat Data===")
#     for i in range(len(data_mahasiswa)):
#             print(f"data ke {i+1}")
#             print(f"Nama : {data_mahasiswa[i]['Nama']}")
#             print(f"Nim : {data_mahasiswa[i]['Nim']}")
#             print("="*10)

# def tambah_data():
#     print("== Tambah Data ==")
#     print("=" * 10)
#     input_nama = input("Nama\t: ")
#     input_nim = input("Nim\t: ")
#     data_mahasiswa.append({
#         "Nama" : input_nama,
#         "Nim" : input_nim
#     })
#     print(f"{input_nama} dengan NIM {input_nim} telah ditambahkan")

# def edit_data():
#     print("== Ubah Data ==")
#     for i in range(len(data_mahasiswa)):
#         print(f"data ke {i+1}")
#         print(f"Nama : {data_mahasiswa[i]['Nama']}")
#         print(f"Nim : {data_mahasiswa[i]['Nim']}")
#         print("="*10)
#     if index > len(data_mahasiswa) or index < 0:
#         data_mahasiswa[index-1]["Nama"] = nama_baru
#         data_mahasiswa[index-1]["Nim"] = nim_baru
#         print("data berhasil diubah")


# os.system('cls || clear')
# while True:
#     print("""
#     Menu
# Lihat Data  >> 1
# Tambah Data >> 2
# Edit Data   >> 3
# Hapus Data  >> 4
# Keluar      >> 5
# """)
    
#     pilih = input("Masukan Pilihan menu >> ")
#     os.system('cls || clear')
#     match(pilih):
#         case "1":
#             input("Enter.....")
#             os.system('cls || clear')
#         case "2":
#             input("Enter....")
#             os.system('cls || clear')
#         case "3":
#                 index= int(input("masukkan index yang mau diedit : "))
#                 print("Index tidak ditemukan")
#                 input("Enter.....")
#                 os.system('cls || clear')
#                 nama_baru = input("masukkan nama anda :")
#                 nim_baru = input("masukkan nim anda :")
#                 input("Enter.....")
#                 os.system('cls || clear')
#         case "4":
#             print("== Hapus Data ==")
#             for i in range(len(data_mahasiswa)):
#                 print(f"data ke {i+1}")
#                 print(f"Nama : {data_mahasiswa[i]['Nama']}")
#                 print(f"Nim : {data_mahasiswa[i]['Nim']}")
#                 print("="*10)
#             index = int(input("masukkan index yang ingin dihapus: "))
#             if index > len(data_mahasiswa) or index < 0:
#                 print("Index tidak ditemukan")
#                 input("Enter.....")
#                 os.system('cls || clear')
#             else:
#                 del_data = data_mahasiswa.pop(index-1)
#                 print(f"{del_data['Nama']} dengan NIM {del_data['Nim']} telah dihapus")
#                 input("Enter......")
#                 os.system('cls || clear')
#         case "5":
#             print("Bye bye")
#             exit()
#         case _:
#             print(f"Menu {pilih} tidak tersedia")
#             input("Enter.....")
#             os.system('cls || clear')