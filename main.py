import os #importar la liberia del sistema
from pytube import Playlist #importar para usar la playlist
from pytube import YouTube #importar para usar Youtube y descar
import moviepy.editor as mp #Libreria para cambiar el formato mp4 a mp3



p = Playlist('https://www.youtube.com/playlist?list=PLgzTt0k8mXzEwr38NTt-4CgJBAAdhTtOD') #Url de playlist
path = r'C:\Users\manue\OneDrive - Instituto Politecnico Nacional\Documents\Pytube' #lughar en donde se va a descargar
urls = p.video_urls #Obtienes el url de todos los videos de la Playlist
contenido = os.listdir(path) # hace una variable para guardar el fichero de la carpeta de descarga
for videos in urls:  #iteras en cada uno de los links que guarda urls
    video = YouTube(videos) #lo convertimos de str a links de yotubue
    audio = video.streams.filter(file_extension = 'mp4').first() #obtenemos solo el video
    audio.download(path) #descargamos en el path indicado
    print("Cancion descargada")

path2 = 'C:\\Users\\manue\\OneDrive - Instituto Politecnico Nacional\Documents\Pytube\\'
path3 =  'C:\\Users\\manue\\OneDrive - Instituto Politecnico Nacional\Documents\Pytube\\Audio' #path modificado

directorio = os.listdir(path2) 
for mp4 in directorio:

    name = path2 + mp4
    clip = mp.VideoFileClip(name)
    mp3 = mp4
    mp3 = mp3.replace('.mp4','.mp3')
    definitly_name = path3 + mp3
    clip.audio.write_audiofile(definitly_name)