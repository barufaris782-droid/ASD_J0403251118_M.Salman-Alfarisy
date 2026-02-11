class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    # Fungsi untuk menambah data di akhir (agar bisa kita tes) 
    def insert_at_end(self, data):
        node_baru = Node(data)
        if not self.head:
            self.head = node_baru
            node_baru.next = self.head # Menunjuk ke diri sendiri 
            return
        temp = self.head
        while temp.next != self.head: # Cari orang terakhir 
            temp = temp.next
        temp.next = node_baru
        node_baru.next = self.head # Sambungkan balik ke head 

    # --- JAWABAN LATIHAN 2: Fungsi Pencarian ---
    def search(self, key):
        # Contoh Tampilan #3: Jika kosong 
        if not self.head:
            print("Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head
        # Kita gunakan loop untuk mengecek setiap node 
        while True:
            if temp.data == key:
                # Contoh Tampilan #1: Jika ketemu 
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return True
            
            temp = temp.next
            
            # Berhenti kalau sudah muter balik ke orang pertama lagi
            if temp == self.head:
                break
        
        # Contoh Tampilan #2: Jika tidak ketemu 
        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")
        return False

# --- CARA MENJALANKANNYA ---
cll = CircularSinglyLinkedList()        
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.insert_at_end(40)
# Mencari elemen yang ada
cll.search(20)  # Output: Elemen 20 ditemukan dalam Circular Linked List.
# Mencari elemen yang tidak ada
cll.search(50)  # Output: Elemen 50 tidak ditemukan dalam Circular Linked
# Mencari di list yang kosong
cll_kosong = CircularSinglyLinkedList()
cll_kosong.search(10)

