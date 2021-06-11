# This program is for playing with python data structures
import sys

string = "This is a string"
print("Hello, World!")
print("the length of the string is " + str(len(string)))
thisset = {"apple", "banana", "cherry"}
print(thisset)
brands = {"Dell", "Apple", "Microsoft", "Lenovo"}
print(brands)
more_brands = {"Nvidia", "Niantic", "Asus", "Dell", 'Dell'}
print(more_brands)

brands.update(more_brands)
print("After update:" + str(brands))

print(more_brands.update(brands))
print(str(more_brands))