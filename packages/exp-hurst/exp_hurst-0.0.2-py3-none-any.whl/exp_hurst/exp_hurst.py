import numpy as np
from mmq.metodo_minimos_quadrados import mmq # pip install mmq

def hurst(dados: np.ndarray, tipo: str = "pow2") -> float:

    """
    :param dados: Este parâmetro deve estar estruturado como um array
    :param tipo: Este parâmetro deve ser uma string. 
    As opções são "pow2" e "incremental".
    :return: O retorno deverá ser o coeficiente angular da reta média de 
    dados logaritmizados (entropizados)
    """

    if tipo == "pow2":
        binario = f"{len(dados):b}"
        n_passos = len(binario) - 1

        # l = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, len(dados)]
        l = [2 ** (i + 1) for i in range(n_passos)]

        if len(dados) not in l:
            l.append(len(dados))
        
    elif tipo == "inc":

        n_passos = len(dados) - 1

        # l = [2, 3, 4, 5, 6, 7, 8, 9, 10, len(dados)]
        l = range(2, len(dados) + 1)
    else:
        raise ValueError("""Tipo de cálculo não reconhecido. 
                         Escolha entre 'pow2' ou 'inc'.""")
        
    serie1 = np.zeros(shape=n_passos + 1)
    serie2 = np.zeros(shape=n_passos + 1)
    for i, tamanho in enumerate(l):

        serie_aux = dados[:tamanho]
        
        media = serie_aux.mean()
        std = serie_aux.std()

        y = [0]
        for el in serie_aux[:tamanho]:
            el_ant = y[-1]
            y.append(el_ant + el - media)

        y.pop(0)

        range_y = np.max(y) - np.min(y)

        if std != 0:
            serie1[i] = np.log2(tamanho)
            serie2[i] = np.log2(range_y / std)
            serie2[i] = np.log2(range_y / std)
            
            serie2[i] = np.log2(range_y / std)            
            
        
    coef_ang = mmq(entradas=serie1, saidas=serie2, g=1)[0]

    return coef_ang

if __name__ == "__main__":
    dados = np.random.normal(0, 1, 1000)
    tipo = "pow2"
    print(f"O coeficiente de Hurst é: {hurst(dados, tipo=tipo)}")
