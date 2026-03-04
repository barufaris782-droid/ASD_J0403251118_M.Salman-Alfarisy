#====================================================
#Nama    : Muhammad Salman Alfarisy
#NIM     : J0403251118
#Kelas   : TPL B1
#====================================================

#====================================================
#Praktikum 4 : Sistem antrian layanan akademik (STUDI KASUS)
# Implementasi Queue
# Enqueue: Menambahkan pelanggan baru ke antrian (memindahkan pointer tail ke node baru)
# Dequeue: Melayani pelanggan di depan antrian (memindahkan pointer head ke node berikutnya)
# stack -> LIFO (Last In First Out) ==> Head -> B -> C -> A -> None
# Queue -> FIFO (First In First Out) ==> Head -> A -> B -> C -> Rear
# ====================================================

#1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim = nim  # Nim mahasiswa
        self.nama = nama # menyimpan nama mahasiswa
        self.next = None # pointer ke node berikutnya (awal)

#2) Mendefinisikan Queue terdiri dari Head dan Tail
class queueAkademik:
    def __init__(self):
        self.head = None #awal kosong
        self.tail = None #awal kosong

    def is_empty(self):
        #fungsi untuk memeriksa apakah antrian kosong (head None)
        return self.head is None
    
    def enqueue(self, nim, nama):
        NodeBaru = Node(nim, nama) #buat node baru dengan data nim dan nama
        # jika data baru masuk dari queue yang kosong, maka head dan tail sama-sama menunjuk ke node baru
        if self.is_empty(): 
            self.head = NodeBaru
            self.tail = NodeBaru
            return
        #Jika queue tidak kosong, tambahkan node baru di belakang tail kemudian dijadikan sebagai tail
        self.tail.next = NodeBaru #tail lama menunjuk ke node baru
        self.tail = NodeBaru #tail menunjuk ke node baru
    #menghapus data dari depan head (dihapus dari head)
    def dequeue(self):

        if self.is_empty():
            print("Antrian kosong, tidak ada mahasiswa yang bisa dilayani.")
            return None
        #lihat data bagian Head, simpan di variabel data yang akan dihapus
        node_dilayani = self.head

        #geser head ke node berikutnya
        self.head = self.head.next
        #jika setelah geser head menjadi None, berarti antrian kosong, maka tail juga harus di-set ke None
        if self.head is None:
            self.tail = None
        return node_dilayani
    
    def tampilkan(self):

        print("Daftar Antrian Mahasiswa (Head -> Tail):")
        current = self.head
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

#Program Utama

def main():

    #instantiasi queue
    q = queueAkademik()

    while True:
        print("\nMenu Antrian Akademik")
        print("1. Tambah Mahasiswa") #Enqueue
        print("2. Layani Mahasiswa ") #Dequeue
        print("3. Lihat antrian")
        print("0. Keluar")

        pilihan = input("Pilih Menu (1-4): ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM Mahasiswa: ").strip()
            nama = input("Masukkan Nama Mahasiswa: ").strip()
            q.enqueue(nim, nama)
            print(f"Mahasiswa {nama} dengan NIM {nim} berhasil ditambahkan ke antrian.")
        elif pilihan == "2":
            mahasiswa_dilayani = q.dequeue()
            if mahasiswa_dilayani:
                print(f"Mahasiswa yang dilayani: {mahasiswa_dilayani.nim} - {mahasiswa_dilayani.nama}")
        elif pilihan == "3":
            q.tampilkan()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

#penanda eksekusi program utama
if __name__ == "__main__":
    main()
        