my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1]) # d

#string slicing, string[start:stop]

print(my_str[1:4]) # ell
print(my_str[:7])  # Hello w
print(my_str[8:])  # rld
print(my_str[8:])  # rld
print(my_str)  # Hello world
print(my_str[:])  # Hello world

# start and stop met een optionele stap parameter, string[start:stop:step]

print(my_str[0:11:2])  # Hlowrd
print(my_str[::-1]) # dlrow olleH
