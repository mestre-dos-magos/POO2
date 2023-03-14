def main(a=0,b=0):
    if a <= b:
        lista = [i for i in range(a,b+1)]
    else:
        lista = [i for i in range(a,a+1)]
    #print(sum(lista))
    return sum(lista)

if __name__ == '__main__':
    main(1,10)

    