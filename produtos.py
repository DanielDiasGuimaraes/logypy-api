
import time



def produtos():
    from limpa_tela import limpa
    from menu import menu_
    from cadastrar_produto import cadastrar_produto
    from alterar_dados_produtos import alterar_cadastro_do_produto
    from listar_produto import listar_produto
    from excluir_produto import excluir_produtos

    while True:
        print('___________________________________________________________')
        print('#                   LOGYPY - PRODUTOS 🖥                   #')
        print('___________________________________________________________')
        print('')
        print('')
        print(' 🔙 0. Voltar')
        print('')
        print(' 🟢 1.Cadastrar produto')
        print(' 🟢 2.Alterar dados do produto')
        print(' 🟢 3.Listar produtos')
        print(' 🟢 4.Excluir Produto')
        print('')
        print('')

        opc = input(' 🔵 Digite uma opção: ')

        if opc == '0':
            limpa()
            menu_()
            break
        elif opc == '1':
            limpa()
            cadastrar_produto()
            break
        elif opc == '2':
            limpa()
            alterar_cadastro_do_produto()
        elif opc == '3':
            limpa()
            listar_produto()
        elif opc == '4':
            limpa()
            excluir_produtos()
        else:
            print('❌ Digite uma opção valida.')
            time.sleep(1)
            limpa()
            continue
