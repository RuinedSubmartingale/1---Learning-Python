# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)

# # re-declaring the variable works
f = "abc"
print(f)

# # ERROR: variables of different types cannot be combined
try:
    print("abc" + 123)
except TypeError:
    print("ERROR: variables of different types cannot be combined")
    print("abc" + str(123))


# Global vs. local variables in functions
def some_function():
    f = "def"
    print(f)


some_function()
print(f)

del(f)
try:
    print(f)
except NameError:
    print("del() removes the binding of the argument from the local/global namespace")
