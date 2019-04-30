# Example
# def power(num, n):
#     if n == 1:  # terminating conndition
#         return num
#     else:
#         # calling itself and moving towards closing condition
#         return num * power(num, n-1)


# print(power(2, 3))  # 2 * (3-1)

# CHALLENGE FACTORIALS


def balls(n):
    if n == 1:
        return n
    else:
        return n * (balls(n-1))


print(balls(4))  # 24

# fibonacci


def fib(n):
    if n == 1 or n == 0:
        return n
    elif n > 1:
        return ((fib(n-1)) + (fib(n-2)))


print(fib(8))  # 21
print(fib(0))  # 0
