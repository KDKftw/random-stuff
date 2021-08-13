##starting point of my ytbe download playlist scripts
from pytube import YouTube
path = executable_path=r"C:\Users\KDK\Desktop\ytbe_dnwload"

link = "https://www.youtube.com/watch?v=Sr0jJNCK_J0&list=PLO89I9yaY2tADwKtDXIrPDM6QA7OGX524&index=170&ab_channel=CopyrightFreeTrap"
yt=YouTube(link)
t=yt.streams.filter(only_audio=True).all()
t[0].download(path)