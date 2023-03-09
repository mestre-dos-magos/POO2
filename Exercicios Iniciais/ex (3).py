def val_nome(nome):
    return len(nome) >= 3

def val_idade(idade):
    return 0 <= idade <= 150

def val_salario(salario):
    return salario >= 0

def val_sexo(sex):
    return sex in ('f', 'm', 'n')

def val_civil(civil):
    return civil in ('s', 'c', 'v', 'd')

def main():
    nome = input('Nome: ')
    print(val_nome(nome))
    idade = int(input('Idade: '))
    print(val_idade(idade))
    salario = float(input('Salario: '))
    print(val_salario(salario))
    sexo = input('Sexo: ')
    print(val_sexo(sexo) )
    civil = input('estado civil: ')
    print(val_civil(civil))

if __name__ == '__main__':
    main()
    