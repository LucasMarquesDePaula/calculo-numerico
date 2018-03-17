# Método da Bissecção
# http://conteudo.icmc.usp.br/pessoas/andretta/ensino/aulas/sme0301-1-15/aula8-bisseccao.pdf
# Parâmetros
# fx: Função avaliada
# x0: limite inferior do intervalo avaliado
# x1: limite superior do intervalo avaliado
# e: tolerancia
# iMax: numero máximo de iterações


def run(fx, x0, x1, e, iMax):
    # Inicializa as variaveis
    i = 0
    x = 0
    y = 0
    _x = []
    _y = []
    _i = []

    while True:
        i += 1
        y0 = fx(x0)
        # y1 = fx(x1)

        # Calcula o valor de x
        x = (x0+x1)/2

        # Calcula um valor para f(x)
        y = fx(x)

        # Salva os dados para análise grafica
        _x.append(x)
        _y.append(y)
        _i.append(i)

        # Interrompe a busca caso encontre valores satisfatórios:
        # 1) O intervalo for maior que a tolerância
        # 2) A distancia f(x) e 0 for maior que a tolerância
        if (x1-x0)/2 <= e or abs(y) <= e:
            break

        # Interrompe a busca caso não encontre valores satisfatórios:
        if i >= iMax:
            break

        # Define um novo intervalo
        if y*y0 > 0:
            x0 = x
        else:
            x1 = x

    return [x, y, i, _x, _y, _i]

# Teste
if __name__ == '__main__':
    from math import cos
    from plot import plot

    ret = run(lambda x: x*x*x + 4*x*x - 10, 1, 2, 0, 100)

    plot(ret, 'bisseccao')
