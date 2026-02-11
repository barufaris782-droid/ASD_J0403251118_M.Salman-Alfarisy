class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    # Fungsi untuk menambah data [cite: 305-313]
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Fungsi untuk menampilkan list dengan format -> null 
    def display(self):
        if not self.head:
            print("kosong")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# Fungsi Utama untuk Menggabungkan 
def merge_lists(list1, list2):
    # Jika list 1 kosong, hasilnya list 2 
    if not list1.head:
        return list2
    
    # Jika list 2 tidak kosong, sambungkan ekor list 1 ke kepala list 2 
    if list2.head:
        temp = list1.head
        while temp.next: # Cari node terakhir list 1 
            temp = temp.next
        temp.next = list2.head # Sambungkan! 
    
    return list1

# --- BAGIAN MENJALANKAN PROGRAM ---
if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()

    # Input untuk Linked List 1
    data1 = input("Masukkan elemen untuk Linked List 1 (pisahkan dengan koma): ")
    if data1.strip(): # Cek jika tidak kosong
        for x in data1.split(','):
            ll1.insert_at_end(x.strip())

    # Input untuk Linked List 2
    data2 = input("Masukkan elemen untuk Linked List 2 (pisahkan dengan koma): ")
    if data2.strip(): # Cek jika tidak kosong
        for x in data2.split(','):
            ll2.insert_at_end(x.strip())

    # Tampilkan kondisi awal
    print("\nLinked List 1:", end=" ")
    ll1.display()
    print("Linked List 2:", end=" ")
    ll2.display()

    # Gabungkan
    combined_list = merge_lists(ll1, ll2)

    # Tampilkan hasil akhir 
    print("Linked List setelah digabungkan:", end=" ")
    combined_list.display()