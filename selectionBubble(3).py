salaries = [30000.0, 20000.0, 50000.0, 10000.0, 40000.0, 60000.0, 35000.0]

def selection_sort(list):
    n = len(list)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]

def bubble_sort(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

sel = salaries[:]
bub = salaries[:]

selection_sort(sel)
bubble_sort(bub)

print("Selection sort:", sel)
print("Bubble sort:", bub)

print("Top 5 highest salaries:")
for i in range(1, 6):
    print(sel[-i])






