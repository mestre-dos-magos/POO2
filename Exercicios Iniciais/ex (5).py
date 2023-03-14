def main(pop_a=80000, pop_b=200000, tax_a= 1.03, tax_b=1.015, ano_i=0):
    while pop_a < pop_b:
        pop_a *= tax_a
        pop_b *= tax_b
        ano_i += 1
    #print(ano_i)
    return ano_i


if __name__ == '__main__':
    main(pop_a=2000, pop_b=100*1000, tax_a=1.05, tax_b=1.025, ano_i=0)
