#double linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Double_Linked_List:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp = temp.next
            temp.next=new_node
            new_node.prev=temp
    def insert_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            self.head.prev = new_node
            new_node.next=self.head
            self.head = new_node
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def traverse_backward(self):
        temp=self.head
        if not temp:
            return
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end=" ")
            temp=temp.prev
        print()
saj=Double_Linked_List()
saj.insert_at_end(10)
saj.insert_at_end(20)
saj.insert_at_end(30)
saj.traverse_forward()
saj.insert_at_beginning(5)
saj.traverse_forward()
saj.traverse_backward()
