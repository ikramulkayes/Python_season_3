class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.itr_lst =""
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Empty")
            return 
        itr = self.head
        
        while itr:
            #print(itr.data)
            self.itr_lst += f"{itr.data}-->"
            itr = itr.next
        print(self.itr_lst)
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def insert_values(self,data_list):
        self.head = None
        for elm in data_list:
            self.insert_at_end(elm)
    def counter(self):
        itr = self.head
        count = 1
        while itr.next:
            count += 1
            itr = itr.next
        print(count)
        return count
    def remove_at(self,index_no):
        if index_no<0 or index_no>self.counter():
            raise "What are you doin"
        elif index_no == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if index_no == count +1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1
    def insert_at(self,index_no,data):
        if index_no<0 or index_no>self.counter():
            raise "What are you doin"
        elif index_no == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if index_no == count+1:
                node = Node(data,itr.next)
                itr.next = node
                return
            itr = itr.next
            count += 1        
            

m = LinkedList()
m.insert_at_begining(2)
m.insert_at_begining(5)
m.insert_at_begining(8)
m.insert_at_end(10)
m.insert_values(["ami","paka","pepe","khay"])
m.counter()
m.remove_at(2)
m.insert_at(2, "pepe")
m.print()