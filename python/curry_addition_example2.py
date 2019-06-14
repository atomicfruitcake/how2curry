from pymonad import *


@curry
def add_three_nums(a, b, c):
    return a + b + c


add_two_nums_to_5 = add_three_nums(5)
add_num_to_15 = add_two_nums_to_5(10)
result = add_num_to_15(20)
print(result)

if __name__ == "__main__":
    print(add_num_to_15(20))

