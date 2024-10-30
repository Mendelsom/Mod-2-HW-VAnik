number_ = int(input('Введите число n '))
def fibo_(n):
    if (n == 0):
        return 1
    if (n == 1):
        return 1
    else:
        return n + fibo_(n-1)
print(f' Fibo(N) = {fibo_(number_)}')

