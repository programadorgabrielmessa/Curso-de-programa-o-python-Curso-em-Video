'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
'''
'''
Digite um numero de qualquer tabuada e saberá ela
'''''

numero = int(input('numero:'))
for i in range (numero,10,1):
    resultado = numero * b
print(f'Ha tabuada do {i} 9')
print(f' {numero} * {i}')


# Solicita ao usuário que insira um número
numero = int(input("Digite um número para ver a sua tabuada: "))

# Utiliza um laço for para calcular e mostrar a tabuada
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
