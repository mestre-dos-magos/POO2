def main():
    login = input('Inserir Login: ')
    senha = input('Inserir Senha: ')
    if login == senha:
        print('ERRADO! INSIRA NOVAMENTE AS INFOMAÇÕES\nERRO 01: LOGIN E SENHA IDENTICOS')
        return main()
    else:
        print('CERTINHO! Ta cadastrado')

if __name__ == '__main__':
    main()