from pymonad import *

def add(a, b):   # f(A, B)
    return a + b # -> C


print(add(5, 3)) # prints 8


@curry
def curry_add(a, b):
    return a + b


curry_add5 = curry_add(5) # f(A) ->
result = curry_add5(3)    # g(B) -> C

print(result)             # prints 8


if __name__ == "__main__":

    print(curry_add5(3))



