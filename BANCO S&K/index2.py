import os

numconta = []
nomconta = []
saldoc = []



def cadastroc(nom, num):
    nomconta.append(nom)
    numconta.append(num)
    saldoc.append(0)

def deletarc(nd):
    if nd in numconta:
        posicao = numconta.index(nd)
        numconta.pop(posicao)
        nomconta.pop(posicao)   
        saldoc.pop(posicao)
        print("A conta foi deletada com sucesso!")
        
    else:
        print("A conta não existe")

def limpar():
    os.system('cls')

def deposito(dpt):
    if dpt in numconta:
        depos = float(input("Digite o valor que você quer depositar: "))
        posicao = numconta.index(dpt)
        saldoc[posicao] = (saldoc[posicao]) + depos
        print("Depósito feito com sucesso")

def saque(sq):
    if sq in numconta:
        saq = float(input("Digite o valor que você quer sacar: "))
        posicao = numconta.index(sq)
        if saldoc[posicao] >= saq:
            saldoc[posicao] = (saldoc[posicao]) - saq
            print("Saque feito com sucesso")
        else:
            print("Saldo insuficiente para saque")

def transferir():

    numcontat1 = int(input("Digite o número da conta de origem: "))
    if numcontat1 not in numconta:
        print("Conta de origem não encontrada")
        

    numcontat2 = int(input("Digite o número da conta de destino: "))
    if numcontat2 not in numconta:
        print("Conta de destino não encontrada")
        

    valort = float(input("Digite o valor a ser transferido: "))
    porigem = numconta.index(numcontat1)
    pdestino = numconta.index(numcontat2)

    if saldoc[porigem] < valort:
        print("Saldo insuficiente para transferência")
    else:
        saldoc[porigem] -= valort
        saldoc[pdestino] += valort
        print("Transferência realizada com sucesso!")

while True:
    limpar()
    print("---------------------- \nEscolha uma opção    - \n1 - Fazer login      - \n2 - Cadastrar        - \n0 - Fechar           - \n----------------------")
    coul = int(input("Digite o que você deseja fazer:"))

    if coul == 1:

        while True:
            limpar()

            print("---------------------- \n0 - Voltar           - \n----------------------")
            
            nomeacesso = input("Digite seu nome de usuário:")
            numeroacesso = int(input("Digite o seu número bancário:"))

            if nomeacesso in nomconta and numeroacesso in numconta:
                limpar()
                print("Login realizado com sucesso!")
                while True:
                    print(f"Bem-Vindo(a) {nomeacesso} -- \nEscolha uma opção    - \n1 - Depositar        - \n2 - Saque            - \n3 - Verificar saldo  -  \n4 - Transferência    -  \n5 - Deletar Conta    -  \n0 - Sair da conta    - \n----------------------")
                    opcao = int(input("Digite uma das opções: "))

                    if opcao == 1:
                        limpar()
                        contad = numeroacesso
                        deposito(contad)

                    elif opcao == 2:
                        limpar()
                        contad = numeroacesso
                        saque(contad)

                    elif opcao == 3:
                        limpar()
                        pesquisars = numeroacesso
                        positions = numconta.index(pesquisars)
                        print("Nome:", nomconta[positions], "\t\t", "Número:", numconta[positions], "\t\t", "Saldo:", saldoc[positions])
                    elif opcao == 4:
                        limpar()
                        transferir()
                    
                    elif opcao == 5:
                        limpar()
                        valord = int(input("Digite o número da conta a ser deletado:"))
                        deletarc(valord)
                        break

                    elif opcao == 0:
                        
                        limpar()
                        print('Até mais, volte Sempre!')
                        break
                    
                    else:
                        limpar()
                        print("Escolha uma opção existente")

            elif nomeacesso == '0':
                limpar()
                print('Até mais, volte Sempre!')
                break


            else:
                limpar()
                print("Usuário Inexistente")
                createaccount = input("Você deseja criar um usuário? (S ou N)")

                if createaccount == "s" or createaccount == "S":
                    limpar()
                    nome = input("Digite seu Nome: ")
                    numero = int(input("Digite o número da sua conta: "))
                    cadastroc(nome, numero)
                else:
                    limpar()
                    print("Tente acessar novamente")

    elif coul == 2:
        limpar()
        print("---------------------- \n0 - Voltar           - \n1 - Continuar        - \n----------------------")
            
        certz = int(input('Deseja continuar a ação:'))
        if certz == 1:
            limpar()
            
            nome = input("Digite seu Nome: ")
            numero = int(input("Digite o número da sua conta: "))
            cadastroc(nome, numero)
            print("Conta cria com sucesso!")

        elif certz == '0':
            limpar()
            break

    elif coul == 0:
        limpar()
        print('Até mais, volte Sempre!')
        break

    else:
        print('Opção invalida, tente novamente!')
