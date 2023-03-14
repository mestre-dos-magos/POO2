def fatorial(n=0):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fatorial(n-1)

if __name__ == '__main__':
    print(fatorial(10))
    