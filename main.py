from tkinter import *
from tkinter import filedialog
from pygame import mixer


def stop():
    mixer.music.stop()


class MusicPlayer:
    def __init__(self, window):
        window.geometry('485x700+290+10')
        root.configure(background = "#333333")
        root.resizable(False,False)
        lower_frame = Frame(root, bg = "#FFFFFF" , width=485 , height =180)
        lower_frame.place(x=0, y=400)
        
        window.title('rockstar music player')
        window.resizable(0, 0)
        Load = Button(window, text='Load', width=10, font=('Times', 10), command=self.load)
        Play = Button(window, text='Play', width=10, font=('Times', 10), command=self.play)
        Pause = Button(window, text='Pause', width=10, font=('Times', 10), command=self.pause)
        Stop = Button(window, text='Stop', width=10, font=('Times', 10), command=stop)
        Load.place(x=0, y=20)
        Play.place(x=110, y=20)
        Pause.place(x=220, y=20)
        Stop.place(x=110, y=60)
        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False


root = Tk()
app = MusicPlayer(root)
root.mainloop()
