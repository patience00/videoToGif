import time

import ffmpeg
import numpy
import cv2
import sys
import random


def read_frame_as_jpeg(in_file, frame_num):
    """
    指定帧数读取任意帧
    """
    out, err = (
        ffmpeg.input(in_file)
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


if __name__ == '__main__':
    start = time.time()
    file_path = 'I:/porn/snis576c.mp4'
    video_info = get_video_info(file_path)
    total_frames = int(video_info['nb_frames'])
    print('总帧数：' + str(total_frames))
    random_frame = random.randint(1, total_frames)
    print('随机帧：' + str(random_frame))
    out = read_frame_as_jpeg(file_path, random_frame)
    image_array = numpy.asarray(bytearray(out), dtype="uint8")
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    cv2.imshow('frame', image)
    cv2.waitKey()
    print('耗时:', time.time() - start)
