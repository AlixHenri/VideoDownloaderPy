#pip install pytube
from pytube import YouTube

print('''PyTube Downloader
[1] Português Brasil
[2] English''')
lang = int(input())

while lang !=1 or lang !=2:
    if lang==1:
        #PT-BR  

        link = input("URL do vídeo: ")
        path = input("Caminho da pasta de download: ")

        yt = YouTube(link)


        print("[1] Baixar Video 🎬")
        print("[2] Baixar Audio 🎵")
        downloadOp = int(input())

        while downloadOp !=1 or downloadOp !=2:

            if downloadOp==1:

                result = {
                    "Título": yt.title,
                    "Número de views": yt.views,
                    "Duração do vídeo": yt.length,
                    "Avaliação do vídeo": yt.rating,
                }

                print(result)
                print('''Qualidade de resolução
[1] Alta
[2] Baixa''')
                resolutionOp=int(input())

                while resolutionOp !=1 or resolutionOp !=2:

                    if resolutionOp==1:

                        yvideo = yt.streams.get_highest_resolution()
                        print("Baixando....")

                        yvideo.download(path)
                        print("Download feito com sucesso!")

                    elif resolutionOp==2:
                        yvideo = yt.streams.get_lowest_resolution()
                        print("Baixando....")

                        yvideo.download(path)
                        print("Download feito com sucesso!")

                    else:
                         print('''Opção Invalida, tente novamQualidade de resol[1] [2] Baixa''')
                    resolutionOp = int(input())

            elif downloadOp ==2:
                yaudio = yt.streams.get_audio_only()
                print("Baixando....")

                yaudio.download(path)
                print("Download feito com sucesso!")
                break
            
            else:
                print("Opção invalida, selecione a opção de download novamente")
                downloadOp = int(input())

    elif lang==2:
        #ENG
        link = input("Video URL: ")
        path = input("Download Path: ")

        yt = YouTube(link)

        print("[1] Download Video 🎬")
        print("[2] Download Audio 🎵")
        downloadOp = int(input())

        while downloadOp !=1 or downloadOp !=2:

            if downloadOp ==1:

                result = {
                    "Título": yt.title,
                    "Número de views": yt.views,
                    "Duração do vídeo": yt.length,
                    "Avaliação do vídeo": yt.rating,
                }

                print(result)

                print(result)
                print('''Resolution quality
[1] High
[2] Low''')
                resolutionOp=int(input())

                while resolutionOp !=1 or resolutionOp !=2:

                    if resolutionOp==1:

                        yvideo = yt.streams.get_highest_resolution()
                        print("Downloading....")

                        yvideo.download(path)
                        print("Download completed succcessfully!")

                    elif resolutionOp==2:
                        yvideo = yt.streams.get_lowest_resolution()
                        print("Downloading....")

                        yvideo.download(path)
                        print("Download completed successfully!")

                    else:
                         print('''Invalid option, try again
Resolution Quality
[1] High
[2] Low''')
                    resolutionOp = int(input())

            elif downloadOp ==2:
                yaudio = yt.streams.get_audio_only()
                print("Downloading audio....")

                yaudio.download(path)
                print("Download completed successfully!")
                break
            
            else:
                print("Invalid option, select a download option again")
                downloadOp = int(input())

    else:
        print('''PyTube Downloader
[1] Português Brasil
[2] English''')
        lang = int(input())