inicio = 1for c in range(inicio, fim + 1):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
fim = 500
soma = 0



print(f'A soma de todos os números ímpares múltiplos de três de 1 até 500 é {soma}')
