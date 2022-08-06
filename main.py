#pip install pytube

from os import R_OK
from pytube import YouTube

link = input("Digite a URL do vídeo que você deseja baixar: ")
path = input("Digite o caminho onde deseja salvar o vídeo: ")

yt = YouTube(link)

result = {
    "Título": yt.title,
    "Número de views": yt.views,
    "Duração do vídeo": yt.length,
    "Avaliação do vídeo": yt.rating,
}

print(result)

ys = yt.streams.get_highest_resolution()

print("Baixando....")

ys.download(path)
print("Download concluido com sucesso!")