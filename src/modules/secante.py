# Método da Secante
# http://conteudo.icmc.usp.br/pessoas/andretta/ensino/aulas/sme0100-2-12/aula10-secantes.pdf
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
        y1 = fx(x1)

        # Calcula o valor de x
        x = x1-(y1*(x1-x0))/(y1-y0)

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
        if abs(x1-x0) <= e or abs(x-x0)/abs(x) < e or abs(y) <= e:
            break

        # Interrompe a busca caso não encontre valores satisfatórios:
        if i >= iMax:
            break

        # Define um novo intervalo
        x0 = x1
        x1 = x

    return [x, y, i, _x, _y, _i]

# Teste
if __name__ == '__main__':
    from math import cos
    from plot import plot

    ret = run(lambda x: cos(x)-x, 1, 10, 0, 100)

    plot(ret, 'secante')
    
