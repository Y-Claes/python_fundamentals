my_str_1 = "Hello World!"
my_str_2 = 'Hello World!'

my_str_3 = """Multiline string"""

# Hoe in een zin " " of '' gebruiken? Tegenovergestelde gebruiken of \ gebruiken

msg_1 = "It's a sunny day"
quote_1 = 'She said, "Hello World!"'

msg_2 = 'It\'s a sunny day'
quote_2 = "She said, \"Hello World!\""

# in operator gebruiken voor iets te zoeken in de string.

my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

# lengte van een string bepalen

print(len(my_str))  # 11

# navigeren van specifieke letter in string

print(my_str[-1])  # d
print(my_str[-2]) # l