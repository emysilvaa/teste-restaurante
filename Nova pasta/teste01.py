path = 'C:\\Users\\emill\\codiguin da emy\\menu.txt'
try:
    with open(path, 'r') as f:
        dados = f.readlines()
except:
    with open(path, 'w') as f:
        f.write('')

class Restaurante:
    def __init__(self, nome):
        self.nome = nome

class Menu(Restaurante):
    def __init__(self, nome):
        super().__init__(nome)
    
    def inserirProduto(self):
        print('você deseja inserir seus produtos? ')
        resposta = int(input('Digite 1 para inserir e 2 para sair desta função > '))
        if resposta == 1:
            print('para parar de adicionar produtos digite: "parar"')
            inserir = 0
            while inserir != 'parar':
                inserir = str(input('Insira aqui seus produtos > '))
        else:
            print('você encerrou a função de adicionar seus produtos! ')
            


    def alterarProduto():
        pass

    def removerProduto():
        pass

class Cliente:
    def __init__(self, nome, mesa):
        self.nome = nome
        self.mesa = mesa
    
    def realizarPedido():
        pass

    def fecharPedido():
        pass

###############################################################
miramar = Restaurante('Miramar')
miramar = Menu('Miramar')
miramar.inserirProduto()
