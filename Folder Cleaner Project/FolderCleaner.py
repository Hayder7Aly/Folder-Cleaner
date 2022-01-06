import os,shutil
os.chdir(r'F:\harry_programmes\MiniProject OsModule\Folder Cleaner Project\Demo')

# import pandas as pd

def CreateFolderExits(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def FolderCleaner(path):
    os.chdir(path)
    files = os.listdir()

    CreateFolderExits('Text Files')
    CreateFolderExits('PhotosImages')
    CreateFolderExits('VediosAudios')
    CreateFolderExits('Programmes')
    CreateFolderExits('Mixer')

    txt,photo,audio_vedio,programme,other=0,0,0,0,0
    for file1 in files:
        if file1.endswith('.txt') or file1.endswith('.win'):
            shutil.move(file1,rf"Text Files/{file1}")
            txt+=1
        elif file1.endswith('.png') or file1.endswith('.jpg'):
            shutil.move(file1,rf"PhotosImages/{file1}")
            photo+=1
        elif file1.endswith('.mp3') or file1.endswith('.mp4') or file1.endswith('.mkv'):
            shutil.move(file1,rf"VediosAudios/{file1}")
            audio_vedio+=1
        elif file1.endswith('.py') or file1.endswith('.js') or file1.endswith('.html'):
            shutil.move(file1,rf"Programmes/{file1}")
            programme+=1
        else:
            if os.path.isfile(file1):
                shutil.move(file1,rf"Mixer/{file1}")
                other+=1
    print(f"Text Files Move : {txt}\nVedio And Audio Files Move : {audio_vedio}\nProgrammes Files Move : {programme}\nPhoto and Image Files Move : {photo}\nOther Files Move : {other}")

if __name__ == "__main__":

    path=input('Please Enter The Path Of your Computer For Cleaner the Folder ? \n')
    FolderCleaner(path)


