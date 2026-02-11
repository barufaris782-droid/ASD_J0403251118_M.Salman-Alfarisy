# 1. Definisi Node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 2. Definisi Linked List 
class LinkedList:
    def __init__(self):
        self.head = None

    # Fungsi tambah data di akhir 
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None


    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# --- CARA MENJALANKANNYA ---
ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)

print("Sebelum dihapus:")
ll.display() # Hasil: 3 -> 5 -> 13 -> 2 -> null

ll.delete_node(13) # Kita hapus angka 13

print("Setelah 13 dihapus:")
ll.display() # Hasil: 3 -> 5 -> 2 -> null