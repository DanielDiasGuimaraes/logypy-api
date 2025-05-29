from limpa_tela import limpa
import time
from produtos import produtos
import requests
from tabulate import tabulate


def alterar_cadastro_do_produto():
    while True:    
        print('')
        print('___________________________________________________________')
        print('#       LOGYPY - PRODUTOS - ALTERAR CADASTRO 🖥           #')
        print('___________________________________________________________')
        print('')
        print(' ⚠ Use 0 para voltar. ')
        print('')
        
        codigo = input(' 🔵 Digite o codigo do produto: ')

        if codigo and codigo != '0':
            url = 'http://localhost:5000'
            requisicao = requests.post(f'{url}/consultar_produto_alterar', json={'codigo': codigo})
            data = requisicao.json()
            if 'msg' in data:
                print('')
                print('❌ Produto não encontrado.')
                time.sleep(1.5)
                limpa()
                continue
            else:
                print(f'✅ Produto encontrado para o código: {codigo}')
                print('')

                nome = data['nome']
                modelo = data['modelo']
                descricao = data['descricao']
                fabricante = data['fabricante']
                fornecedor = data['fornecedor']
                codigo_ = data['codigo']

                tabela = [[nome, modelo, descricao, fabricante, fornecedor, codigo_]]
                headers = ['Nome', 'Modelo', 'Descrição', 'Fabricante', 'Fornecedor', 'Código']

                print(tabulate(tabela, headers=headers, tablefmt='grid'))

                print('')
                
                
        elif codigo == '0':
            limpa()
            produtos()
            break
        else:
            print('⚠ Digite um código válido.')
            time.sleep(1)
            limpa()
            continue
