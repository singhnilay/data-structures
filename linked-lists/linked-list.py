class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp != None:
            print(temp.value)
            temp = temp.next

    def list_append(self, value):
        new_node = Node(value)

        if self.length is not None :
            self.tail.next = new_node
            self.tail = new_node

        else :
            self.head = new_node
            self.tail = new_node

        self.length += 1

        return True

    def list_pop(self):

        if self.head is None:
            return "Cannot Pop from an Empty List"

        elif self.length == 1:
            old_tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1

            return old_tail

        else : 
            temp = self.head
            old_tail = self.tail

            while temp.next != self.tail:
                temp = temp.next

            self.tail = temp
            self.tail.next = None
            self.length -= 1


            return old_tail

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else :
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1
        
    def pop_first(self) : 

        if self.length == 0:
            return None

        prev_head = self.head
        
        self.head = self.head.next
        prev_head.next = None

        return prev_head

    def get(self, index):
        if index > (self.length - 1) or index < 0:
            return None

        temp = self.head
        
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index,value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True

        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.length += 1
            return self.prepend(value)
            

        if index == self.length:
            self.length += 1
            return self. list_append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False

        elif index == 0:
            return self.pop_first()

        elif index == self.length:
            return self.list_pop

        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True
        
        
        
my_linked_list = LinkedList(10)
my_linked_list.list_append(4)
print(f"Linked List before popping the last element : ")
my_linked_list.print_list()
my_linked_list.list_pop()

print(f"Linked List after popping the last element : ")
my_linked_list.print_list()

print(f"The list after prepending: ")
my_linked_list.prepend(1)
my_linked_list.print_list()




