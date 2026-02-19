def exercicio1():
    print('Exercicio 1')
    numeros = [10, 20, 30, 40, 50]
    print(numeros)
    print("Primeiro número:", numeros[0])
    print("Último número:", numeros[-1])


# 2
def exercicio2():
    print('Exercicio 2')
    nomes = []
    for i in range(3):
        nome = input(f"Digite o {i+1}º nome: ")
        nomes.append(nome)

    print("Lista de nomes:")
    for nome in nomes:
        print(nome)


# 3
def exercicio3():
    print('Exercicio 3')
    valores = [1, 2, 3, 4, 5, 6]
    print(valores)
    print("Tamanho da lista:", len(valores))


# 4
def exercicio4():
    print('Exercicio 4')
    lista = []
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        lista.append(numero)
    print("Lista final:", lista)


# 5
def exercicio5():
    print('Exercicio 5')
    frutas = ["maçã", "banana", "uva", "laranja", "abacaxi"]
    print(frutas)
    fruta = input("Digite uma fruta para remover: ")

    if fruta in frutas:
        frutas.remove(fruta)
        print("Fruta removida!")
    else:
        print("Fruta não encontrada.")

    print("Lista atual:", frutas)


# 6
def exercicio6():
    print('Exercicio 6')
    numeros = []
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)

    soma = sum(numeros)
    print("Soma total:", soma)


# 7
def exercicio7():
    print('Exercicio 7')
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)

    media = sum(notas) / len(notas)
    print("Média:", media)


# 8
def exercicio8():
    print('Exercicio 8')
    numeros = [5, 8, 2, 15, 9]
    print(numeros)
    print("Maior número:", max(numeros))


# 9
def exercicio9():
    print('Exercicio 9')
    numeros = []
    pares = 0

    for i in range(6):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)

        if numero % 2 == 0:
            pares += 1

    print("Quantidade de números pares:", pares)


# 10
def exercicio10():
    print('Exercicio 10')
    nome = str(input("Insira seu nome:"))
    print(f'Seja bem vindo ao Phyton,{nome}!')

#11
def exercicio11():
    print('Exercicio 11')
    n1 = int(input('Insira o primeiro numero:'))
    n2 = int(input('Insira o segundo numero:'))
    soma = n1 + n2
    print(f'A soma é:{soma}')

#12
def exercicio12():
    print('Exercicio 12')
    numeros = [2,4,6,8,12]
    media = sum(numeros) / len(numeros)
    print(media)

#13
def exercicio13():
    print('Exercicio 13')
    num = int(input('Insira um numero para verificar se é impar ou par:'))
    if num % 2 == 0:
        print('Numero par')
    else:
        print('Numero impar')

#14
def exercicio14():
    print('Exercicio 14')
    try:
        num = int(input('Insira um numero inteiro:'))
    except ValueError:
            print('Insira apenas um  numero inteiro valido.')

#15
def exercicio15():
    print('Exercicio 15')
    lista = [80,20,100,200]
    print(lista)
    soma = sum(lista)
    print('A soma da lista é: ', soma)

#16
def exercicio16():
    print('Exercicio 16')
    lista = [2000,578627354,90,300]
    
    print(lista)
    print(max(lista))

#17
def exercicio17():
    print('Exercicio 17')
    lista = [9,6,8,4,9,3,5,2]
    print(lista)
    print(len(lista))

#18
def exercicio18():
    print('Exercicio 18')
    i = 1
    soma = 0
    while i < 4 :
        try:
            nota = float(input(f'insira a nota {i}:'))
            if 0 <= nota <= 10:
                print('Nota adicionada')
                i += 1         
                soma += nota
            else:
                print('Insira um valor valido')
        except ValueError:
            print('Insira apenas numeros')

    media = soma / 3
    print(f'A média é {media:.2f}')

#19
def exercicio19():
    print('Exercicio 19')
    carrinho = []
    intencao = (input('Oque você deseja:\nPressione 1 para adicionar ao carrinho.\nPressione 2 para remover do carrinho.\nResposta:'))
    if intencao == '1':
        carrinho.append(input('Insira o item que deseja adicionar:'))
        
    elif intencao == 2:
            if len(intencao) == '0':
                print("Seu carrinho está vazio.")
            else:
                item = input("Qual item você deseja remover? ")
                if item in intencao:
                    carrinho.remove(item)
                    print("Item removido!")
                
                else:
                    print("Item não encontrado no carrinho.")


#20
def exercicio20():
    print('Exercicio 20')
    lista = []
    while True:
        menu = int(input('\n===MENU===\nDigite 1 para adicionar numero\nDigite 2 para mostrar a lista\nDigite 3 para calcular a media da lista.\nDigite o numero 4 para sair. '))
        if menu == 1:
            quantidade = int(input('Quantos numeros você deseja adicionar?'))
            for i in range(1,quantidade + 1):
                lista.append(int(input(f'Insira o {i}º numero:')))
        elif menu == 2:
            print(lista)
        elif menu == 3:
            if len(lista) > 0:
                media = sum(lista) / len(lista)
                print('A media da lista é: ', media)
            else:
                print('Lista vazia.')
        elif menu == 4:
            print('Você escolheu sair')
            print('Encerrando')
            break
    


# Função Master
def master():
    exercicio1()
    exercicio2()
    exercicio3()
    exercicio4()
    exercicio5()
    exercicio6()
    exercicio7()
    exercicio8()
    exercicio9()
    exercicio10()
    exercicio11()
    exercicio12()
    exercicio13()
    exercicio14()
    exercicio15()
    exercicio16()
    exercicio17()
    exercicio18()
    exercicio19()
    exercicio20()



# Executa tudo
master()