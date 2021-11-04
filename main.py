import os 
from pytube import Playlist
from pytube import YouTube
import os
import moviepy.editor as mp



p = Playlist('https://www.youtube.com/playlist?list=PLgzTt0k8mXzEwr38NTt-4CgJBAAdhTtOD')
path = r'C:\Users\manue\OneDrive - Instituto Politecnico Nacional\Documents\Pytube'
urls = p.video_urls
contenido = os.listdir(path)
for videos in urls:
    video = YouTube(videos)
    audio = video.streams.filter(file_extension = 'mp4').first()
    audio.download(path)
    print("Cancion descargada")

path2 = 'C:\\Users\\manue\\OneDrive - Instituto Politecnico Nacional\Documents\Pytube\\'
path3 =  'C:\\Users\\manue\\OneDrive - Instituto Politecnico Nacional\Documents\Pytube\\Audio'

directorio = os.listdir(path2)
for mp4 in directorio:

    name = path2 + mp4
    clip = mp.VideoFileClip(name)
    mp3 = mp4
    mp3 = mp3.replace('.mp4','.mp3')
    definitly_name = path3 + mp3
    clip.audio.write_audiofile(definitly_name)