import os
import subprocess
import time
subprocess.call(["pip", "install", "--upgrade", "pip"])
try:
    subprocess.check_output(
    "pytube --version",
    stderr = subprocess.STDOUT,
    shell= True
    )
except:
    subprocess.call(["pip", "install", "pytube"])
import pytube
from tkinter import *

class Application:
    def __init__(self,master=None):
        self.fontePadrao = ("Arial","10")

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 10
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 20
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.primeiroContainer["pady"] = 10
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.sair = Button(self.quartoContainer, text="Sair")
        self.sair["font"] = ("Calibri", "20")
        self.sair["width"] = 20
        self.sair["fg"] = "red"
        self.sair["command"] = self.primeiroContainer.quit
        self.sair.pack(side=RIGHT)

        self.titulo = Label(self.primeiroContainer, text="Insira o link do vídeo: ")
        self.titulo["font"] = ("Arial", 15,"bold")
        self.titulo.pack()

        self.link = Entry(self.segundoContainer)
        self.link["width"] = 70
        self.link["font"] = self.fontePadrao
        self.link.pack(side=LEFT)

        self.baixar = Button(self.terceiroContainer)
        self.baixar["text"] = "Baixar Música"
        self.baixar["font"] = ("Calibri", "13")
        self.baixar["width"] = 12
        self.baixar["command"]
        self.baixar["command"] = self.searchMusic
        self.baixar.pack()

    def searchMusic(self):
        self.titulo["text"] = "Procurando Música:"
        time.sleep(2)
        videoLink = self.link.get()
        yt = pytube.YouTube(videoLink)
        vids = yt.streams
        parent_dir = r"D:\Bruno\Musics\Pytube"

        for i in range(len(vids)):
            music = vids[i].mime_type
            if (music == "audio/mp4"):
                music = vids[i]
                self.titulo["text"] = "Baixando Música:"
                music.download(parent_dir)
                break
        default_filename = music.default_filename  # get default name using pytube API
        size = len(default_filename)
        new_filename = default_filename[0:(size-4)] + ".mp3"

        subprocess.call(["ffmpeg", "-i",                # or subprocess.run (Python 3.5+)
        os.path.join(parent_dir, default_filename),
        os.path.join(parent_dir, new_filename)
        ])

        full_path = "D:\\Bruno\\Musics\Pytube\\" + default_filename
        os.remove(full_path)

        self.titulo["text"] = "Música Baixada com sucesso"


root = Tk()
root.attributes('-fullscreen',True)
Application(root)
root.mainloop()
