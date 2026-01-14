import time

def somar ( x, y):
    return x + y

def subtrair (x, y):
    return x - y

def dividir (x, y):
    if y == 0:
        print(' Erro; Divisão por 0')
    else:
        return x / y

def multiplicar (x, y):
    return x * y

def menu():
    print('-=-=-=- CALCULADORA -=-=-=-')
    print(' [1] Somar')
    print(' [2] Subtrair')
    print(' [3] Dividir')
    print(' [4] Multiplicar')

def executar():
    menu()
    escolha = input(' Escolha a operação [1/2/3/4]: ')
    print('-=-' * 27)
    if escolha not in '1234':
        print(' -> Opção Inválida!')
        executar()
    try:
        num1 = float(input(' Digite o primeiro número: '))
        print(' ')
        num2 = float(input(' Digite o segundo número: '))
        print(' ')
    except ValueError:
        print(' -> Opção Inválida!')
        return

    if escolha == '1':
        print(f' Conta: {num1} + {num2}')
        print(' ')
        time.sleep(1)
        print(f' Resultado: {somar(num1, num2)}')

    if escolha == '2':
        print(f' Conta: {num1} - {num2}')
        print(' ')
        time.sleep(1)
        print(f' Resultado: {subtrair(num1, num2)}')

    if escolha == '3':
        print(f' Conta: {num1} / {num2}')
        print(' ')
        time.sleep(1)
        print(f' Resultado: {dividir(num1, num2)}')

    if escolha == '4':
        print(f' Conta: {num1} x {num2}')
        print('')
        time.sleep(1)
        print(f' Resultado: {multiplicar(num1, num2)}')
    
    novamente()

def novamente():
    print('-=-' * 27)
    print(' Você deseja usar novamente?')
    print(' [1] Sim')
    print(' [2] Não')
    print('-=-' * 27)

    resposta = input('Resposta: ')
    if resposta == '1':
        executar()
    else:
        print(' Obrigada por usar nossa calculadora!')

if __name__ == '__main__':
    executar()

print('-=-' * 27)
