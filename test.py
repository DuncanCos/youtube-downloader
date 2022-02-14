#code by duncanCos

#import lybrary
import os
import subprocess as sp 
import tkinter
from tkinter import filedialog, messagebox

#all the function

def verifUrl():
    url = var_entry.get()
    url = url.split("/")
    if(url[2] == "youtu.be"):
        newUrl = var_entry.get()
    else:
        newUrl = url[3].split("=")
        newUrl = newUrl[1].split("&")
        newUrl = "https://youtu.be/"+newUrl[0]
        
    return newUrl

#function to get the video in 720p
def chooseGoodVideo():
    getDLPlaylist()
    myUrl = verifUrl()
    file_path= tkinter.filedialog.askdirectory()
    
    name = sp.getoutput('youtube-dl --skip-download -e '+myUrl)
    name= name.replace(" ", "_")

    os.system('youtube-dl -o '+file_path+ '/'+name+'.mp4 '+myUrl )
    messagebox.showinfo("telechargement finit", "La video ce trouve dans: " + file_path)


def chooseMusic():
    getDLPlaylist()
    myUrl = verifUrl()
    file_path= tkinter.filedialog.askdirectory()
    
    name = sp.getoutput('youtube-dl --skip-download -e '+myUrl)
    name= name.replace(" ", "_")

    os.system('youtube-dl -x -o '+file_path+ '/'+name+'.mp3 '+myUrl )
    messagebox.showinfo("telechargement finit", "La video ce trouve dans: " + file_path)


def chooseplaylist():
    getDLPlaylist()
    myUrl = verifUrl()
    file_path= tkinter.filedialog.askdirectory()

    name = sp.getoutput('youtube-dl --skip-download -e '+myUrl)
    name= name.replace(" ", "_")

    os.system('youtube-dl  -o '+file_path+ '/'+name+'.mp3 '+myUrl )
    messagebox.showinfo("telechargement finit", "La video ce trouve dans: " + file_path)


def getDLPlaylist():
    myUrl = verifUrl()
    file_path= tkinter.filedialog.askdirectory()
    name = sp.getoutput('youtube-dl --skip-download -e '+myUrl)
    print("name")
    print(name)

#function to erase the video choose entry
def effacer ():
     var_entry.set("")

#initialisation of the UI
app = tkinter.Tk()
app.title("youtube downloader")
app.minsize(300,200)


var_entry= tkinter.StringVar()
url = ""
#creation of entry button and text

#creation of the entry
videoUrl = tkinter.Entry(app, textvariable=var_entry, width=60)

#creation of the button
butonhighvideo = tkinter.Button(app, text="choisir la video en bonne qualité", command=chooseGoodVideo)
butonmusic = tkinter.Button(app, text="choisir la video au format music", command=chooseMusic)
butonplaylist = tkinter.Button(app, text="choisir la playlist", command=chooseplaylist)
butonEfface = tkinter.Button(app, text="X", command=effacer)

#creation of the text
titletext=tkinter.Label(app, text="titre:")
lengthtext=tkinter.Label(app,text="durré de la video: ")



#position of the UI
videoUrl.grid(row=0, column=0)
butonEfface.grid(row=0, column=1)
titletext.grid(row=2, column=0)
lengthtext.grid(row=3, column=0)
butonhighvideo.grid(row=4, column=0)
butonmusic.grid(row=5, column=0)
butonplaylist.grid(row=6, column=0)

app.mainloop() 