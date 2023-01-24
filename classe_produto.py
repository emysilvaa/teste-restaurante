path = 'C:\\Users\\20211174010006\\Desktop\\teste03\\cardapio.txt'
try:
    with open(path, 'r') as f:
        estoque = f.readlines()
except:
    with open(path, 'w') as f:
        f.write('')

class Produto:
    def __init__(self):
        print('Deseja colocar produtos no seu estoque? ')
        resposta = int(input(' Digite: 1 para SIM e 2 para NÃO: '))
        if resposta == 1:
            r = 0
            while  r != 4 :
                self.codigo = str(input('codigo: '))
                self.nomeProduto = str(input('nome do seu produto: '))
                self.precoProduto = str(input('coloque o preço: '))
                r = int(input('deseja adicionar outro produto? 3 para SIM 4 para NÃO > '))
                with open(path, 'a') as f:
                    f.write(f'{self.codigo} :: {self.nomeProduto} :: R${self.precoProduto}\n')
                with open(path, 'r') as f:
                    self.estoque = f.readlines()
        print('você saiu da opção de adicionar produtos no estoque.')
        print(self.estoque)


produtos = Produto()

