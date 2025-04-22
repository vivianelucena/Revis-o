while True:
    num = int(input(f'Digite um número: '))
    mod = num % 2

    if mod == 1:
        print(f' O número {num} é ímpar!')
    else:
        print(f' O número {num} é par!')

    if num < 0:
        print(f' O número {num} é negativo!')
    else:
        print(f' O número {num} é positivo!')