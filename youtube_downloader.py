from __future__ import unicode_literals
import os
import youtube_dl

videos = [ "https://www.youtube.com/watch?v=IeuQW3DRVQ0" ]

ydl_opts = {
    'format': 'best',
    "keepvideo": True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    "writeautomaticsub" : True,
    "sub-format": "ttml",
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    result = ydl.download(['https://www.youtube.com/watch?v=IeuQW3DRVQ0'])
