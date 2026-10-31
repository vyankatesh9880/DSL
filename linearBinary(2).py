
ids = [77, 98, 105, 150, 230, 310, 412, 500]   

def linear_search(myList, key):
    for i in range(len(myList)):
        if myList[i] == key:
            return i
    return -1

def binary_search(myList, key):
    low = 0
    high = len(myList) - 1
    while low <= high:
        mid = (low + high) // 2
        if myList[mid] == key:
            return mid
        elif key < myList[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

key = int(input("Enter ID: "))

print("Linear:", linear_search(ids, key))
print("Binary:", binary_search(ids, key))






