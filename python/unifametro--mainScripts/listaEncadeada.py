# Implementação de uma Lista Encadeada (padrão Linked List)

class Node():
    data: any
    next: 'Node' = None
    def __init__(self, data_insert):
        self.data = data_insert
    
    def getData(self):
        return self.data
    
    def setNext(self, node_insert: 'Node'):
        self.next = node_insert

class custom_LinkedList(): # FI, LO
    head: Node
    def __init__(self): #Primeiro estado, inicialização
        self.head = None
    
    def insertData(self, newData):
        new: Node = Node(newData)
        new.setNext(self.head)      #passando início para o fim 
        self.head = new             #tomando lugar de início
        return self.head.getData()

    def searchData(self, data_searched):
        current: Node = self.head
        while(True):
            if current.next == None:                        # Fim da linha
                return None
            elif current.next.getData() == data_searched:   # Achou o dado
                return current.next.getData()
            else: current = current.next                    # Não achou o dado

    def printAll(self):
        current: Node = self.head
        i = 0
        while(True):
            if current == None: break;

            i += 1
            print(f"Node {i} -> {current.getData()}")
            current = current.next
            

if __name__ == "__main__":
    linked = custom_LinkedList()
    linked.insertData(1)
    linked.insertData(2)
    linked.insertData(3)
    linked.insertData("abc")
    
    print(linked.searchData(1))
    linked.printAll()

    print("END OF CODE")