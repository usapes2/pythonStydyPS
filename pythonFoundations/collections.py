"""
str bytes list dict
"""
# string are immutabe in python
# Read more about Escape Sequences at lexical_analysis.html#strings docs.python.org
# raw strings 
path = r'C:\Users\Merlin\Documets\Spells'
print(path)

# We can create strings using type conversions
st1 = str(123)
print(st1)

# We can access the contents of the string with indexes
print(st1[0])

# We can can check the type with
print(type(st1[0]))

# Methods on strings use help(str) 
c = 'oslo'
print(c.capitalize())
print(c) # strings are immutable so c is not changed

# Unicode is allowed to be written
print('\345')

"""
bytes
"""
b'data'
b"data"

d = b'some bytes' # docs.python.org/3/library/codecs.html#standard-encodings
print(d.split()) # return list of bytes objects
print(d)
# we use decode('utf-8') and encode('urf-8') methods to convert strings and bytes

"""
list
"""
li = [1, 2, 9, 7]
print(li)
li1 = ['a','b','c']
print(li1)

b = [] # empty list

# Lots of list constructors to create lists from other objects
print(list("characters"))

"""
dictionaries
"""

d = {'alice':'773-221-222','bob':'111-222-333',}
print(d['alice'])

cities = ["London","Minsk","Moscow","Chicago"]
for each in cities:
    print(each)

colors = {'crimson': 0xdc143,'coral': 0xff7f50}
for c in colors:
    print(colors[c])


