class Node:

    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.data = None


tree = Node()


def Add(number, node):
    if node.right is not None:
        if number >= node.data:
            Add(number, node.right)
            return
    if node.left is not None:
        if number < node.data:
            Add(number, node.left)
            return

    if node.data is None:
        node.data = number
    else:
        newNode = Node()
        newNode.data = number
        newNode.parent = node
        if number >= node.data:
            node.right = newNode
        else:
            node.left = newNode


def FindLeft(node):
    if node.left is None:
        return node
    else:
        return Find(node.left)


def Find(number, node):
    if number == node.data:
        return node

    if number > node.data:
        return Find(number, node.right)
    else:
        return Find(number, node.left)


def Remove(node):
    if node.left is None and node.right is None:
        if node.data > node.parent.data:
            node.parent.right = None
        else:
            node.parent.left = None
        return

    if node.left is None or node.right is None:
        if node.left is not None:
            child = node.left
        else:
            child = node.right
        if node.data > node.parent.data:
            node.parent.right = child
            child.parent = node.parent.right
        else:
            node.parent.left = child
            child.parent = node.parent.left
        return

    if node.right.left is None:
        if node.data > node.parent.data:
            node.parent.right = node.right.left
            node.right.left = node.parent.right
        else:
            node.parent.left = node.right.left
            node.right.left = node.parent.left
        node.right.left = node.left
    else:
        mostleft = FindLeft(node.right)
        node.data = mostleft.data
        Remove(mostleft)


def Clear():
    global tree
    tree = Node()


def Show(node):
    rightdata = ""
    if node.right is not None:
        rightdata = node.right.data
    leftdata = ""
    if node.left is not None:
        leftdata = node.left.data
    print("{} ({}, {})".format(node.data, leftdata, rightdata))
    if node.right is not None:
        Show(node.right)
    if node.left is not None:
        Show(node.left)


action = None
while action != "E":
    action = input("Add(A), Remove(R), Clear(C), Show(S), Exit(E): ")
    if action == "A":
        data = input("Data: ")
        Add(data, tree)

    if action == "R":
        data = input("Data: ")
        node = Find(data, tree)
        Remove(node)

    if action == "C":
        Clear()

    if action == "S":
        Show(tree)