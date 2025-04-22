peso = float(input(f'Digite o peso: '))
altura = float(input(f'Digite a altura: '))

imc = peso/(altura)**2
print(f'{imc:.1f}')

if imc < 18.6:
    print(f'Abaixo do peso!')

elif imc >= 18.6 and imc <= 24.9:
    print(f'Peso ideal!')

elif imc >= 25 and imc <= 29.9:
    print(f'Levemente acima do peso!')

elif imc >= 30 and imc <= 34.9:
    print(f'Obesidade Grau I!')

elif imc >= 35 and imc <= 39.9:
    print(f'Obesidade Grau II!')

else:
    print(f'Obesidade Grau III!')