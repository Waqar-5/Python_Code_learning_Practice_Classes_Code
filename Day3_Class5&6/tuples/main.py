# Tuple Properties (Recap)
# Creating Tuples
empty = ()
single = (5,)
multi = (1, 2, 3, "Hello", 3.12)

print("empty tuple: ",empty)
print("single tuple: ",single)
print("multi tuple: ",multi)


# Indexing
print("indexing: ",multi[0])      # 1
print("negative indexing: ",multi[-1])     # 3.14


# Slicing
print("slicing: ",multi[1:4])    # (2, 3, 'hello')

# Length
print(len(multi))    # 5


print("*************************************")
# All Tuple Methods in Python

# Tuple Methods with Examples — 4 Each
#  count()
letters = ("a", "b", "a", "c", "a")
print(letters.count("a"))    # 3
print("******************************************")
# index()

langs = ("Python", "Java", "C++")
print(langs.index("Java"))  # 1