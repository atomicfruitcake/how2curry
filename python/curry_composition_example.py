from pymonad import *

@curry
def add(x, y):
    return x + y

@curry
def multiply(x, y):
    return x * y


double_then_add7 = add(7) * multiply(2)     # 'multiple(2)' is evaluated first, and it's result passed to 'add(7)'
result = double_then_add7(4)                # returns 15 since 4 * 2 = 8, then 8 + 7 = 15
print(result)  # returns 15    

add7_then_double = multiply(2) * add(7)     # 'multiple(2)' is evaluated first, and it's result passed to 'add(7)'
result = add7_then_double(4)                # returns 2 since 4 + 7 = 11, then 2 * 11 = 22
print(result) # returns 22       

if __name__ == "__main__":
    double_then_add7 = add(7) * multiply(2) # 'multiple(2)' is evaluated first, and it's result passed to 'add(7)'
    result = double_then_add7(4)            # returns 15 since 4 * 2 = 8, then 8 + 7 = 15
    print(result)              

    add7_then_double = multiply(2) * add(7) # 'multiple(2)' is evaluated first, and it's result passed to 'add(7)'
    result = add7_then_double(4)            # returns 2 since 4 + 7 = 11, then 2 * 11 = 22
    print(result)              
