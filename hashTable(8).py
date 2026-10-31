size = 10
table = [None] * size      # None = empty, -1 = deleted

def insert(key):
    i = key % size
    for k in range(size):
        if table[i] is None or table[i] == -1:
            table[i] = key
            return
        i = (i + 1) % size

def search(key):
    i = key % size
    for k in range(size):
        if table[i] is None:
            return -1
        if table[i] == key:
            return i
        i = (i + 1) % size
    return -1

while True:
    print("\n1.Insert 2.Search 3.Delete 4.Display 5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        insert(int(input("Key: ")))
    elif ch == 2:
        pos = search(int(input("Key: ")))
        if pos == -1:
            print("Not found")
        else:
            print("Found at index", pos)
    elif ch == 3:
        pos = search(int(input("Key: ")))
        if pos == -1:
            print("Not found")
        else:
            table[pos] = -1
    elif ch == 4:
        for i in range(size):
            if table[i] is None or table[i] == -1:
                print(i, ": -")
            else:
                print(i, ":", table[i])
    else:
        break



    
