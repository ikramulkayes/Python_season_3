class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head= node
    def print(self):
        if self.head is None:
            print("Emptry")
            return
        itr = self.head
        count = 1
        while itr:
            print(f"{itr.data} ")
            itr= itr.next
            #print(count)
            count += 1

m = LinkedList()
m.insert_at_begining(2)
m.insert_at_begining(5)
m.print()