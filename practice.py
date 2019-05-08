'''
Program going through examples of each of the standard python library functions
'''

'''

abs(x)
Return the absolute value of a number. 
The argument may be an integer or a floating point number. 
If the argument is a complex number, its magnitude is returned.
'''
a = -5
print(abs(a)) # Returns 5

'''
all(iterable)
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:
def all(iterable):
    for element in iterable:
        if not element:
            return False
        return True
'''

b = [5.12, 'True', 'Hello']
c = [None, 5.12]

print(all(b))  # Returns True
print(all(c))  # Returns False -> I believe None is not iterable

'''
any(iterable)
Return True if any element of the iterable is true. If the iterable is empty, return False.
Equivalent to:
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
'''

print(any(b))  # True
print(any(c))  # True

'''
ascii(object)
As repr(), return a string containing a printable representation of an object, 
but escape the non-ASCII characters in the string returned by repr() using \\x, \\u or \\U escapes. 
This generates a string similar to that returned by repr() in Python 2.
'''

d = 'A' # Will probably return A because letters are numbers behind the scene in a program.
e = 65   # Might return a letter from the ascii table
print(ascii(d))  # returns 'A'
print(ascii(e))  # returns 65
print(ascii(True))  # Returns True

'''
bin(x)
Convert an integer number to a binary string prefixed with “0b”. 
The result is a valid Python expression. If x is not a Python int object, 
it has to define an __index__() method that returns an integer. Some examples:
'''

print(bin(3))  # will return 0bXXXXX
print(bin(-15))  # Will return -0bXXXX
print(bin(True))  # Not sure what it will return
# bin(True) returned 0b1 so I am assuming Python treats True as 1 behind the scenes
# Let's see bin(False)

print(bin(False))  # 0b0 ???
# It did indeed return 0b0

'''
class bool([x])
Return a Boolean value, i.e. one of True or False. 
x is converted using the standard truth testing procedure. 
If x is false or omitted, this returns False; otherwise it returns True. 
The bool class is a subclass of int (see Numeric Types — int, float, complex). 
It cannot be subclassed further. Its only instances are False and True (see Boolean Values)
'''

# In fact, we see here that bool types are subclasses of int so Python does treat True and False as 1 and 0/
print(bool(True))
print(bool(False))
print(bool(None))  # Returns False interestingly.
print(bool(5))  # Returns True as expected.

print(callable(print()))
print(callable(5))


class Foo:
    def test(self):
        pass


foo = Foo()
print(callable(foo))

