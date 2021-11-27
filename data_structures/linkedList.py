#lets create a linked list with 3 nodes

# let's create a node class
class Node:
    #function to initiate the node object
    def __init__(self, data):
        self.data = data
        self.next = None # points to the next node, let's keep it none for now

#Linked list class contains a node object

class LinkedList:

    #function to initialise head
    def __init__(self):
        self.head = None

    #function to print the linked list
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    #function to insert a new node at the beginning
    def push(self, new_data):
        #create a new node
        new_node = Node(new_data)
        #make next of new node as the head
        new_node.next = self.head
        #move the head to point to new node
        self.head = new_node

    #function to add a


# code execution starts here
if __name__=='__main__':
    #start with an empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second;
    second.next = third;

    llist.printlist()
