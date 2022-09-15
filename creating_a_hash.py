from os import lseek
from hash_distribution import plot, distribute
from string import printable

def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key). lstrip("'"), 1)
    )

x = hash_function("a"), hash_function("b"), hash_function("c")
print(x)

#plot(distribute(printable, 6, hash_function))