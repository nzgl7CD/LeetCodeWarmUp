class Node:
    def __init__(self, data) -> None:
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def insert_in_front(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def print_list(self):
        current_node=self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node=current_node.next
        print('None')
        
obj=LinkedList()
obj.insert_in_front(10)
obj.insert_in_front(20)

obj.print_list()