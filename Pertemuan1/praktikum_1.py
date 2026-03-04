#==========================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1A : Membaca seluruh Isi Teks File 
#==========================

#membuka file dengan metode read ("r")
with open ("Data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("Hasil Read")
print("Tipe Data", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("Jumlah Baris", isi_file.count("\n")+1)

print("====membaca file per baris====")
jumlah_baris = 0
with open("Data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris=+1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print("isinya :", baris)

#==========================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : konsep parsing data
#==========================
with open("Data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai, = baris.split(",") #parsing data berdasarkan koma
        print("NIM :", nim, "Nama :", nama, "Nilai: ", nilai)

#==========================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : membaca file dan menyimpan ke list
#==========================
data_list = []
with open("Data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        data_list.append([nim,nama,int(nilai)])

print("====Data_mahasiswa dalam list")
print(data_list)

print("====jumlah record dalam list=====")
print("Jumlah record", len(data_list))

print("=====menampilkan data record tertentu====")
print("contoh record pertama", data_list[0])

#==========================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : membaca file dan menyimpan file ke dictionary
#==========================
data_dict = {} 
with open("Data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai, = baris.split(",") #parsing data berdasarkan koma
        #simpan data mahsiswa ke dictionary dengan key NIM
        data_dict[nama,nim] = {  #key
            "nama": nama,  #values
            "nilai": int(nilai)  #values
        }
print("=====data mahasiswa dalam dictionary=====")
print(data_dict)



