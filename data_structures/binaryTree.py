
import math


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, node=None):
        self.root = node
        self.size = 1 if node else 0

    def insert(self, newNode: Node):
        if not self.root:
            self.root = newNode
            return

        aux = self.root
        while True:
            if newNode.val == aux.val:
                return

            parent = aux
            if newNode.val < aux.val:
                aux = aux.left
                if not aux:
                    parent.left = newNode
                    self.size += 1
                    return
            else:
                aux = aux.right
                if not aux:
                    parent.right = newNode
                    self.size += 1
                    return

    def remove(self, value: int):
        return

    def get(self, value: int):
        return self.get(value, self.root)

    def get(self, value: int, node: Node):
        if node.val == value:
            return node

        if value < node.val and node.left:
            return self.get(value, node.left)

        if value > node.val and node.right:
            return self.get(value, node.right)

        return "not found"

    def print(self, node=None):
        if not node:
            if not self.root:
                print("<empty tree>")
                return
            node = self.root

        if node.left:
            self.print(node.left)

        print(node.val, end=" - ")

        if node.right:
            self.print(node.right)

    def printByLevel(self):
        if not self.root:
            print("<empty tree>")
            return

        arr = [None] * self.size
        print(arr)
        printArr = self.createPrintArr(self.root, arr)
        print(printArr)

    def createPrintArr(self, node: Node, arr, i=0):
        if node.left:
            self.createPrintArr(node.left, arr, i + 1)

        if node.right:
            self.createPrintArr(node.right, arr, i + 1)

        if not arr[i]:
            arr[i] = [node.val]
        else:
            arr[i].append(node.val)

        return arr


tree = BinaryTree(Node(10))
tree.printByLevel()
print()
tree.insert(Node(2))
tree.printByLevel()
print()
tree.insert(Node(3))
tree.printByLevel()
print()
tree.insert(Node(8))
tree.printByLevel()
print()
tree.insert(Node(4))
tree.printByLevel()
print()
tree.insert(Node(5))
tree.printByLevel()
print()
tree.insert(Node(6))
tree.printByLevel()
print()
tree.insert(Node(7))
tree.printByLevel()
print()
tree.insert(Node(1))
tree.printByLevel()
print()
tree.insert(Node(9))

tree.printByLevel()
