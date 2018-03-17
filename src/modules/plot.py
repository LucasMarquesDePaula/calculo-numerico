import plotly
from plotly.graph_objs import Scatter, Layout

def plot(ret, dst):
    plotly.offline.plot(
        {
            'data': [
                Scatter(x=ret[5], y=ret[3], mode='lines', name='x'),
            ],
            'layout': Layout(title='X')
        },
        filename='./graphs/{0}/x.html'.format(dst)
    )

    plotly.offline.plot(
        {
            'data': [
                Scatter(x=ret[5], y=ret[4], mode='lines', name='y'),
            ],
            'layout': Layout(title='Y')
        },
        filename='./graphs/{0}/y.html'.format(dst)
    )

    out = open('./graphs/{0}/out.txt'.format(dst), 'w')
    out.write('I: %d\nX: %f\nY: %f\n' % (ret[2], ret[0], ret[1]))

    out.write('Iteracao\tX\tY\n')
    for i in range(len(ret[5])):
        out.write('%d\t%f\t%f\n' % (ret[5][i], ret[3][i], ret[4][i]))

    out.close()


def multplot(ret_b, ret_nr, ret_pf, ret_s, dst):
    # X
    plotly.offline.plot(
        {
            'data': [
                Scatter(y=ret_b[3],
                        mode='lines', name='Bisseccao'),
                Scatter(y=ret_nr[3],
                        mode='lines', name='Newton Raphson'),
                Scatter(y=ret_pf[3],
                        mode='lines', name='Posicao Falsa'),
                Scatter(y=ret_s[3],
                        mode='lines', name='Secante')
            ],
            'layout': Layout(
                title='X',
                yaxis=dict(
                    type='log',
                    autorange=True
                )
            )
        },
        filename='./graphs/{0}/x.html'.format(dst)
    )

    # Y
    plotly.offline.plot(
        {
            'data': [
                Scatter(y=ret_b[4],
                        mode='lines', name='Bisseccao'),
                Scatter(y=ret_nr[4],
                        mode='lines', name='Newton Raphson'),
                Scatter(y=ret_pf[4],
                        mode='lines', name='Posicao Falsa'),
                Scatter(y=ret_s[4],
                        mode='lines', name='Secante')
            ],
            'layout': Layout(
                title='Y',
                yaxis=dict(
                    type='log',
                    autorange=True
                )
            )
        },
        filename='./graphs/{0}/y.html'.format(dst)
    )

    # ERRO
    plotly.offline.plot(
        {
            'data': [
                Scatter(y=erro_relativo(ret_b[3]),
                        mode='lines', name='Bisseccao'),
                Scatter(y=erro_relativo(ret_nr[3]),
                        mode='lines', name='Newton Raphson'),
                Scatter(y=erro_relativo(ret_pf[3]),
                        mode='lines', name='Posicao Falsa'),
                Scatter(y=erro_relativo(ret_s[3]),
                        mode='lines', name='Secante')
            ],
            'layout': Layout(
                title='Erro Relativo'
            )
        },
        filename='./graphs/{0}/er.html'.format(dst)
    )

def erro_relativo(_x):
    x_old = 0
    _e = []
    for x in _x:
        _e.append(abs((x-x_old)/x)*100)
        x_old = x

    return _e