import io
import os.path

from flask import Flask, send_file
from waitress import serve
from ytdlp import yt_download
from ffmpeg import check_ffmpeg, convert_to_dfpwm

app = Flask(__name__)


@app.route("/<ytid>")
def download_and_convert_yt_song(ytid):
    yt_download(ytid)
    convert_to_dfpwm(ytid)
    filepath = os.path.join(os.getcwd(), ytid)
    dfpwm_file = ytid + '.dfpwm'
    if os.path.exists(filepath + '.dfpwm'):
        return_data = io.BytesIO()
        with open(dfpwm_file, 'rb') as fo:
            return_data.write(fo.read())
        return_data.seek(0)
        os.remove(filepath + '.dfpwm')
        os.remove(filepath + '.m4a')
        return send_file(return_data, mimetype='application/octet-stream',
                         download_name=dfpwm_file)
    else:
        return


if __name__ == '__main__':
    check_ffmpeg()
    serve(app, port=5000)
