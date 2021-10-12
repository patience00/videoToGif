# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from FrameToGif import FrameToGif
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as messagebox


def selectPath():
    # 设置窗口标题:
    path_ = askdirectory()
    print('选择的路径', path_)
    path.set(path_)


def selectFile():
    fileName = askopenfilename()
    print('选择的文件', fileName)
    FrameToGif.videoToGif(fileName, "F:\\video_gif\\")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # FrameToGif.toGif("I:\\", "F:\\video_gif\\")
    # FrameToGif.videoToGif("I:\\porn\\ABP-933.mp4", "F:\\video_gif\\")
    window = Tk()
    window.title('选择文件')
    path = StringVar()
    Label(window, text="目标路径:").grid(row=0, column=0)
    Entry(window, textvariable=path).grid(row=0, column=1)
    Button(window, text="选择文件夹", command=selectPath).grid(row=0, column=2)
    Button(window, text="选择文件", command=selectFile).grid(row=1, column=2)
    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
