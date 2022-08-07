#pip install pytube
#pip install tqdm
from pytube import YouTube
from tqdm import tqdm

link = input("Digite a URL do vídeo que você deseja baixar: ")
path = input("Digite o caminho onde deseja salvar o vídeo: ")

yt = YouTube(link)


print("[1] Baixar Video 🎬")
print("[2] Baixar Audio 🎵")
opcaoDownload = int(input())

while opcaoDownload !=1 or opcaoDownload !=2:

    if opcaoDownload ==1:

        result = {
            "Título": yt.title,
            "Número de views": yt.views,
            "Duração do vídeo": yt.length,
            "Avaliação do vídeo": yt.rating,
        }

        print(result)

        yvideo = yt.streams.get_highest_resolution()
        #Opções de resoluções diferentes para download
        #Opção de baixar apenas audio

        #Barra de progresso - Baixando: [----------]0% - Video Baixado com Sucesso[##########]100%
        #Mensagem de erro - Não foi possivel baixar o video tente novamente
        print("Baixando....")

        yvideo.download(path)
        print("Download feito com sucesso!")

    elif opcaoDownload ==2:
        yaudio = yt.streams.get_audio_only()
        print("Baixando....")

        yaudio.download(path)
        print("Download feito com sucesso!")
        break
    
    else:
        print("Opção invalida, selecione a opção de download novamente")
        opcaoDownload = int(input())