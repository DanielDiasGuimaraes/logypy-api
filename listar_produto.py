


def listar_produto():
    from tabulate import tabulate
    import requests
    from limpa_tela import limpa
    from produtos import produtos
    import time

    while True:
        print('')
        print('___________________________________________________________')
        print('#       LOGYPY - PRODUTOS - LISTAR PRODUTOS 🖥            #')
        print('___________________________________________________________')
        print('')
        print('')
        print('')
        url = 'http://localhost:5000'
        requisicao = requests.get(f'{url}/listar_produto')
        data = requisicao.json()

        if data['msg'] == '0':
            print(' ❌ Não há produtos cadastrados.')
            time.sleep(1)
            print('')
            input('Pressione Enter para sair...')
            limpa()
            produtos()
        else:

            cabecalhos = ["Nome", "Modelo", "Descrição", "Fabricante", "Fornecedor", "Código", "Preço",]


            print(tabulate(data['msg'], headers=cabecalhos, tablefmt='grid'))
            print('')
            print('Pressione Enter para sair...')
            input('')
            limpa()
            produtos()
            break