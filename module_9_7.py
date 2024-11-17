def is_prime(func):
    def wrapper(a,b,c):
        n = func(a,b,c)
        if n < 2:
            return f'Простое \n{n}'
        for i in range(2, n):
            if n % i == 0:
                return f'Составное \n{n}'
        return f'Простое \n{n}'
    return wrapper

@is_prime
def sum_three(a,b,c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

