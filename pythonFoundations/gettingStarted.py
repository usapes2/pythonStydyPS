"""
Conditional expressions

    if expr:
        print("expr is True")
    else:
        print("espr is False")

"""

# Python provides the elif keyword to elimitate the need for nested if ... else
h = int(input())
if h > 50:
    print("Greater than 50")
elif h < 20:
    print("Less than 20")
else:
    print("Between 20 and 50")
print("\n\n\n")
"""
Whie loops

while c != 0:
    print(c)
    c -= 1
# could be written as

while c:
    print(c)
    c -= 1

"""
c = int(10)
while c:
    print(c)
    c -= 1

