class Empty(Exception):
    pass


class dequeue_using_linkedlist:
    class node:
        __slots__ = 'element', 'next'

        def __init__(self,element,next):
            self.element = element
            self.next = next
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def len(self):
        return self.size

    def is_empty(self):
        return self.size==0
    
    def add_first(self,element):
        newest = self.node(element,None)
        if self.is_empty():
            self.head = newest
            self.tail = newest
        else:
            newest.next = self.head
        self.head =newest
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
    
    def remove_first(self):
        if self.is_empty():
            raise Empty("dequeue empty")
        value = self.head.element
        self.head = self.head.next
        self.size -=1
        return value

    def remove_last(self):
        if self.is_empty():
            raise Empty("dequeue empty")
        thead = self.head
        i= 1
        while i< self.size -1:
            thead = thead.next
            i+=1
        self.tail = thead
        thead = thead.next
        value = thead.element
        self.tail.next = None
        self.size -= 1
        return value

    def display(self):
        thead = self.head
        while thead:
            print(thead.element, end ='-->')
            thead = thead.next
        print()

dq = dequeue_using_linkedlist()

dq.add_first(10)
dq.add_first(20)
dq.add_last(30)
dq.display()
dq.remove_first()
dq.display()
dq.add_last(100)
dq.display()
dq.remove_last()
dq.display()


