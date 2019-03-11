def outer():
    state = 10
    def inner():
        return state
    return inner

def adder(x):
    def sum(b):
        return x + b
    return sum

def add10(f):
    def decor(*args):
        return f(*args) + 10
    return decor

def adder(n):
    def service(f):
        def decor(*args):
            return f(*args) + n
        return decor
    return service

@adder(10)
def sum(a, b):
    s = a + b
    return s

s = sum(10, 20, 3)
print(s)
