import time
import random
import requests

def cadastrar_produto():
    from limpa_tela import limpa
    from produtos import produtos

    print('___________________________________________________________')
    print('#       LOGYPY - PRODUTOS - CADASTRAR PRODUTOS 🖥          #')
    print('___________________________________________________________')
    print('')
    print('')
    print(' ⚠ ATENÇÃO : Caso preencher errado cancele no final.')
    print('')
    print('')
    nome = input(' 🔵 Digite o nome do seu produto: ')
    modelo =input(' 🔵 Digite o nome do modelo do produto: ')
    descricao=input(' 🔵 Digite uma descrição para o produto:')
    fabricante = input (' 🔵 Digite o fabricante do produto: ')
    fornecedor = input (' 🔵 Digite o fornecedor do produto: ')
    valor_venda = input (' Valor (R$): ')
    preco = float(valor_venda)
    print('')
    opc = input('⚠ Deseja prosseguir para gerar o codigo do produto ? (S - para sim/ N- para não.): ')

    if opc == 'n':
        limpa()
        return produtos()
    elif opc == 's':
        print('')
        print('👍 Agora o sistema vai gerar um numero que vai ser o codigo do seu produto...')
        time.sleep(1)
        print(' 📝📦 Gerando codigo do produto.')
        time.sleep(1)
        while True:
            codigo = random.randint(1,9999)
            #verificar se ja existe esse codigo no produtos
            
            #Declarar rota http para api
            api_url = 'http://localhost:5000'

            #fazer requisição POST
            resquisicao = requests.post(f'{api_url}/verificar_bd_codigo_produto', json={
                'codigo': codigo
            })
            resposta_api = resquisicao.json()
            msg = resposta_api['msg']

            if msg == '1':
                print(' ❌ Codigo do produto já existe... Gerando outro codigo.')
                time.sleep(1)
                limpa()
                continue
            else:
                print(f' 😀👍 O cofigo do seu produto foi gerado: {codigo}')
                time.sleep(1)
                print(' 📥Iniciando o cadastro no sistema.')
                time.sleep(1)
                #cadastrar o produto:
                
                #Declarar url
                url_cadastro_produto = 'http://localhost:5000'

                #requisição
                resquisicao_para_cadastro = requests.post(f'{url_cadastro_produto}/cadastro_produto', json=({
                    'nome': nome,
                    'modelo': modelo,
                    'descricao': descricao,
                    'fabricante': fabricante,
                    'fornecedor': fornecedor,
                    'codigo': codigo,
                    'preco': preco
                }))
                resposta_api_cadastro = resquisicao_para_cadastro.json()
                resposta = resposta_api_cadastro['msg']

                if resposta == '1':
                    print('')
                    print('✅ Produto cadastrado com sucesso!')
                    input('')
                    limpa()
                    produtos()
                    break
                else:
                    print(' ❌ Error ao cadastrar produto')
                    time.sleep(1)
                    limpa()
                    produtos()
                    break







