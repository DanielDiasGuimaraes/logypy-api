import time

def menu_():
    from limpa_tela import limpa
    from produtos import produtos
    while True:
        print('___________________________________________________________')
        print('#                   LOGYPY - MENU 🖥                     #')
        print('___________________________________________________________')
        print('')
        print('')
        print(' 🔙 0. Deslogar')
        print('')
        print(' 🟢 1.Produtos')
        print('')

        opc = input(' 🔵 Digite uma opção: ')

        if opc == '1':
            limpa()
            produtos()
            break
        elif opc == '0':
            limpa()
            return
        else:
            print('❌ Digite uma opção valida.')
            time.sleep(1)
            limpa()
            continue
            

    
