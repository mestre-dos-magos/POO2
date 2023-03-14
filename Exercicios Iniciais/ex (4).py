def main():
    ano, pop_a, pop_b = 0, 80000, 200000
    while pop_a < pop_b:
        pop_a *= 1.03
        pop_b *= 1.015
        ano += 1
    #print(ano)
    return ano

if __name__ == '__main__':
    main()
    