def fibonacci(n=0):
    if n == 0:
        return 0
    elif n == 1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    i = 0
    while True:
        valor = fibonacci(i)
        if valor < 500:
            print(valor, end=' ')
            i += 1
        else:
            break
