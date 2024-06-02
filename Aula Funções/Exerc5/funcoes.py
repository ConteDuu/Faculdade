def area_quadrado():
    medida = float(input('Informe a medido do lado do quadrado: '))
    return medida ** 2


def area_circunferencia():
    raio = float(input('Informe a medido do raio do cículo: '))
    resultado = 3.14 * raio
    return resultado


def area_triangulo():
    base = float(input('Informe a medida da base do triângulo: '))
    altura = float(input('Informe a altura do triângulo: '))
    resultado = (base * altura) / 2
    return resultado
