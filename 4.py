def outer():
    msg="Hello"
    def inner():
        print(msg)
    return inner
a=outer()
a()

