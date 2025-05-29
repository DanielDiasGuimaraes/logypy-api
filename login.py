import requests
import os 
import time



def login():
    from menu import menu_
    from limpa_tela import limpa
    while True:
        print('___________________________________________________________')
        print('#                   LOGYPY - LOGIN 🖥                     #')
        print('___________________________________________________________')
        print('')
        print('')
        #Pegar dados do ususario.

        user = input(' 🔵 Usuario: ')
        password = input(' 🔵 Senha: ')

        #condições
        if not user or not password:
            print('Preencha os campos!')
            time.sleep(1)
            continue
        
        #Declarar http para requisição.
        api_url = 'http://localhost:5000'

        #Mandar dados para API em formato JSON.
        requisicao = requests.post(f'{api_url}/login', json={
            'user': user,
            'password': password
        })
        #Pegar respsota da requisição e colocar em uma variavel
        resposta_de_volta_api = requisicao.json()
        notificar = resposta_de_volta_api['msg']

        if notificar == '1':
            print('')
            print(' ✅ Acesso Liberado.')
            time.sleep(1)
            limpa()
            menu_()
            break
        else:
            print(' ❌ Usuario Invalido.')
            time.sleep(1)
            limpa()
            continue





login()