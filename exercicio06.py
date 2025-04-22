salario = 1
cont = 1

minimo = float(input('Digite o salario mínimo atualmente: '))

while salario != 0:
    salario = float(input('Digite seu salário: '))
    divisao = salario/minimo

    if salario == 0:
        print(f'Você é desempregado!')
        cont = cont - 1

    else:
        print(f'O salário é de R${salario}, que equivale a {divisao} salários mínimos!')