

def excluir_produtos():
    from produtos import produtos
    from limpa_tela import limpa
    import requests
    import time

    while True:
        print('')
        print('___________________________________________________________')
        print('#       LOGYPY - PRODUTOS - EXCLUIR PRODUTOS 🖥           #')
        print('___________________________________________________________')
        print('')
        print('⚠  Use 0 para voltar.')
        print('')
        codigo = input('🔵 Digite o codigo do produto: ')
        print('')
        if codigo and codigo != '0':

            time.sleep(1)
            print('🔎 Buscando produto...')
            time.sleep(1)

            print('')
            api_url = 'http://localhost:5000'
            requisicao = requests.post(f'{api_url}/excluir_produto', json={
                'codigo':codigo
            })

            resposta = requisicao.json()
            resultado = resposta['msg']

            if resultado == '1':
                print('✅ Produto encontrado.')
                time.sleep(1)
                print('')
                print('✅ Produto deletado com sucesso.')
                time.sleep(1)
                limpa()
                continue
            elif resultado == '0':
                print('❌ Produto não encontrado.')
                time.sleep(1)
                limpa()
                continue

        elif codigo == '0':
                limpa()
                produtos()
                break
        else:
            print('❌ Opção Invalida.')
            time.sleep(1)
            limpa()
            continue