class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.left = None;    
        self.middle = None;    
        self.right = None;    
            
class TernaryTreeToDLL:    
    def __init__(self):    
 
        self.root = None;    
     
        self.head = None;    
        self.tail = None;    
            
     
    def convertTernaryToDLL(self, node):    
          
        if(node == None):    
            return;    
                
       
        left = node.left;    
        middle = node.middle;    
        right = node.right;    
            
           
        if(self.head == None):    
               
            self.head = self.tail = node;    
            node.middle = None;    
              
            self.head.left = None;    
                
            self.tail.right = None;    
        
        else:    
               
            self.tail.right = node;    
        
            node.left = self.tail;    
            node.middle = None;    
             
            self.tail = node;    
                
            self.tail.right = None;    
                
   
        self.convertTernaryToDLL(left);    
           
        self.convertTernaryToDLL(middle);    
            
        self.convertTernaryToDLL(right);    
        
       
    def displayDLL(self):    
         
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        print("Nodes of generated doubly linked list: ");    
        while(current != None):    
              
            print(current.data),    
            current = current.right;    
                
tree = TernaryTreeToDLL();    
  
tree.root = Node(4);    
tree.root.left = Node(10);    
tree.root.middle = Node(12);    
tree.root.right = Node(25);    
tree.root.left.left = Node(20);    
tree.root.left.middle = Node(70);    
tree.root.left.right = Node(50);    
tree.root.middle.left = Node(24);    
tree.root.middle.middle = Node(66);    
tree.root.middle.right = Node(48);    
tree.root.right.left = Node(10);    
tree.root.right.middle = Node(45);    
tree.root.right.right = Node(90);    
     
   
tree.convertTernaryToDLL(tree.root);    
       
tree.displayDLL();    
