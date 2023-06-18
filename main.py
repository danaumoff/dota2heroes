from tkinter import *
import glob
import winsound

root = Tk()
root.title("krutaya dota2")
root.geometry("720x480")
root.resizable(0, 0)
root["bg"] = "lavender"

imgs = []
imgsFiles = []
for imgFile in glob.glob("./img/heroes/*.png"):
    imgs.append(PhotoImage(file=imgFile).subsample(2, 2))
    imgsFiles.append(imgFile)


def getSound(pos):
    # winsound.PlaySound(imgsFiles[pos].replace("img", "sound").replace(".png", ".wav"), winsound.SND_ASYNC)
    print(pos)


xs = 26
ys = 30
c = 0

for i in range(0, len(imgs)):
    hero = Button(image=imgs[i], command=lambda: getSound(imgFile))
    hero.place(x=xs, y=ys)
    xs += 178
    if xs > 560:
        xs = 26
        ys += 102


if __name__ == "__main__":
    root.mainloop()