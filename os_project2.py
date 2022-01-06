import os
import shutil

path=input('ENTER PATH WHERE YOU WORK ...... ?  ')
os.chdir(rf'{path}')

os.mkdir('Pics')
os.mkdir('Musics')
os.mkdir('Files')
for item in os.listdir():
    if item.endswith('.jpg'):
        shutil.copy(item,rf'Pics\{item}')
    elif item.endswith('.txt'):
        shutil.copy(item,rf'Files\{item}')
    elif item.endswith('.mp3'):
        shutil.copy(item,rf'Musics\{item}')
    else:
        pass

