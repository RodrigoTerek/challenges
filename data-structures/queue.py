
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

# FIFO
class Queue:
    def __init__(self, init=None):
        self.init = init
        self.last = init

    def enqueue(self, node: Node):
        if not self.init:
            self.init = node
            self.last = node
            return

        self.last.next = node
        self.last = node

    def dequeue(self):
        if not self.init:
            raise Exception("Queue is empty")

        aux = self.init
        if self.init == self.last:
            self.init = None
            self.last = None
            return aux

        if aux.next:
            self.init = aux.next

        return aux

    def print(self):
        if not self.init:
            print("<empty queue>")
            return

        aux = self.init
        while aux:
            print(aux.val, end=" -> ")
            aux = aux.next
        print("\n==================================================")


list = Queue(Node(10))

list.enqueue(Node(2))
list.enqueue(Node(8))
list.enqueue(Node(4))
list.enqueue(Node(1))
list.enqueue(Node(2))
list.print()

list.dequeue()
list.print()

list.dequeue()
list.print()

list.dequeue()
list.print()

list.dequeue()
list.print()

list.dequeue()
list.print()

list.dequeue()
list.print()

