#pip install pytube
from pytube import Playlist

p = Playlist('playlist link on your youtube channel or others')

DOWNLOADFOLDER = "Directory"

for video in p.videos:
    video.streams.get_by_itag(140).download(DOWNLOADFOLDER)


print('end')
