class MyClass:
   ...

def myfunc():
   ...

myint = 777
mystr = "Hello"
myobj = MyClass()

mylst = [
   MyClass, myfunc,
   myint, mystr, myobj
]

# print(*map(callable, [*()]), sep="\n")
print((not len([])))