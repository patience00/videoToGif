import os
from pathlib import Path

import cv2

from GifUtil import GifUtil
from FileUtil import FileUtil


class FrameToGif:

    @staticmethod
    def toGif(moviePath=None, createGifPath=None):
        files = FileUtil.all_path(moviePath)
        print("total files:", len(files))
        file_count = 0
        for file in files:
            if file_count < 20000:
                print("file path:", file)
                fileName = file.lstrip(moviePath)
                print("file name:", fileName)
                diction = createGifPath + fileName

                print("mkdir:", diction)
                newPath = Path(diction)
                if newPath.exists():
                    print("folder exist")
                else:
                    os.mkdir(diction)
                    # vc = cv2.VideoCapture("I:\132.mp4")  # 读取视频文件
                    vc = cv2.VideoCapture(file)  # 读取视频文件
                    frame_count = vc.get(cv2.CAP_PROP_FRAME_COUNT)
                    print("frameIndex:", frame_count)

                    c = 0
                    if vc.isOpened():  # 判断是否正常打开
                        rval = True
                    else:
                        rval = False
                        raise Exception("file error")

                    timeF = 1000  # 视频帧计数间隔频率
                    j = 0
                    i = int(frame_count / 5)
                    shotCount = 0
                    frameIndex = 0
                    imagePath = createGifPath + fileName + "\\"
                    while rval:  # 循环读取视频帧
                        rval, frame = vc.read()
                        frameIndex += 1
                        if frameIndex >= i & i <= frame_count:
                            if (i - frameIndex) % 400 == 0:
                                print("current frame:", frameIndex)
                                cv2.imwrite(imagePath + str(frameIndex) + '.jpg', frame)  # 存储为图像
                                shotCount += 1
                            if shotCount > 25:
                                break
                            i += 3000
                    cv2.waitKey(1)
                    vc.release()
                    print("==================================")
                    gifName = diction + '.gif'

                    GifUtil.images2Gif(imagePath, gifName)
                file_count += 1
                print("success")

    @staticmethod
    def videoToGif(moviePath=None, createGifPath=None):
        fileName=os.path.basename(moviePath)
        print("file name:", fileName)
        diction = createGifPath + fileName

        print("mkdir:", diction)
        newPath = Path(diction)
        if newPath.exists():
            print("folder exist")
        else:
            os.mkdir(diction)
            # vc = cv2.VideoCapture("I:\123.mp4")  # 读取视频文件
            vc = cv2.VideoCapture(moviePath)  # 读取视频文件
            frame_count = vc.get(cv2.CAP_PROP_FRAME_COUNT)
            print("frameIndex:", frame_count)

            c = 0
            if vc.isOpened():  # 判断是否正常打开
                rval = True
            else:
                rval = False
                raise Exception("file error")

            timeF = 1000  # 视频帧计数间隔频率
            j = 0
            i = int(frame_count / 5)
            shotCount = 0
            frameIndex = 0
            imagePath = createGifPath + fileName + "\\"
            while rval:  # 循环读取视频帧
                rval, frame = vc.read()
                frameIndex += 1
                if frameIndex >= i & i <= frame_count:
                    if (i - frameIndex) % 400 == 0:
                        print("current frame:", frameIndex)
                        cv2.imwrite(imagePath + str(frameIndex) + '.jpg', frame)  # 存储为图像
                        shotCount += 1
                    if shotCount > 25:
                        break
                    i += 3000
            cv2.waitKey(1)
            vc.release()
            print("==================================")
            gifName = diction + '.gif'

            GifUtil.images2Gif(imagePath, gifName)
        print("success")
