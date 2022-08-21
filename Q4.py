def lerMatriz():
    m, ler_linha = [], input()
    while ler_linha:
        m.append([int(i) for i in ler_linha.split(" ") if i])
        ler_linha = input()
    return m
def escreverMatriz(m):
    for linha in m:
        print(*linha)



matriz = lerMatriz()
cond = True


linhas = len(matriz)
colunas = len(matriz[0])

cond = False
cont = 0

for linha in range(0, linhas):
    cont = 0
    if(cond == False):
        for coluna in range(0, colunas):
            if(cont <= 1):
                if(matriz[linha][coluna] == 1):
                    cont += 1
            else:
                cond = True
                break

    else:
        cond = True
        break

if(cond == True):
    print("NÃO")
else:
    print("SIM")
