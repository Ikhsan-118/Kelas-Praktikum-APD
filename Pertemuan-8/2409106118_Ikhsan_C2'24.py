# Nama Error

# SyntaxError Terjadi ketika interpreter menemui sintaks yang tidak valid.
# print("Hello World"  # Kurang tanda kurung penutup

# IndexError Terjadi ketika kita salah memberikan index untuk mengambil data dari list
# my_list = [1, 2, 3]
# print(my_list[5])  # Indeks 5 tidak ada

# AssertionError Terjadi ketika kita ingin melakukan pengecekan
# assert 1 == 2, "Angka tidak sama!"  # Gagal karena 1 tidak sama dengan 2

# AttributeError Terjadi ketika melakukan operasi yang tidak sesuai pada suatu data
# my_string = "Hello"
# my_string.append(" World")  # String tidak memiliki metode append

# ImportError Terjadi jika module yang ingin kita import tidak ditemukan
# import non_existent_module  # Modul ini tidak ada

# KeyError Terjadi jika key pada dictionary tidak ditemukan
# my_dict = {'a': 1}
# print(my_dict['b'])  # Key 'b' tidak ada

# NameError Terjadi jika sebuah variable belum diinisialisasi
# print(my_variable)  # my_variable belum diinisialisasi

# MemoryError Terjadi jika sebuah program kehabisan memory untuk digunakan
# my_list = [1] * (10**10)  # Menggunakan terlalu banyak memori

# TypeError Terjadi jika sebuah fungsi dan operasi tidak digunakan sebagaimana mestinya
# print("Hello" + 5)  # Tidak bisa menggabungkan string dengan integer

# IndentationError Terjadi saat tab atau spasi dalam kode tidak mengikuti pola yang diharapkan.
# def my_function():
# print("Hello")  # Indentasi tidak benar

# FileNotFoundError Terjadi ketika file tidak ditemukan
# with open('non_existent_file.txt') as f:  # File ini tidak ada
#     content = f.read()

# angka = int(input("Masukkan angka: "))
# print(angka)
# #input “Hello”
# try:
#     angka = int(input("Masukkan angka: "))
# except ValueError:
#     print("Input yang anda masukkan bukan angka")
# except SyntaxError:
#     print("Penempatan syntax salah")
    
# try:
#     angka = int(input("Masukkan angka: "))
# except ValueError:
#     print("Input yang anda masukkan bukan angka")
# else:
#     print(f"Angka yang kamu input: {angka}")

# try:
# angka = int(input("Masukkan angka: "))
# except ValueError:
# print("Input yang anda masukkan bukan angka")
# else:
# print(f"Angka yang kamu input: {angka}")
# finally:
# print("Program selesai")

# try:
# nama = input("Hello, what's your name? ")
# if len(nama) > 5:
# raise ValueError("Nama tidak boleh lebih dari 5

# karakter")
# except ValueError as e:
# print(e)

# # Membuka file untuk dibaca
# file = open('nama_file.txt', 'r')
# # Membuka file untuk ditulis
# file = open('nama_file.txt', 'w')
# # Membuka file untuk menambah data
# file = open('nama_file.txt', 'a')
# # Membaca seluruh isi file sekaligus
# with open('nama_file.txt', 'r') as file:
# konten = file.read()
# print(konten)
# # Membaca baris per baris
# with open('nama_file.txt', 'r') as file:
# for baris in file:
# print(baris, end='')

# # Menulis teks ke file
# with open('nama_file.txt', 'w') as file:
# file.write('Ini adalah baris pertama.\n')
# file.write('Ini adalah baris kedua.\n')

# try:
# with open("data.txt") as file:
# print(file.read())
# except FileNotFoundError:
# print("File tidak ditemukan")

# def input_nama():
#     while True:
#         try:
#             nama = input("Masukkan nama: ")
#             if nama.strip() == "":
#                 raise ValueError("Jangan Di Spasi Dek.")
#             return nama
#         except ValueError as e:
#             print(f"Error: {e}")

# nama = input_nama()
# print("Nama yang Anda masukkan:", nama)