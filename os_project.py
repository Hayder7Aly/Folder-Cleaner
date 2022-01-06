import os
import shutil


path=input("ENTER FILE NAME WHERE YOU WORK ? ")
os.chdir(rf'{path}')

os.mkdir('Files')
os.mkdir('Music')
os.mkdir('Pics')

for item in os.listdir():
    if item.endswith('.txt'):
        shutil.move(item,rf'Files\{item}')

    elif item.endswith('.jpg'):
        shutil.move(item,rf'Pics\{item}')

    elif item.endswith('.mp3'):
        shutil.move(item,rf'Music\{item}')
    else:
        pass




input()

