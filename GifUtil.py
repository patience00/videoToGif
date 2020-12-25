import os

import imageio
from FileUtil import FileUtil


class GifUtil:
    @staticmethod
    def images2Gif(imagePath=None, gif_name=None):
        images = FileUtil.all_path(imagePath)
        frames = []
        for image_name in images:
            frames.append(imageio.imread(image_name))
        imageio.mimsave(gif_name, frames, 'GIF', duration=0.3)
