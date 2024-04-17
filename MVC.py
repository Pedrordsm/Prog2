import random
import conio

################MODELO#########################
def lepalavras(texto):
    #lê arquivo e retorna uma lista de palavras
    bd = open(texto, "rt")
    lista_palavras = []
    linha = bd.readline()

    while linha != "":
        palavras = linha.strip().split()
        if linha not in lista_palavras:
            lista_palavras = palavras + lista_palavras
        linha = bd.readline()
    bd.close()
    return lista_palavras

def palavras(lista_palavras, n):
    #retorna uma lista com as 5 maiores palavras da lista recebida
    lista_n_palavras = []
    for i in range(n):
        maior = 0
        j = 0
        for palavra in lista_palavras:
            if len(palavra) > maior:
                maior = len(palavra)
                maiorpalavra = palavra
            j += 1
        lista_n_palavras.append(maiorpalavra.upper())
        lista_palavras.remove(maiorpalavra)

    return lista_n_palavras

def geracampo(linhas, colunas):
    #gera matriz
    M = []
    for i in range(linhas):
        lst = []
        for j in range(colunas):
            lst.append("_")
        M.append(lst)
    return M

def letras_aleatorias(c):
    # coloca letras aleatorias na matriz recebida
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(c)):
        for j in range(len(c[0])):
            if c[i][j] == "_":
                c[i][j] = random.choice(letras)
    return c

def posicionar_palavra(c, palavras):
    posicoes = []
    #percorre cada palavra
    for palavra in palavras:
        palavra_correta = False
        # loop para conseguir alocar a palavra sem extrapolar os limites da matriz
        # de todas as maneiras que tentei sem utilizar o break ou continue houveram bugs
        while not palavra_correta:
            direcao = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
            i = random.randint(0, len(c) - 1)
            j = random.randint(0, len(c[0]) - 1)
            pos = random.choice(direcao)
            if 0 <= i + (len(palavra) - 1) * pos[0] < len(c) and 0 <= j + (len(palavra) - 1) * pos[1] < len(c[0]):
                pos_i, pos_j = i, j
                palavra_correta = True
                for letra in palavra:
                    t = (pos_i, pos_j)
                    # condição para se posição já estiver ocupada, a palavra não ser posicionada
                    if c[pos_i][pos_j] != "_" and c[pos_i][pos_j] != letra:
                        palavra_correta = False
                        break
                    posicoes.append(t)
                    pos_i += pos[0]
                    pos_j += pos[1]
            if palavra_correta:
                pos_i, pos_j = i, j
                for letra in palavra:
                    t = (pos_i, pos_j)
                    c[pos_i][pos_j] = letra
                    posicoes.append(t)
                    pos_i += pos[0]
                    pos_j += pos[1]
    return c, posicoes #retorna o campo e as posições das letras

