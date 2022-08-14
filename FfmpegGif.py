import os
import random
import time
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

import cv2
import ffmpeg
import sys
from GifUtil import GifUtil

from FrameToGif import FrameToGif

savePath = 'F:/video_gif'
# 隔多少帧截取一个片段
frameNumber = 0
# 一个片段中隔多少帧截取
frameJump = 0

totalFrameCount = 0
filePath = ''


def selectPath():
    # 设置窗口标题:
    path_ = askdirectory()
    print('选择的路径', path_)
    path.set(path_)
    print('保存的路径', savePath)


def selectFile():
    global totalFrameCount
    global filePath
    filePath = askopenfilename()
    print('选择的文件:', filePath)
    totalFrameCount = FrameToGif.getFrameCount(filePath)
    Label(window, text='一共' + str(totalFrameCount) + '帧').grid(row=1, column=0)


def startGif():
    global frameNumber
    global frameJump
    global filePath
    global savePath

    print('选择的文件:', filePath)
    print('保存的路径:', savePath)

    frameNumber = int(frameNumber)
    videoToGif(filePath, savePath)
    os.startfile(savePath)


def selectSavePath():
    path_ = askdirectory()
    global savePath
    savePath = path_
    print('保存的路径', savePath)
    Label(window, text=savePath).grid(row=0, column=1)


def read_frame_as_jpeg(in_file, frame_num):
    """
    指定帧数读取任意帧
    """
    out, err = (
        in_file
            .filter('select', 'gte(n,{})'.format(frame_num))
            .output('pipe:', vframes=1, format='image2', vcodec='mjpeg')
            .run(capture_stdout=True)
    )
    return out


def get_video_info(in_file):
    """
    获取视频基本信息
    """
    try:
        probe = ffmpeg.probe(in_file)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        if video_stream is None:
            print('No video stream found', file=sys.stderr)
            sys.exit(1)
        return video_stream
    except ffmpeg.Error as err:
        print(str(err.stderr, encoding='utf8'))
        sys.exit(1)


def videoToGif(moviePath=None, createGifPath=None):
    start = time.time()
    fileName = os.path.basename(moviePath)
    print("file name:", fileName)
    diction = os.path.join(createGifPath, fileName)

    print("mkdir:", diction)
    if os.path.exists(diction):
        print("文件夹已存在")
    else:
        os.mkdir(diction)

    video_info = get_video_info(moviePath)
    total_frames = int(video_info['nb_frames'])
    print("frame_count:", total_frames)

    eachFrameNumber = int(total_frames / 50)
    frameIndex = int(total_frames / 60)
    imagePath = os.path.join(createGifPath, fileName)
    i = 0
    ffmpegInput = ffmpeg.input(moviePath)
    while i < 25:
        frameIndex = random.randint(frameIndex, frameIndex + eachFrameNumber)
        frame = read_frame_as_jpeg(ffmpegInput, frameIndex)
        gifFIle = open(os.path.join(imagePath, str(frameIndex)) + '.jpg', "wb")
        gifFIle.write(frame)
        print('截取帧:', frameIndex)
        i += 1

    print("==================================耗时:%d秒", (time.time() - start))
    gifName = diction + '.gif'
    GifUtil.images2Gif(imagePath, gifName)


if __name__ == '__main__':
    window = Tk()
    window.title('gif转换工具')
    # 更改窗口图标
    window.iconbitmap('123.ico')
    path = StringVar()
    # 第一行
    Label(window, text="gif保存路径:").grid(row=0, column=0)
    Label(window, text=savePath).grid(row=0, column=1)
    Button(window, text="选择目录", command=selectSavePath).grid(row=0, column=2)
    # 按钮
    Button(window, text="选择文件", command=selectFile).grid(row=1, column=2)
    Label(window, text='一共' + str(totalFrameCount) + '帧').grid(row=1, column=0)

    Button(window, text="开始", command=startGif).grid(row=4, column=0)

    window.mainloop()
