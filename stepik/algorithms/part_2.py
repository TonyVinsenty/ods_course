'''
Дано целое число 1 <= n <= 40, необходимо вычислить n-e число Фибоначчи


def fib(n):
    fib_list = [0,  1]
    if n <= 1:
        return fib_list[n]
    else:
        for i in range(2, n + 1):
            fib_n = fib_list[i-1] + fib_list[i-2]
            fib_list.append(fib_n)
        return fib_list[n]
'''   
    
'''
Последняя цифра большого числа Фибоначчи


def fib_digit(n):
    fib_list = [0,  1]
    if n <= 1:
        return fib_list[n]
    else:
        for i in range(2, n + 1):
            fib_n_last_digit = fib_list[i-1]%10 + fib_list[i-2]%10
            fib_list.append(fib_n_last_digit)
        return fib_list[n] % 10
'''

'''
Огромное число Фибоначчи по заданному модулю. 1 <= n <= 10**18, 2 <= m <= 10**5
'''

'''
def fib_mod(n, m):
    fib_list = [0, 1]
    if n <= 1:
        return fib_list[n]
    else:
        for i in range(2, n + 1):
            fib_n_1_module = fib_list[1] % m
            fib_n_2_module = fib_list[0] % m
            fib_n_1 = fib_n_1_module % m
            fib_n_2 = fib_n_2_module % m
            fib_n_module = (fib_n_1 + fib_n_2) % m
            fib_list.append(fib_n_module)
            fib_list.remove(fib_list[0])
        return fib_list[1]


def fib_mod(n, m):
    fib = int((((1 + 5**(1/2))/2)**n - ((1 - 5**(1/2))/2)**n) / 5**(1/2))
    return fib % m
'''


def pizano(n):
    

print(fib_mod(14, 350))
#for i in range(1, 20):
#    print(fib(i))
