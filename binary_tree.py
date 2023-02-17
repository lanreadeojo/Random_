class Node:
    ''' Binary tree Node'''
    def __init__(self, data):
        self.value = data
        self.left_child = None
        self.right_child = None

class BinaryTree:
    ''' This class represent a binary tree data structure.'''
    def __init__(self, root):
        '''
        :param root: Binary tree node.
        '''
        self.root = Node(root)






tree = BinaryTree("a")
the_root = tree.root
the_root.left_child = Node("b")
the_root.right_child = Node("c")
the_root.left_child.left_child = Node("d")
the_root.right_child.right_child = Node("e")


def breath_first(tree):
    '''
    Breath first search of binary tree print out each node.
    :param tree: binaryTree
    :return:
    '''
    current_level = [tree.root]
    next_level = []
    while current_level:
        for node in current_level:
            print(node.value)
            if node.left_child:
                next_level.append(node.left_child)
            if node.right_child:
                next_level.append(node.right_child)
        current_level = next_level
        next_level = []


breath_first(tree)