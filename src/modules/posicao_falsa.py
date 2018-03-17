# Método da posição falsa
# http://wwwp.fc.unesp.br/~arbalbo/Iniciacao_Cientifica/zerodefuncoes/algoritmos/posicao_falsa.pdf
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

        # Atribui um valor para x
        x = x0-y0*(x1-x0)/(y1-y0)

        # Calcula um valor para f(x)
        y = fx(x)

        # Salva os dados para análise grafica
        _x.append(x)
        _y.append(y)
        _i.append(i)

        # Interrompe a busca caso encontre valores satisfatórios:
        # 1) O intervalo for maior que a tolerância
        # 3) A distancia entre f(x) e 0 for maior que a tolerância
        if abs(x1-x0) <= e or abs(y) <= e:
            break

        # Interrompe a busca caso não encontre valores satisfatórios:
        if i >= iMax:
            break

        # Define novos valores para busca
        if y0*y1 < 0:
            x0 = x
        else:
            x1 = x
      
    return [x, y, i, _x, _y, _i]

# Teste
if __name__ == '__main__':
    from math import log
    from plot import plot

    ret = run(lambda x: x*log(x) - 1, 1, 10, 0.0, 100)

    plot(ret, 'posicao_falsa')
    