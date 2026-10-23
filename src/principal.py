import numpy as np


def principal(observada, mascara):
    """Completa uma matriz usando a média dos valores conhecidos.

    Esta é uma implementação baseline para validar o contrato do avaliador.
    As estratégias de Álgebra Linear da equipe devem substituir apenas o
    preenchimento das posições ocultas, mantendo esta assinatura e o retorno.
    """
    saida = np.array(observada, dtype=float, copy=True)
    mascara_array = np.asarray(mascara, dtype=bool)
    valores_conhecidos = saida[mascara_array]

    if valores_conhecidos.size:
        estimativa = float(np.mean(valores_conhecidos))
    else:
        estimativa = 0.0

    saida[~mascara_array] = estimativa
    return saida
