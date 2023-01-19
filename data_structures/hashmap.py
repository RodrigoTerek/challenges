
class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.val = value
        self.next = next

    def __str__(self) -> str:
        return "{}: {}".format(self.key, self.val)


class LinkedList:
    def __init__(self, init: Node | None = None):
        self.init = init
        self.last = init

    def add(self, node: Node):
        if not self.init:
            self.init = node
            self.last = node
            return

        self.last.next = node
        self.last = node

    def remove(self, key: int):
        auxBef = None
        aux = self.init

        while aux:
            if aux.key == key:
                break
            auxBef = aux
            aux = aux.next

        if aux == None:
            return None

        if auxBef:
            auxBef.next = aux.next
        elif aux.next:
            self.init = aux.next
        else:
            self.init = None
            self.last = None

        return aux

    def get(self, key: int):
        aux = self.init

        while aux:
            if aux.key == key:
                return aux
            aux = aux.next

        return None

    def getAll(self):
        allNodes = []

        aux = self.init
        while aux:
            allNodes.append(aux)
            aux = aux.next

        return allNodes

    def print(self):
        if not self.init:
            print('<empty>')
            return

        aux = self.init
        i = 0
        while aux:
            print(i, aux.key, aux.val, end=", ")
            aux = aux.next
            i += 1
        print()


class HashMap:
    def __init__(self):
        self.arr: list[LinkedList] = []
        self.size = 0

        for _ in range(13):
            self.arr.append(LinkedList())

    def insert(self, key, value):
        node = Node(key, value)

        pos = hash(key) % len(self.arr)
        self.arr[pos].add(node)

        self.size += 1

        if (self.size / len(self.arr) > 0.9):
            self.rehash()
        return

    def rehash(self):
        print('rehashing')
        allNodes = []
        for list in self.arr:
            allNodes += list.getAll()

        previousLen = len(self.arr)
        self.arr = []
        for _ in range(previousLen * 2):
            self.arr.append(LinkedList())

        for n in allNodes:
            pos = hash(n.key) % len(self.arr)
            self.arr[pos].add(n)

    def get(self, key):
        pos = hash(key) % len(self.arr)
        return self.arr[pos].get(key)

    def remove(self, key):
        pos = hash(key) % len(self.arr)
        node = self.arr[pos].remove(key)
        if node != None:
            self.size -= 1
        return node

    def getSize(self):
        return self.size

    def print(self):
        for list in self.arr:
            list.print()


map = HashMap()
map.insert('usr1', 1234)
map.insert('usr2', 4321)
map.insert('usr3', 4684)
map.insert('acc1', 8215)
map.insert('acc2', 1321)
map.insert('acc3', 8465)
map.insert('acc5', 8465)
map.insert('acc6', 8465)
map.insert('acc7', 8465)
map.insert('acc8', 8465)
map.insert('acc9', 8465)
map.insert('acc0', 8465)
map.insert('ac2', 8465)
map.insert('ac12', 8465)
map.insert('ac234', 8465)
map.insert('acc30', 8465)
map.insert('acc31', 8465)
map.insert('acc32', 8465)
map.insert('acc33', 8465)
map.insert('acc323', 8465)
map.insert('acc35', 8465)
map.insert('acc34', 8465)
map.insert('acc36', 8465)
map.insert('acc32', 8465)
map.insert('acc35', 8465)
map.insert('acc21', 8465)
map.insert('acc22', 8465)
map.insert('acc23', 8465)
map.insert('acc24', 8465)
map.insert('acc25', 8465)
map.insert('acc26', 8465)

map.print()
print(map.getSize())
print('\n==============\n')

print(map.get('usr3'))
print(map.get('usr4'))
print(map.get('acc2'))
print('\n==============\n')

print(map.remove('acc3'))
print(map.remove('usr3'))
print(map.remove('acc4'))
print('\n==============\n')

map.print()
print(map.getSize())
print('\n==============\n')

# print(map.rehash())
map.print()
