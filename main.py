# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from FrameToGif import FrameToGif
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as messagebox

savePath = ''
# 隔多少帧截取图片合成gif
frameNumber = 0
totalFrameCount=0
filePath=''

def selectPath():
    # 设置窗口标题:
    path_ = askdirectory()
    print('选择的路径', path_)
    path.set(path_)
    print('保存的路径', savePath)


def selectFile():
    global frameNumber
    global totalFrameCount
    global filePath
    frameNumber = frame.get()
    filePath = askopenfilename()
    print('选择的文件', filePath)
    print('保存的路径', savePath)
    print('多少帧:', frameNumber)
    frameNumber = int(frameNumber)
    totalFrameCount = FrameToGif.getFrameCount(filePath)
    Label(window, text='一共'+str(totalFrameCount)+'帧').grid(row=1, column=0)

    FrameToGif.videoToGif(filePath, savePath, frameNumber)
    os.system("explorer.exe %s" % savePath)
    os.startfile(savePath)


def savePath():
    path_ = askdirectory()
    global savePath
    savePath = path_
    print('保存的路径', savePath)
    Label(window, text=savePath).grid(row=0, column=1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # FrameToGif.toGif("I:\\", "F:\\video_gif\\")
    # FrameToGif.videoToGif("I:\\porn\\ABP-933.mp4", "F:\\video_gif\\")
    window = Tk()
    window.title('gif转换工具')
    path = StringVar()
    # 第一行
    Label(window, text="gif保存路径:").grid(row=0, column=0)
    Button(window, text="选择目录", command=savePath).grid(row=0, column=2)

    # Label(window, text="目标路径:").grid(row=2, column=0)
    # Entry(window, textvariable=path).grid(row=1, column=1)

    # 第二行
    Label(window, text="隔多少帧截取图片:").grid(row=1, column=0)
    frame = Entry(window)
    frame.grid(row=1, column=1)
    # 按钮
    # Button(window, text="选择文件夹", command=selectPath).grid(row=1, column=2)
    Button(window, text="选择文件", command=selectFile).grid(row=1, column=2)
    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
