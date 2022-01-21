# def my_add(a, b):
#     return a + b

# print(my_add(5, 10))
# print(my_add(10, 20))

# def my_multiply(a, b):
#     return a * b

# print(my_multiply(10, 5))

# def f(x):
#     return x**2 - 3*x + 2
# print(f(2))
# print(f(3))

# def f(x):
#     return x**2 - 3*x + 2

# my_xs = [-1, 0, 1, 1.5, 2, 3]

# for ricxvi in my_xs:
#     print(f(ricxvi))


# def double_every_item_in_list(my_list):
#     new_list = []
#     for element in my_list:
#         new_list.append(element * 2)
#     return new_list

# chemi_sia = ["nika", 1, 10, 2.5]

# print(double_every_item_in_list(chemi_sia))

def f(x):
    list = []
    for element in x:
        list.append(element * 2)
    return list

chemi_sia = ["nika", 1, 10, 2.5]
print(f(chemi_sia))