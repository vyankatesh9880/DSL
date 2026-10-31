class Node:
    def __init__(self, data):
        self.data = data      # [roll, name, marks]
        self.next = None

def add(head, data):
    new = Node(data)
    new.next = head
    return new

def delete(head, roll):
    prev = None
    p = head
    while p and p.data[0] != roll:
        prev = p
        p = p.next
    if p is None:
        print("Not found")
    elif prev is None:
        head = p.next
    else:
        prev.next = p.next
    return head

def search(head, roll):
    p = head
    while p and p.data[0] != roll:
        p = p.next
    return p

def sort(head, i, order):
    p = head
    while p:
        q = p.next
        while q:
            if (order == 1 and p.data[i] > q.data[i]) or (order == 2 and p.data[i] < q.data[i]):
                p.data, q.data = q.data, p.data
            q = q.next
        p = p.next

def display(head):
    while head:
        print(*head.data)
        head = head.next

head = None
while True:
    print("\n1.Add 2.Delete 3.Update 4.Search 5.Sort 6.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        head = add(head, [int(input("Roll: ")), input("Name: "), int(input("Marks: "))])
    elif ch == 2:
        head = delete(head, int(input("Roll: ")))
    elif ch == 3:
        roll = int(input("Roll: "))
        p = search(head, roll)
        if p:
            p.data = [roll, input("New name: "), int(input("New marks: "))]
        else:
            print("Not found")
    elif ch == 4:
        p = search(head, int(input("Roll: ")))
        if p:
            print(*p.data)
        else:
            print("Not found")
    elif ch == 5:
        i = int(input("0.Roll 2.Marks: "))
        sort(head, i, int(input("1.Asc 2.Desc: ")))
        display(head)
    else:
        break


    
