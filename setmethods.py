collection = set()
collection.add(1)
collection.add(2)
collection.add("SR Academy")
collection.add((1, 2, 3,))

collection.remove(1)
collection.clear

print(collection)

collection = {"hello", "academy", "world", "rehmani",}
print(collection.pop())
print(collection.pop())

set1 = {1, 2, 3,}
set2 = {3, 4, 5,}
print(set1.union(set2))

set1 = {1, 2, 3,}
set2 = {3, 4, 5,}
print(set1.intersection(set2))