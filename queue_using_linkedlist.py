class Empty(Exception):
    pass


class queue_using_linkedlist:
    class node:
        __slots__ = 'element', 'next'

        def __init__(self,element,next):
            self.element = element
            self.next = next
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def enqueue(self,element):
        new_node = self.node(element,None)
        if self.is_empty():
            self.head= new_node
        else:
            self.tail.next= new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("queue is empty")
        value = self.head.element
        self.head = self.head.next
        self.size -=1
        if self.is_empty:
            self.tail= None
        return value
        
    def first(self):
        if self.is_empty():
            raise Empty("queue is empty")
        return self.head.element

    def display(self):
        temp = self.head
        while temp:
            print(temp.element, end = '-->')
            temp =temp.next
        print()

# q= queue_using_linkedlist()

# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.display()

# print('length', q.len())

# q.dequeue()

# print('length', q.len())
# q.display()
# print(q.first())

        