from binarytree import build, Node

def insert(root,key):
    if root is None:
        return Node(key)
    if key is not None:
        if key < root.value:
            root.left = insert(root.left,key)
        else:
            root.right = insert(root.right,key)
    return root
def create():
    root = None
    values = input("Enter the value for bst (use none for empty node):").split()
    for value in values:
        try:
            if value.lower() == 'none':
                key = None
            else:
                key = int(value)
            root = insert(root,key)
        except ValueError:
            print("Invalid value Enter integer value")
    return root
def size(node):
    if node is  None:
        return 0
    return 1 + size(node.left) + size(node.right)
def height(node):
    if node is None:
        return 0
    left = height(node.left)
    right = height(node.right)
    return 1 + max(left,right)
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.value,end="")
        inorder(node.right)
def preorder(node):
    if node is not None:
        
        print(node.value,end="")
        preorder(node.left)
        preorder(node.right)
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.value,end="")

print("Binary Tree Creation")
bst = create()
print(bst)
size = size(bst)
print("Size of the Tree:",size)
height = height(bst) - 1
print("Height of the Tree:",height)
print("Inorder Traversal:", inorder(bst))
print("Preorder Traversal:", preorder(bst))
print("Postorder Traversal:", postorder(bst))
        

