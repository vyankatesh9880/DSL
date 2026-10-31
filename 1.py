

members = ["Vir", "Siya", "Ravi", "Neha", "Om", "Kiya"]
member_borrow = [3, 0, 5, 2, 0, 4]


books = ["Python", "Java", "C", "DBMS", "OS", "AI"]
book_borrow = [5, 0, 3, 3, 2, 1]


# 1. Average books borrowed per member
total = 0
for x in member_borrow:
    total = total + x
avg = total / len(member_borrow)

# 2. Highest and lowest borrowed book
high = 0
low = 0
for i in range(len(book_borrow)):
    if book_borrow[i] > book_borrow[high]:
        high = i
    if book_borrow[i] < book_borrow[low]:
        low = i

# 3. Count of members who borrowed nothing
zeros = 0
for x in member_borrow:
    if x == 0:
        zeros = zeros + 1

# 4. Most frequently borrowed book (same as the highest borrowed book)
most_book = books[high]

print("Average:", avg)
print("Highest:", books[high], "-", book_borrow[high])
print("Lowest:", books[low], "-", book_borrow[low])
print("Members with 0 books:", zeros)
print("Most frequently borrowed book:", most_book)


print("Time: O(n) for average, highest/lowest, zero count; O(1) for most borrowed")
print("Space: O(1) for all operations")


