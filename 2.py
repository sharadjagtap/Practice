
#Nested functions-definning a function inside another function is called Nested function
#outer is enclosing function
#inner function is nested function
# we can't call inner outside of outer,as inner is local to outer

def outer():
    x=3
    def inner():
        print(x)
    inner()
outer()

# inner()