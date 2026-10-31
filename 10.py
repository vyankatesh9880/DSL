class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def search(root, data):
    if root is None:
        return False
    if data == root.data:
        return True
    if data < root.data:
        return search(root.left, data)
    return search(root.right, data)

def display(root):
    if root is not None:
        display(root.left)
        print(root.data, end=" ")
        display(root.right)

def smallest(root):
    while root.left is not None:
        root = root.left
    return root

def delete(root, data):
    if root is None:
        return None
    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        small = smallest(root.right)
        root.data = small.data
        root.right = delete(root.right, small.data)
    return root

root = None
while True:
    print("\n1.Insert 2.Delete 3.Display 4.Search 5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        root = insert(root, int(input("Enter value: ")))
    elif ch == 2:
        root = delete(root, int(input("Enter value: ")))
    elif ch == 3:
        display(root)
        print()
    elif ch == 4:
        if search(root, int(input("Enter value: "))):
            print("Found")
        else:
            print("Not found")
    else:
        break


    
