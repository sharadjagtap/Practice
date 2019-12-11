def outer():
    x=5
    def inner():
        y=10
        result=x+y
        return result
    return inner()
a=outer()
print(a)