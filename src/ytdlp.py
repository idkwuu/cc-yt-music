from yt_dlp import YoutubeDL

ydl_opts = {
    'quiet': True,
    'format': 'm4a/bestaudio',
    'outtmpl': '%(id)s.%(ext)s'
}

ydl = YoutubeDL(ydl_opts)


def yt_download(ytid):
    ydl.download("https://youtube.com/watch?v=" + ytid)
