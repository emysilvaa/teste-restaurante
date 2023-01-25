path =  'C:\\Users\\20211174010006\\Documents\\GitHub\\teste-restaurante\\cardapio.txt'
try:
    with open(path, 'r') as f:
        estoque = f.readlines()
except:
    with open(path, 'w') as f:
        f.write('')

class Produto:
    def __init__(self):
        self.estoque = ''
        print('Deseja colocar produtos no seu estoque? ')
        resposta = int(input(' Digite: 1 para SIM e 2 para NÃO: '))
        if resposta == 1:
            r = 0
            while  r != 4 :
                self.codigo = int(input('codigo: '))
                self.nomeProduto = str(input('nome do seu produto: '))
                self.precoProduto = str(input('coloque o preço: '))
                r = int(input('deseja adicionar outro produto? 3 para SIM 4 para NÃO > '))
                with open(path, 'a') as f:
                    f.write(f'{self.codigo} :: {self.nomeProduto} :: R${self.precoProduto}\n')
                with open(path, 'r') as f:
                    self.estoque = f.readlines()
                    
        else:
            print('você saiu da opção de adicionar produtos no estoque.')
    

class Menu(Produto):
    def __init__(self):
        pass
    
    def Organiza_Produtos(self):
        self.nome_menu = input('Por favor informe o tipo do menu: ')
        with open(path, 'a') as f:
            f.write('\n')
        with open(path,'a') as f:
            f.write('{}\n'.format(self.nome_menu))
        
        if self.nome_menu == 'Salgados':
            for c in estoque:
                if 'hamburguer' in c:
                    self.salgados = []
                    self.salgados.append(c)
                    with open(path, 'a') as f:
                        f.write('{}'.format(c))
        
        elif self.nome_menu == 'Bebidas':
            for c in estoque:
                if 'refrigerante' in c or 'suco' in c:
                    self.bebidas = []
                    self.bebidas.append(c)
                    with open(path, 'a') as f:
                        f.write('{}'.format(c))
        else:
            for c in estoque:
                if 'bolo' in c or 'brigadeiro' in c:
                    self.doces = []
                    self.doces.append(c)
                    with open(path, 'a') as f:
                        f.write('{}'.format(c))
        '''
        print('Salgados: {}'.format(self.salgados)) 
        print('Bebidas: {}'.format(self.bebidas))
        
        print('Doces: {}'.format(self.doces))
 '''       '''
cliente = Produto()
'''
cliente = Menu()

cliente.Organiza_Produtos()



