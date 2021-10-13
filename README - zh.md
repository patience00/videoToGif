# videoToGif
使用Python3截取帧合成为gif图

原本我是使用Java的FFmpegFrameGrabber,如果视频文件太大,会报错:

```
Error on InputStream.reset() or skip(): java.io.IOException: Resetting to invalid mark
```

所以转头使用Python来生成gif

Python可以使用moviepy库的subclip(),但是只能生成某个时间片段的gif,不够灵活

这个脚本是先遍历视频所有帧,跳帧截取生成图片,最后根据图片再合成gif



如何使用:

运行main.py选择视频文件或者视频的目录

