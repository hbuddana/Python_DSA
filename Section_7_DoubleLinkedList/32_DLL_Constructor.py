# Creation of a Node Class

class Node: 
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None # None <- 7 -> None


class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        

my_dll = DoublyLinkedList(7)

my_dll.print_list()