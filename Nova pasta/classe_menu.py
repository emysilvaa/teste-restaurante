path1 = 'C:\\Users\\20211174010006\\Documents\\GitHub\\teste-restaurante\\estoque.txt'
path2 = 'C:\\Users\\20211174010006\\Documents\\GitHub\\teste-restaurante\\menu.txt'
try:
    with open(path1, 'r') as f:
        estoque = f.readlines()
except:
    with open(path1, 'w') as f:
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
                self.tipoProduto = input('Digite o tipo do seu produto: ')
                r = int(input('deseja adicionar outro produto? 3 para SIM 4 para NÃO > '))
                with open(path1, 'a') as f:
                    f.write(f'{self.codigo} :: {self.nomeProduto} :: R${self.precoProduto} :: {self.tipoProduto}\n')
                with open(path1, 'r') as f:
                    self.estoque = f.readlines()
                    
        else:
            print('você saiu da opção de adicionar produtos no estoque.')
    

class Menu(Produto):
    def __init__(self):
        self.salgados = []
        self.bebidas = []
        self.doces = []
        self.menu = ''
    
    def Organiza_Produtos(self):
        print('Voc')
        self.nome_menu = input('Por favor informe o tipo do menu: ')
        with open(path2, 'a') as f:
            f.write('\n')
        with open(path2,'a') as f:
            f.write('{}\n'.format(self.nome_menu))
        
        if self.nome_menu == 'Salgados':
            for c in estoque:
                if 'salgado' in c:
                    self.salgados.append(c)
                    with open(path2, 'a') as f:
                        f.write('{}'.format(c))
                    break
        
        elif self.nome_menu == 'Bebidas':
            for c in estoque:
                if 'bebida' in c:
                    self.bebidas.append(c)
                    with open(path2, 'a') as f:
                        f.write('{}'.format(c))
                    break
        
        else:
            for c in estoque:
                if 'sobremesa' in c:
                    self.doces.append(estoque)
                    with open(path2, 'a') as f:
                        f.write('{}'.format(c))
        
        with open(path2, 'r') as f:
            self.menu = f.readlines()
        print({self.salgados})
        print({self.bebidas})
        print({self.doces})
        
    def Remove_Produto(self):
        print('Deseja remover produtos do seu estoque e menu?')
        resposta = int(input(' Digite: 1 para SIM e 2 para NÃO: '))
        if resposta == 1:
            r = 0
            while r != 4:
                self.codigo = input('Informe o código do produto: ')
                for c in estoque:
                    if self.codigo in c:
                        estoque.remove(c)
                        with open(path1, 'w') as f:
                            for c in estoque:
                                if c:
                                    f.write('{}'.format(c))

                for c in self.menu:
                    if self.codigo in self.menu:
                        self.menu.remove(c)       
        
                for c in self.salgados:
                    if self.codigo in c:
                        self.salgados.remove(c)
        
                for c in self.bebidas:
                    if self.codigo in c:
                        self.bebidas.remove(c)
        
                for c in self.doces:
                    if self.codigo in c:
                        self.bebidas.remove(c)
        
                with open(path2,'w') as f:
                    for c in self.menu:
                        if c:
                            f.write({c})
                r = int(input('deseja adicionar outro produto? 3 para SIM 4 para NÃO > '))
        '''
        print({estoque})
        print({self.salgados})
        print({self.bebidas})
        print({self.doces})
        '''
        
            


cliente = Produto()
cliente = Menu()
cliente.Organiza_Produtos()
cliente.Remove_Produto()
