'''
After running the code you'll see a window
where you should insert the URL-address of a YouTube video.
After that you should press the 'Download' button.
The downloading process will be shown in the shell window of your IDE.
After downloading you'll hear 'Download complete!'.
'''

import youtube_dl  # Library for downloading from YouTube
import PySimpleGUI as sg  # Library for the interface
from playsound2 import playsound  # Library for playing sounds

# Interface
sg.theme('DarkBlue3')
layout = [[sg.Text('Video URL'), sg.InputText()],
          [sg.Button('Download'), sg.Button('Exit')]]
window = sg.Window('YouTube Downloader', layout, icon = 'icon.ico')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    # Downloading video from YouTube and saving it in the program folder
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([values[0]])  # The 'value' comes from sg.InputText
    playsound('Download Complete.wav')
    
window.close()
