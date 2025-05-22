from .listaEncadeada import Node # do not use crude, its a linked list Node

class ListNode(Node):
    #do not use 'next'!
    last: 'ListNode' = None
    
    def __init__(self, data_insert):
        super().__init__(data_insert)
        del self.next #not used
        
    def getData(self):
        return super().getData()
    
    def setLast(self, node_insert):
        self.last = node_insert
    
    def setNext(self, node_insert):
        print("Please use 'setLast()'")
        self.setLast(node_insert)

class custom_Queue():
    head: ListNode
    
    def __init__(self, node: ListNode = None): #always start with 1 element
        self.head = node
        
    #managing
    def add(self, newValue: ListNode, currentNode = head): #FI
        if self.head == None:
            self.head = newValue
        
        if currentNode.last:
            self.add(self)
        else:
            newNode = ListNode(newValue)
            currentNode.setLast(newNode)
            print(f"Added to the node with value {currentNode.data}, a new node with value {newNode.data}")
                
    def remove(self) -> ListNode: #FO
        nodeReturned = self.head
        self.head = nodeReturned.last
        
        return nodeReturned