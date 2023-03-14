def main(quantia_num = 10):
    lista = [int(input('Insira um numero inteiro: ')) for _ in range(quantia_num)]
    pares = [i for i in lista if i % 2 == 0]
    impares = [i for i in lista if i % 2 != 0]
    #print(pares, impares, end='\n')
    #print(len(pares), len(impares))
    return len(pares), len(impares)

if __name__ == '__main__':
    main()
    