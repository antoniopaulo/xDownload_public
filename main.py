import sys
from CDownloaderXvideos import DownloaderXvideos
from CDownloaderYouPorn import DownloaderYouPorn
from CDownloaderRedTube import DownloaderRedTube
from CDownloaderPornHub import DownloaderPornHub
from CDownloaderBeeg import DownloaderBeeg
# ordem: servidor, pesquisa, pagina inicial, pagina final, pasta de saida

if len(sys.argv) == 6:
    servidor = str(sys.argv[1])
    pesquisa = str(sys.argv[2])
    pagina_ini = int(sys.argv[3])
    pagina_fin = int(sys.argv[4])
    pasta_saida = str(sys.argv[5])

    if servidor == 'XVideos':
        print("-----------------------------------------------------------")
        print("Servidor: XVideos" )
        print("Pesquisa: " + pesquisa)
        print("Página " + str(pagina_ini) + " até " + str(pagina_fin))
        print("-----------------------------------------------------------")
        puxador = DownloaderXvideos(pasta_saida, pesquisa, pagina_ini, pagina_fin)
        puxador.download()
    elif servidor == 'YouPorn':
        print("-----------------------------------------------------------")
        print("Servidor: YouPorn" )
        print("Pesquisa: " + pesquisa)
        print("Página " + str(pagina_ini) + " até " + str(pagina_fin))
        print("-----------------------------------------------------------")
        puxador = DownloaderYouPorn(pasta_saida, pesquisa, pagina_ini, pagina_fin)
        puxador.download()
    elif servidor == 'RedTube':
        print("-----------------------------------------------------------")
        print("Servidor: RedTube" )
        print("Pesquisa: " + pesquisa)
        print("Página " + str(pagina_ini) + " até " + str(pagina_fin))
        print("-----------------------------------------------------------")
        puxador = DownloaderRedTube(pasta_saida, pesquisa, pagina_ini, pagina_fin)
        puxador.download()
    elif servidor == 'PornHub':
        print("-----------------------------------------------------------")
        print("Servidor: PornHub")
        print("Pesquisa: " + pesquisa)
        print("Página " + str(pagina_ini) + " até " + str(pagina_fin))
        print("-----------------------------------------------------------")
        puxador = DownloaderPornHub(pasta_saida, pesquisa, pagina_ini, pagina_fin)
        puxador.download()
    elif servidor == 'Beeg':
        print("-----------------------------------------------------------")
        print("Servidor: Beeg")
        print("Pesquisa: " + pesquisa)
        print("A página é única para este servidor.")
        print("-----------------------------------------------------------")
        puxador = DownloaderBeeg(pasta_saida, pesquisa, pagina_ini, pagina_fin)
        puxador.download()
    else:
        print('Servidor Inválido')
else:
    print('ERROR: Esperando argumentos...')
