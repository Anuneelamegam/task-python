i = 0
 

class node:
    def __init__(self, k=0, p=None, n=None):
        self.key = k
        self.prev = p
        self.next = n
 
 

head = None
first = None
temp = None
tail = None
 


def addnode(k: int):
    global i, head, first, tail
    
    ptr = node(k)
 

    if head == None:
        head = ptr
        first = head
        tail = head
 
    
    else:
        temp = ptr
        first.next = temp
        temp.prev = first
        first = temp
        tail = temp
 
    
    i += 1
 
 

def traverse():
    # Nodes points towards head node
    ptr = head
 
    # While pointer is not None,
    # traverse and print the node
    while ptr != None:
 
        # Print key of the node
        print(ptr.key, end=" ")
        ptr = ptr.next
 
    print()
 
 
# Function to insert a node at the
# beginning of the linked list
def insertatbegin(k: int):
    global head, first, tail, i
 
    # Allocating memory
    # to the Node ptr
    ptr = node(k)
 
    # If head is None
    if head == None:
        first = ptr
        first = head
        tail = head
 
    # Else insert at beginning and
    # change the head to current node
    else:
        temp = ptr
        temp.next = head
        head.prev = temp
        head = temp
 
    i += 1
 
 
# Function to insert Node at end
def insertatend(k: int):
    global head, first, tail, i
 
    # Allocating memory
    # to the Node ptr
    ptr = node(k)
 
    # If head is None
    if head == None:
        first = ptr
        first = head
        tail = head
 

    else:
        temp = ptr
        temp.prev = tail
        tail.next = temp
        tail = temp
 
    i += 1
 
 

def insertatpos(k: int, pos: int):
    global i
 
    # For Invalid Position
    if pos < 1 or pos > i + 1:
        print("Please enter a" " valid position")
 
    # If position is at the front,
    # then call insertatbegin()
    elif pos == 1:
        insertatbegin(k)
 
    # Position is at length of Linked
    # list + 1, then insert at the end
    elif pos == i + 1:
        insertatend(k)
 
    # Else traverse till position pos
    # and insert the Node
    else:
        src = head
 
        # Move head pointer to pos
        while pos:
            pos -= 1
            src = src.next
 
        # Allocate memory to new Node
        ptr = node(k)
 
        # Change the previous and next
        # pointer of the nodes inserted
        # with previous and next node
        ptr.next = src
        ptr.prev = src.prev
        src.prev.next = ptr
        src.prev = ptr
        i += 1
 
 
# Function to delete node at the
# beginning of the list
def delatbegin():
    # Move head to next and
    # decrease length by 1
    global head, i
    head = head.next
    i -= 1
 
 
# Function to delete at the end
# of the list
def delatend():
    # Mode tail to the prev and
    # decrease length by 1
    global tail, i
    tail = tail.prev
    tail.next = None
    i -= 1
 
 
# Function to delete the node at
# a given position pos
def delatpos(pos: int):
    global i
    # If invalid position
    if pos < 1 or pos > i + 1:
        print("Please enter a" " valid position")
 
    # If position is 1, then
    # call delatbegin()
    elif pos == 1:
        delatbegin()
 
    # If position is at the end, then
    # call delatend()
    elif pos == i:
        delatend()
 
    # Else traverse till pos, and
    # delete the node at pos
    else:
        # Src node to find which
        # node to be deleted
        src = head
        pos -= 1
 
        # Traverse node till pos
        while pos:
            pos -= 1
            src = src.next
 
        
        src.prev.next = src.next
        src.next.prev = src.prev
 
        
        i -= 1
 
 

if __name__ == "__main__":
    # Adding node to the linked List
    addnode(2)
    addnode(4)
    addnode(9)
    addnode(1)
    addnode(21)
    addnode(22)
 
    
    print("Linked List: ")
    traverse()
 
    print("\n")
 
    
    insertatbegin(1)
    print("Linked List after inserting 1 at beginning: ")
    traverse()
 
    
    insertatend(0)
    print("Linked List after inserting 0 at end: ")
    traverse()
 
    
    insertatpos(44, 3)
    print("Linked List after inserting 44 after 3rd Node: ")
    traverse()
 
    print("\n")
 
    
    delatbegin()
    print("Linked List after deleting node at beginning: ")
    traverse()
 
    
    delatend()
    print("Linked List after deleting node at end: ")
    traverse()
 
    
    print("Linked List after deleting node at position 5: ")
    delatpos(5)
    traverse()
