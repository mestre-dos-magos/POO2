def main():
    lista = [int(input()) for _ in range(5)]
    soma = sum(lista)
    media = soma/len(lista)
    #print(soma, media)
    return soma, media

if __name__ == '__main__':
    main()
    