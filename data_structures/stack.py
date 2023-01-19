
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Stack:
    def __init__(self, init=None):
        self.init = init
        self.last = init

    def push(self, node: Node):
        if not self.init:
            self.init = node
            self.last = node
            return

        self.last.next = node
        self.last = node

    def pop(self):
        aux = self.init
        if self.init == self.last:
            self.init = None
            self.last = None
            return aux

        auxNext = aux.next

        while auxNext.next:
            aux = auxNext
            auxNext = auxNext.next

        aux.next = None
        self.last = aux

        return auxNext

    def print(self):
        if not self.init:
            print("<empty stack>")
            return

        aux = self.init
        while aux:
            print(aux.val, end=" -> ")
            aux = aux.next
        print("\n==================================================")


list = Stack(Node(10))

list.push(Node(2))
list.push(Node(8))
list.push(Node(4))
list.push(Node(1))
list.push(Node(2))

list.print()

list.pop()
list.print()

list.pop()
list.print()

list.pop()
list.print()

list.push(Node(12))
list.push(Node(13))
list.print()

list.pop()
list.print()
