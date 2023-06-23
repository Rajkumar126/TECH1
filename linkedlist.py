class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                     
                     print(temp.data,"->",end=" ")
                     temp=temp.next
    def insert_beginning(self,data):
         nb=Node(data)
         nb.next=self.head
         self.head=nb
    def insert_end(self,data):
         ne=Node(data)
         temp=self.head
         while temp.next:
              temp=temp.next
        temp.next=ne
        ne.next=None
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
obj.display()