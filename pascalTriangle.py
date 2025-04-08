#Representação dos coeficientes das expansões binomiais de ordem 0 até o infinito

def pascal(ordem, cont = 0, lista = [1]):
    #cont será uma variavel para parar a função quando chegar no valor da ordem
    print(lista)

    if cont == ordem:
        return


    listaAux = [1]
    for i in range(len(lista)-1):
        prox = lista[i] + lista[i+1]
        listaAux.append(prox)

    listaAux.append(1)
    
    #Chamada recursiva para preencher a proxima linha
    pascal(ordem, cont+1, listaAux)
