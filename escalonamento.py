matriz = list()

linha1 = [2, 2, 1, 1, 7]
linha2 = [1, -1, 2, -1, 1]
linha3 = [3, 2, -3, -2, 4]
linha4 = [4, 3, 2, 1, 12]

matriz.append(linha1)
matriz.append(linha2)
matriz.append(linha3)
matriz.append(linha4)

save = matriz.copy()
shift = 0
mLinhas = len(matriz) - 1
rowGlobal = 0
rowIdx = len(matriz) - 1

while rowGlobal < (len(matriz) - 1):
    constantes = list()
    # criando as constantes
    for shi in range(0, rowIdx):
        const = float(save[rowGlobal + shi + 1][rowGlobal]) / float(save[rowGlobal][rowGlobal])
        constantes.append(const)

    row = rowGlobal
    lAnterior = matriz[row]
    col = 0
    escalonar = 0

    while row < mLinhas:
        linha = matriz[row + 1]
        for idx, ele in enumerate(linha):
            linha[idx] = round(linha[idx] - (constantes[escalonar] * lAnterior[idx]), 2)
        
        row += 1
        escalonar += 1    

    save = matriz.copy()
    shift += 1
    rowGlobal += 1
    rowIdx -= 1

    print("---------------------------------------------------")
    for linha in matriz:
        print('linha: ', linha)

print("---------------------------------------------------")
for linha in matriz:
    print('linha: ', linha)