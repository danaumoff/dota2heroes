from tkinter import *
import glob
import winsound
from functools import partial

root = Tk()
root.title("krutaya dota2")
root.geometry("720x480")
root.resizable(0, 0)
root["bg"] = "lavender"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

imgs = []
imgsFiles = []
for imgFile in glob.glob("./img/heroes/*.png"):
    imgs.append(PhotoImage(file=imgFile).subsample(2, 2))
    imgsFiles.append(imgFile)


soundsFiles = []
for soundFile in glob.glob("./sound/heroes/*.wav"):
    soundsFiles.append(soundFile)

def getSound(audioFile):
    winsound.PlaySound(audioFile, winsound.SND_ASYNC)

xs = 26
ys = 30
heroBtns = []

for i in range(0, len(imgs)):
    heroBtns.append(Button(image=imgs[i], command=partial(getSound, soundsFiles[i])))

for btn in heroBtns:
    btn.place(x=xs, y=ys)
    xs += 178
    if xs > 560:
        xs = 26
        ys += 102

if __name__ == "__main__":
    root.mainloop()