def verificapalavra(c,posij,direcao,palavra,lista_palavras):
    posij_palavra = []
    # para cada palavra verifica a direção que o usuário escolheu 
    # e se a palavra está no campo retorna todas suas coordenadas e a direção
    if palavra in lista_palavras:
        if direcao == "BX":
            t = (1,0)
            i = posij[0]
            j = posij[1]
            if c[i][j] == palavra[0]:
                posij_palavra.append(posij)
                for k in range(len(palavra)-1):
                    i += t[0]
                    j += t[1]
                    posij_palavra.append((i,j))
        elif direcao == "DR":
            t = (0,1)
            i = posij[0]
            j = posij[1]
            if c[i][j] == palavra[0]:
                posij_palavra.append(posij)
                for k in range(len(palavra)-1):
                    i += t[0]
                    j += t[1]
                    posij_palavra.append((i,j))

        elif direcao == "CM":
            t = (-1,0)
            i = posij[0]
            j = posij[1]
            if c[i][j] == palavra[0]:
                posij_palavra.append(posij)
                for k in range(len(palavra)-1):
                    i += t[0]
                    j += t[1]
                    posij_palavra.append((i,j))

        elif direcao == "EQ":
            t = (0,-1)
            i = posij[0]
            j = posij[1]
            if c[i][j] == palavra[0]:
                posij_palavra.append(posij)
                for k in range(len(palavra)-1):
                    i += t[0]
                    j += t[1]
                    posij_palavra.append((i,j))

        elif direcao == "DID":
            t = (1,1)
            i = posij[0]
            j = posij[1]
            if c[i][j] == palavra[0]:
                posij_palavra.append(posij)
                for k in range(len(palavra)-1):
                    i += t[0]
                    j += t[1]
                    posij_palavra.append((i,j))

        elif direcao == "DSD":
            t = (-1,1)
            i = posij[0]
            j = posij[1]
            if c[i][j] == palavra[0]:
                posij_palavra.append(posij)
                for k in range(len(palavra)-1):
                    i += t[0]
                    j += t[1]
                    posij_palavra.append((i,j))
        elif direcao == "DSE":
            t = (-1,-1)
            i = posij[0]
            j = posij[1]
            if c[i][j] == palavra[0]:
                posij_palavra.append(posij)
                for k in range(len(palavra)-1):
                    i += t[0]
                    j += t[1]
                    posij_palavra.append((i,j))

        elif direcao == "DIE":
            t = (1,-1)
            i = posij[0]
            j = posij[1]
            if c[i][j] == palavra[0]:
                posij_palavra.append(posij)
                for k in range(len(palavra)-1):
                    i += t[0]
                    j += t[1]
                    posij_palavra.append((i,j))

        return True, posij_palavra, direcao #retorna True se a palavra está no campo e suas coordenadas
    else:
        return False, [] #retorna False se a palavra não está no campo
##################FIM MODELO##########################

#############VIEW#######################
def exibe_campo(c,posij,palavras):
    #limpa o campo e destaca as coordenadas recebidas
    conio.cls()
    for i in range(len(c)):
        for j in range(len(c[0])):
            if (i,j) in posij:
                print('\033[31m' + c[i][j], end=" " + chr(27) + "[0m")
            else:
                print(c[i][j],end=" ")
        print()
    print("palavras a serem encontradas: ",palavras)
    return c

def encerra_campo(c,posij):
    #limpa o campo e destaca todas as palavras
    conio.cls()
    for i in range(len(c)):
        for j in range(len(c[0])):
            if (i,j) in posij:
                print('\033[31m' + c[i][j], end=" " + chr(27) + "[0m")
            else:
                print(c[i][j],end=" ")
        print()
    print()
    print("Parabéns! Você encontrou todas as palavras")
    return c
################FIM DO VIEW###########################

#######################CONTROLLER#######################
def init(texto, n):
    #chamada das funções do modelo
    lista_palavras = lepalavras(texto)
    maiores_palavras = palavras(lista_palavras,n)
    c = geracampo(30,50)
    c, posicoes = posicionar_palavra(c,maiores_palavras)
    letras_aleatorias(c)
    return c, posicoes, maiores_palavras, []

def run(c, posicoes,lista_palavras):

    print()
    print("\nOnde e qual é a palavra (x, y, direção(Direita = dr, Esquerda = eq, Cima = cm, Baixo = bx, Diagonal Superior Direita = dsd, Diagonal Inferior Direita = did, Diagonal Superior Esquerda = dse, Diagonal Inferior Esquerda = die), palavra) ??: ", end="")
    # interação com o usúario
    tentativa = input().upper().split(",")
    #verifica se o usuário passou a coordenada inicial, a direção e a palavra.
    #retorna True se a palavra está no campo e as coordenadas que ela ocupa
    acertou, coordenadas, direcaocorreta = verificapalavra(c,(int(tentativa[0]),int(tentativa[1])),tentativa[2],tentativa[3],lista_palavras)
    if acertou:
        #destaca as coordenadas da palavra
        posicoes += coordenadas
        lista_palavras.remove(tentativa[3])
        exibe_campo(c,posicoes,lista_palavras)
        print()
        print("Parabéns, você acertou uma palavra! (se a palavra não foi destacada apenas errou a coordenada dela)")
    else:
        #exibe o campo com o que ja foi antes descoberto
        exibe_campo(c,posicoes,lista_palavras)
        print()
        print("\nTente novamente (posiçãoinicial, posiçãofinal, direção, palavra): ", end="")
    #condição para finalizar o jogo 
    if acertou and lista_palavras == []:
        return True

######################FIM DO CONTROLLER############################

