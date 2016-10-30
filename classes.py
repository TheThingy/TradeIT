#! /usr/bin/env python3


# Define class Foo
class Foo:
    # __init__() is run when Foo() is initialized
    def __init__(self, text):
        # hello is stored in instance of class referenced by the self parameter
        self.hello = text
        # not_hello is not stored and will be deleted
        not_hello = "hade"
    
    def bar(self, text):
        # Print hello variable which is stored in the self parameter
        print(self.hello, end=" ")
        
        # Print text parameter
        print(text)
        

# Define another class FooBar
class FooBar:
    def __init__(self):
        self.hello = "God dag"


# Create an instance of class Foo
a = Foo("hi")

# Print "hi" from the instance of Foo
print(a.hello)

# Print "hi world"
a.bar("world")
Foo.bar(a, "world") # This is the same


# Foo does not need to be initialized to use its functions
Foo.bar(a, "world") # Prints "hi world"
Foo("hello").bar("world") # Prints "hello world"

# Foo.bar does not even require the "self" parameter to be an instance of same class
b = FooBar()
Foo.bar(b, "world") # Prints "God dag world"
