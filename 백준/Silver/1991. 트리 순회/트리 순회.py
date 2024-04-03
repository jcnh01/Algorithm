class Node :
    def __init__(self, item, left = None, right = None) :
        self.item = item
        self.left = left
        self.right = right

def preorder(node) :
    print(node.item, end="")
    if node.left != None :
        preorder(tree[node.left])
    if node.right != None :
        preorder(tree[node.right])

def inorder(node) :
    if node.left != None :
        inorder(tree[node.left])
    print(node.item, end="")
    if node.right != None :
        inorder(tree[node.right])

def postorder(node) :
    if node.left != None :
        postorder(tree[node.left])
    if node.right != None :
        postorder(tree[node.right])
    print(node.item, end="")

n = int(input())
tree = {}
for i in range(n) :
    a, b, c = input().split()
    if b == "." :
        b = None
    if c == "." :
        c = None
    tree[a] = Node(a, b, c)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])