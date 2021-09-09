#SINGLE LINK LIST
#======================================================================
import os

#membuat class untuk Node
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    #mengambil data dari node
    def get_data(self):
        return self.data
    
    #mengambil data berikutnya
    def get_next(self):
        return self.next_node
    
    #menentukan data berikutnya
    def set_next(self, new_next):
        self.next_node = new_next

#membuat class untuk Linked List
class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    #Menambah node baru
    def tambahdepan(self, data):
        #inisialisasi node baru
        new_node = Node(data)
        #jika head masih kosong
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
        else :
            new_node.set_next(self.head)
            self.head = new_node
    
    def tambahbelakang(self, data):
        #inisialisasi node baru
        new_node = Node(data)
        #jika head masih kosong
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next_node = new_node
            self.tail = new_node
    
    #menambah sebuah data di tengah pada list
    def tambahtengah(self, data):
        #membuat pointer baru menunjuk ke node yang ditunjuk oleh HEAD
        current = self.head
        found = False
        #perulangan mencari node yang dicari
        while current and found is False :
            if current.get_data() == data:
                found = True
                obj1 = str(input("Masukkan data yang ingin anda tambahkan :"))
                new_node = Node(obj1)
                new_node.next_node = current.next_node
                current.next_node = new_node
            else :
                current = current.get_next()
        return found
    
    def cari(self, data):
        #membuat pointer baru menunjuk ke node yang ditunjuk oleh HEAD
        current = self.head
        found = False
        idx = 0
        #perulangan mencari node yang dicari
        while current and found is False :
            idx += 1
            if current.get_data() == data :
                found = True
                print("Ketemu pada urutan ke -", idx)
                x = input("")
            else :
                current = current.get_next()
        return found
    
    #menghapus data di depan list
    def deletedidepan(self):
        if(self.head is None):
            print("Data Tidak Ada")
        else : 
            self.head = self.head.next_node

    #menghapus data di belakang list
    def deletedibelakang(self):
        current_node = self.head
        if(self.head is None):
            print("Data Tidak Ada")
        else : 
            while current_node.next_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = self.tail.next_node
            self.tail = current_node
    
    #menghapus data di tengah list
    def deleteditengah(self, Removekey):
            current = self.head
            if (current is not None):
                if (current.data == Removekey):
                    self.head = current.next_node
                    current = None
                    return
            while (current is not None):
                if current.data == Removekey:
                    break
                prev = current
                current = current.next_node
            if (current == None):
                return
            prev.next_node = current.next_node
            current = None
            
    #menampilkan isi list
    def showData(self):
        os.system("cls")
        print("Tampilkan list data :")
        print("Node -> Next Node")
        current_node = self.head
        if(self.head is None):
            print("Data masih kosong")
        else : 
            while current_node is not None:
                print(current_node.data)
                print(" ->")
                current_node = current_node.next_node
    def cekKosong(self):
        if(self.head is None):
            return True
        else :
            return False
    #main menu aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("cls")
            print("===================================")
            print("|    Menu aplikasi linked list    |")
            print("===================================")
            print("1. Tambah Depan")
            print("2. Tambah Belakang")
            print("3. Mencari Data")
            print("4. Tambah Data di Tengah")
            print("5. Hapus Data di Depan")
            print("6. Hapus Data di Belakang")
            print("7. Hapus Data di Tengah")
            print("8. Tampil Data")
            print("===================================")
            pilihan = input("Silahkan masukkan pilihan anda :")
            if(pilihan == "1"):
                os.system("cls")
                self.showData()
                obj = input("Masukkan data yang ingin ditambahkan di depan : ")
                self.tambahdepan(obj)
            elif(pilihan == "2"):
                os.system("cls")
                self.showData()
                obj = input("Masukkan data yang ingin ditambahkan di belakang : ")
                self.tambahbelakang(obj)
            elif(pilihan == "3"):
                os.system("cls")
                if self.cekKosong() == False:
                    self.showData()
                    obj = input("Masukkan data yang ingin anda cari : ")
                    self.cari(obj)
                else :
                    self.showData()
                    x = input("")
            elif(pilihan == "4"):
                os.system("cls")
                self.showData()
                obj = input("Tambah data setelah : ")
                self.tambahtengah(obj)
            elif(pilihan == "5"):
                os.system("cls")
                self.showData()
                if self.cekKosong() == False:
                    self.deletedidepan()
                else :
                    print("Data masih kosong")
                    x = input("")
            elif(pilihan == "6"):
                os.system("cls")
                self.showData()
                if self.cekKosong() == False:
                    self.deletedibelakang()
                else :
                    print("Data masih kosong")
                    x = input("")
            elif(pilihan == "7"):
                os.system("cls")
                self.showData()
                if self.cekKosong() == False:
                    obj = input("Masukkan data yang ingin anda hapus : ")
                    self.deleteditengah(obj)
                else :
                    print("Data masih kosong")
                    x = input("")

            elif(pilihan == "8"):
                os.system("cls")
                self.showData()
                x = input("")
            else :
                pilih = "n"
if __name__ == "__main__" :
    l = LinkedList()
    l.mainmenu()