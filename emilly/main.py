from produto import Produto
from menu import Menu



while True:
    opcao = int(input('DIGITE UMA OPÇÃO\n1 - ENTRAR NO MENU\n2 - ADICIONAR PRODUTO\n3 - SAIR DO PROGRAMA\n > '))
    if opcao == 1:
        Menu()

    elif opcao == 2:
        resposta2 = 0
        while  resposta2 != 4 :
            print('1 - Pratos\n2 - Bebidas\n3 - Sobremesas')
            tipoProduto = int(input('> '))
            codigo = str(input('Codigo: '))
            nomeProduto = str(input('Nome do seu produto: '))
            precoProduto = str(input('Coloque o preço: '))

            if tipoProduto == 1:
                with open('pratos.txt' 'a') as f:
                    f.write(f'{codigo} :: {nomeProduto} :: {precoProduto} ::\n')
            
            resposta2 = int(input('Deseja adicionar outro produto?\n SIM: 3 NÃO: 4 > '))
            produto = Produto(codigo, nomeProduto, precoProduto)

    elif opcao == 3:
        break