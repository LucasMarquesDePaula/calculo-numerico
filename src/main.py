# Exercícios escolidos
# 5.16
# 6.22
# x^10 - 1


from modules import bisseccao, newton_raphson, posicao_falsa, secante, plot

from math import pi


def ex1(x):
    v = 30
    r = 3
    return v-pi*x*x*(3*r-x)/3*2


def ex1_(x):
    r = 3
    return -4*pi*(3*r-x)*x/3+2*pi*x*x/3


def ex2(x):
    a = 0
    return x*x - a


def ex2_(x):
    return 2*x


def ex3(x):
    return x*x*x*x*x*x*x*x*x*x - 1


def ex3_(x):
    return x*x*x*x*x*x*x*x*x


print('')
print('Escolha a funcao:')
print('1) 5.16')
print('2) 6.22')
print('3) x^10 - 1')

f = input()

# valida a funcao escolhida
if f == '1':
    fx = ex1
    f_x = ex1_
    x0 = 0.0001
    x1 = 5.9999
    e = 0.1
    iMax = 200

elif f == '2':
    fx = ex2
    f_x = ex2_
    x0 = 2
    x1 = 4
    e = 0.1
    iMax = 200

elif f == '3':
    fx = ex3
    f_x = ex3_
    x0 = 0.0001
    x1 = 1.3
    e = 0.1
    iMax = 200

else:
    print('Funcao invalida')
    quit()


ret_b = bisseccao.run(fx, x0, x1, e, iMax)
ret_nr = newton_raphson.run(fx, f_x, x0,  e, iMax)
ret_pf = posicao_falsa.run(fx,  x0, x1, e, iMax)
ret_s = secante.run(fx, x0, x1, e, iMax)

plot.multplot(ret_b, ret_nr, ret_pf, ret_s, 'main')


# x0 = float(input('Entre com o inicio do intervalo: '))
# x1 = float(input('Entre com o fim do intervalo: '))

# # Valida o intervalo
# if x0 >= x1:
#     print('Intervalo invalido')
#     quit()

# e = float(input('Entre com a precisão desejada: '))
# # Valida a precisao
# if e < 0:
#     print('Precisao invalida')
#     quit()

# iMax = float(input('Entre com o maximo de iteracoes: '))

# # Valida o numero maximo de iteracoes
# if iMax < 1:
#     print('Numero maximo de iteracoes invalida')
#     quit()
