import collections


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def minimum_level_sum(root):

    def rec_level_sum(root, dict, level = 0):
        if not dict[level]:
            dict[level] = 0

        dict[level] += root.val

        if root.left:
            rec_level_sum(root.left, dict, level+1)

        if root.right:
            rec_level_sum(root.right, dict, level+1)

    dict = collections.defaultdict()
    result = rec_level_sum(root, dict)

    print(result)

    return


#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print(minimum_level_sum(node))
