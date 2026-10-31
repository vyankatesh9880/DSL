salaries = [30000.0, 20000.0, 50000.0, 10000.0, 40000.0, 60000.0, 35000.0]

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_i]:
                min_i = j
        lst[i], lst[min_i] = lst[min_i], lst[i]

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

sel = salaries[:]
bub = salaries[:]

selection_sort(sel)
bubble_sort(bub)

print("Selection sort:", sel)
print("Bubble sort:", bub)

print("Top 5 highest salaries:")
for i in range(1, 6):
    print(sel[-i])





