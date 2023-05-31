

# s = input('Enter a string: ')
#
# if s.isdigit():
#     print('It is a number')
# else:
#     if s[0] == '-' or s[0] == '+':
#         if s[1:].isdigit():
#             print('It is a number')
#         else:
#             print('It is not a number')
#     else:
#         print('It is not a number')


def my_function(name: str, price: int, color: str = 'Red'):
    print(f'Color: {color}')
    print(f'Name: {name}')
    print(f'Price: {price}')


# my_function('Audi', 'red', 100) -> positional args
# my_function(price=100, name='Audi', color='red') -> keyword args
# my_function('Audi', color='red', price=100) -> positional + keyword args
# my_function('Audi', color='red', 100) -> SyntaxError: positional argument follows keyword argument
# my_function('Audi', 100) -> optional args (default args)


def calc(a: int, b: int) -> int:
    return a + b


print(calc(2, 4))
