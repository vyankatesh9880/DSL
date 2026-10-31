table = [[] for i in range(10)]

def insert(key, value):
    table[key % 10].append([key, value])

def search(key):
    for pair in table[key % 10]:
        if pair[0] == key:
            return pair[1]
    return None

def delete(key):
    for pair in table[key % 10]:
        if pair[0] == key:
            table[key % 10].remove(pair)
            return True
    return False

while True:
    print("\n1.Insert 2.Search 3.Delete 4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        insert(int(input("Key: ")), input("Value: "))
    elif ch == 2:
        value = search(int(input("Key: ")))
        if value:
            print("Value:", value)
        else:
            print("Not found")
    elif ch == 3:
        if delete(int(input("Key: "))):
            print("Deleted")
        else:
            print("Not found")
    else:
        break



