from audioop import mul
from hmac import new
from re import M


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

        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        temp = self.tail
        temp.next = new_node
        self.tail = new_node
        new_node.next = None
        self.length += 1

        return True

    def list_pop(self):
        if self.head is None:
            return False

        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            return self.head

        old_tail = self.tail
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next


        self.tail = temp
        self.length -= 1
        self.tail.next = None
        return old_tail

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        
        new_node.next = self.head
        self.head = new_node
        self.length += 1

        return True

    def pop_fist(self):
        if self.head is None:
            return False

        old_head = self.head
        self.head = self.head.next
        old_head.next = None
        self.length -= 1

        return old_head

    def get(self, index):
        if index < 0 or index >= self.length:
            return False

        temp = self.head

        for _ in range(index):
            temp = temp.next 

        return temp

    def set_value(self, index, value):
        # if index < 0 or index >= self.length:
        #     return False

        # temp = self.head 

        # for _ in range(index):
        #     temp = temp.next

        # temp.value = value
        
        # return True

        temp = self.get(index)

        if temp:
            temp.value = value
            return True

        return False


    def insert(self, index, value):

        if index < 0 or index > self.length:
            return False

        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True
        
        if index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True

        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node

        return True

    def remove(self, index):
        if self.head is None:
            return False

        if index < 0 or index >= self.length:
            return False

        if index == self.length:
            self.list_pop()
            return True

        if index == 0:
            self.pop_fist()
            return True

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
        prev = None

        for _ in range(self.length):
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after
            
        return True
        

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.prepend(5)
my_linked_list.list_pop()
my_linked_list.set_value(1,2)
my_linked_list.insert(0, 10)
my_linked_list.reverse()
my_linked_list.print_list()


        