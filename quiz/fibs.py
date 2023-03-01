def sum_of_even_fibonacci(n):

    sum = 0
    a, b = 0, 1
    while b < n:
        if b % 2 == 0:
            sum += b
        a, b = b, a + b
    return sum

print(sum_of_even_fibonacci(4000000))