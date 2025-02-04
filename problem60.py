books = {}
for i in range(5):
    name_a = input("Enter author name: ")
    book_n = input("enter book name: ")
    books[name_a] = book_n

print("Last author is: " + str(list(books.keys())[-1]))
print("Last book is: " + str(list(books.values())[-1]))
print(books)