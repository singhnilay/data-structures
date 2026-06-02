class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head

        while temp != None:
            print(temp)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else: 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return False

        if self.head.next is None:
            oldTail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return oldTail


        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1

            return temp

    
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:       
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True


    def popFirst(self):

        if self.head is None:
            return None

        elif self.head.next is None:
            oldTail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return oldTail

        else: 

            temp = self.head

            temp.next.prev = None
            temp.next = None
            self.length -= 1
            return temp

    def get(self, index):

        if index < 0 or index >= self.length:
            return None


        if index< self.length // 2:

            temp = self.head

            for _ in range(index):
                temp = temp.next

            return temp
        
        else: 
            temp = self.tail
            for _ in range(self.length - 1 , index , -1):
                temp = temp.prev

            return temp

    def set_value(self, index, value):

        temp = self.get(index)

        if temp:
            temp.value = value
            return True

        return False


    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            self.prepend(value)

        if index == self.length:
            self.append(value)

        newNode = Node(value)


        if index < self.length // 2:
            temp = self.head

            for _ in range(index):
                temp = temp.next

            newNode.next = temp.next
            temp.next.prev = newNode
            temp.next = newNode

        else:

            temp = self.tail

            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

                temp.prev

            

            