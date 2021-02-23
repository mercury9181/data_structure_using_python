class Empty(Exception):
    pass


class linkedlist:
    class node:
        __slots__ = 'element', 'next'

        def __init__(self,element,next):
            self.element = element
            self.next = next
    

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def length(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def add_first(self,element):
        newest = self.node(element,None)
        if self.is_empty():
            self.head = newest
            self.tail = newest
        else:
            newest.next = self.head
        self.head = newest
        self.size += 1
    

    def add_last(self,element):
        newest = self.node(element,None)
        if self.is_empty():
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1
    

    def add_anywhere(self,element,position):
        newest = self.node(element,None)
        thead = self.head
        i=1

        while i < position:
            thead = thead.next
            i += 1
        newest.next= thead.next
        thead.next =newest
        self.size += 1




    def remove_first(self):
        if self.is_empty():
            raise Empty("linked list is empty")
        value= self.head.element
        self.head= self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return value
    
    def remove_last(self):
        if self.is_empty():
            raise Empty("linked list is empty")
        thead = self.head
        i = 1
        while i < self.size-1:
            thead = thead.next
            i +=1
        self.tail= thead
        thead = thead.next
        value = thead.element
        self.tail.next = None
        self.size -= 1
        return value

    def remove_any(self,position):
        if self.is_empty():
            raise Empty("linked list is empty")
        thead = self.head
        i = 1
        while i < position-1:
            thead = thead.next
            i +=1
        value = thead.next.element
        thead.next = thead.next.next
        self.size-=1
        return value

    def display(self):
        thead= self.head
        while thead:
            print(thead.element, end='--->')
            thead = thead.next
        print()

link= linkedlist()
link.add_last(10)
link.add_last(20)
link.add_last(30)
link.add_last(40)
link.add_last(50)
link.add_last(60)
link.display()
print("first deleted",link.remove_first())
link.display()
print("last deleted",link.remove_last())
link.display()
link.add_last(90)
link.add_anywhere(60,2)
link.display()
print("delete at position 3",link.remove_any(3))
link.display()








