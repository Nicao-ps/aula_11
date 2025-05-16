print(66*'_')
print('\n      *** BEM VINDO AO AUTO ATENDIMENTO DO BANCO CAIXOTE ***      \n')

while True:
    try:
        balance = 1000.0
        print(f'Saldo disponível: R$ {balance:.2f}\n')
        cashout = float(input('Informe valor para saque: '))
        print(66*'_')
    except ValueError:
        print('\nDigite apenas dígitos numéricos.\n')
    else:
        if balance >= cashout:
            balance = balance - cashout
            print('\nOrdem autorizada. Aguarde um momento...\n')
            print('Retire notas disponibilizadas no terminal.\n')
        elif cashout > balance:
            print('\nOrdem negada. Saldo insuficiente.\n')
    finally:
        print(f'Saldo disponível: R$ {balance:.2f}')
        print(66*'_')
        while True:
            new_order = input('\nDeseja realizar outro saque? [s/n]: ')
            match new_order:
                case 's':
                    new_cashout = float(input('\nInforme valor para saque: '))
                    print(66*'_')
                    if balance >= new_cashout:
                        balance = balance - new_cashout
                        print('\nOrdem autorizada. Aguarde um momento...\n')
                        print('Retire notas disponibilizadas no terminal.\n')
                        print(f'Saldo disponível: R$ {balance:.2f}')
                        print(66*'_')
                    elif cashout > balance:
                        print('\nOrdem negada. Saldo insuficiente.\n')
                        print(f'Saldo disponível: R$ {balance:.2f}')
                        print(66*'_')
                case 'n':
                    print('\nAtendimento finalizado.')
                    print(66*'_')
                    break
                case _:
                    print('\nOpção inválida. Informe s ou n.\n')
                    print(66*'_')
    break
