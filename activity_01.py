while True:
    try:
        n1 = float(input('\nInforme nota 1: '))
        n2 = float(input('\nInforme nota 2: '))
    except ValueError:
        print('\nValor inválido.')
    else:
        if 10.0 >= n1 >= 0.0 and 10.0 >= n2 >= 0.0:
            lenn = (n1 + n2) / 2
            if lenn >= 6.0:
                print(f'\nMédia do aluno: {lenn:.2f}')
                print('\nAprovado!')
                break
            elif lenn < 6.0:
                print(f'\nMédia do aluno: {lenn:.2f}')
                print('\nReprovado!')
                break
        elif n1 < 0 or n2 < 0:
            if n1 < 0 and n2 < 0:
                print('\nValores inválidos. Notas 1 e 2 devem ser maior que 0')
            elif n1 < 0:
                print('\nValor inválido. Nota 1 deve ser maior que 0')
            elif n2 < 0:
                print('\nValor inválido. Nota 2 deve ser maior que 0')
    finally:
        print('\nDesligando...')
