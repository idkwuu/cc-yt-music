import subprocess


def check_ffmpeg():
    try:
        subprocess.run(['ffmpeg'])
        return
    except FileNotFoundError:
        exit(1)


def convert_to_dfpwm(ytid):
    m4a_filename = ytid + '.m4a'
    dfpwm_filename = ytid + '.dfpwm'
    subprocess.run(['ffmpeg', '-i', m4a_filename, '-ac', '1', dfpwm_filename, '-y'])
