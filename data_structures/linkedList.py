
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class List:
    def __init__(self, init=None):
        self.init = init
        self.last = init

    def add(self, node: Node):
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

    def remove(self, index: int):
        auxBef = None
        aux = self.init

        while (index > 0):
            if not aux.next:
                raise IndexError("Index out of range")

            auxBef = aux
            aux = aux.next
            index -= 1

        if auxBef:
            auxBef.next = aux.next
        elif aux.next:
            self.init = aux.next
        else:
            self.init = None
            self.last = None

        return aux

    def get(self, index: int):
        aux = self.init

        while (index > 0):
            if not aux.next:
                raise IndexError("Index out of range")

            aux = aux.next
            index -= 1

        return aux.val

    def print(self):
        if not self.init:
            print("<empty list>")
            return

        aux = self.init
        while aux:
            print(aux.val, end=" -> ")
            aux = aux.next
        print("\n==================================================")


list = List(Node(10))

list.add(Node(2))
list.add(Node(8))
list.add(Node(4))
list.add(Node(1))
list.add(Node(2))

list.print()

list.remove(2)
list.print()

list.remove(2)
list.print()

list.remove(0)
list.print()

list.add(Node(12))
list.add(Node(13))
list.print()


list.pop()
list.print()
