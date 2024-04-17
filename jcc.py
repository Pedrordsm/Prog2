import MVC as mvc
import sys
def main():
    c, posicoes, cinco_maiores, jogadas  = mvc.init(sys.argv[1],int(sys.argv[2])) #arquivo a ser lido e quantidade de palavras
    mvc.exibe_campo(c,jogadas,cinco_maiores)
    while not mvc.run(c,jogadas,cinco_maiores):
        pass
    mvc.encerra_campo(c,posicoes)
# main
main()