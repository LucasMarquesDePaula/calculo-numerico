# Método de Newton
# http://conteudo.icmc.usp.br/pessoas/andretta/ensino/aulas/sme0500-1-12/newton.pdf
# Parâmetros
# f: Função avaliada
# f_x: Derivada da função avaliada
# x0: valor inicial para busca
# e: tolerancia
# iMax: numero máximo de iterações


def run(fx, f_x, x0, e, iMax):
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
        y_0 = f_x(x0)

        # Atribui um valor para x
        x = x0-y0/y_0

        # Calcula um valor para f(x)
        y = fx(x)

        # Salva os dados para análise grafica
        _x.append(x)
        _y.append(y)
        _i.append(i)

        # Interrompe a busca caso encontre valores satisfatórios:
        # 1) O intervalo for maior que a tolerância
        # 2) O percentual da diferença for menor que a tolerância
        # 3) A distancia f(x) e 0 for maior que a tolerância
        if abs(x-x0) <= e or abs(x-x0)/abs(x) < e or abs(y) <= e:
            break

        # Interrompe a busca caso não encontre valores satisfatórios:
        if i >= iMax:
            break

        # Define novos valores para busca
        x0 = x

    return [x, y, i, _x, _y, _i]

# Teste
if __name__ == '__main__':
    from math import log
    from plot import plot

    ret = run(lambda x: x*x - 4, lambda x: 2*x, 3, 0.0, 100)

    plot(ret, 'newton_raphson')
