def main(n):
    valido = 0 <= n <= 10
    if not valido:
        n = int(input('INVALIDO!\nInsira o numero valido: ')) 
        main(n)       

if __name__ == '__main__':
    n = int(input('um valor entre zero e dez: '))
    main(n)
