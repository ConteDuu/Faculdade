from funcoes import *

print('Para identificação do resultado informe o número correto sendo: 1 para Quadrado, 2 para Cículo, 3 para Retângulo.')
opcao = int(input('Informe o número que necessita: '))
try:
    if opcao == 1:
        resultado = area_quadrado()
        print(f'O área do quadrado é equivalente a: {resultado:.2f}')

    if opcao == 2:
        resultado = area_circunferencia()
        print(f'A área da circunferência é: {resultado:.2f}')

    if opcao == 3:
        resultado = area_triangulo()
        print(f'A área do triângulo corresponde há: {resultado:.2f}')
except:
    print('Numero inválido!')

