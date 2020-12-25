import os

import cv2


class FileUtil:
    @staticmethod
    def project_root_path(project_name=None):
        PROJECT_NAME = 'videoToGif' if project_name is None else project_name
        project_path = os.path.abspath(os.path.dirname(__file__))
        root_path = project_path[:project_path.find("{}\\".format(PROJECT_NAME)) + len("{}\\".format(PROJECT_NAME))]
        return root_path

    def get_fileSize(filePath):
        fsize = os.path.getsize(filePath)
        fsize = fsize / float(1024 * 1024)
        return round(fsize, 2)


    def all_path(dirname):
        result = []  # 所有的文件
        for maindir, subdir, file_name_list in os.walk(dirname):
            # print("1:",maindir) #当前主目录
            # print("2:",subdir) #当前主目录下的所有目录
            # print("3:",file_name_list)  #当前主目录下的所有文件
            for filename in file_name_list:
                apath = os.path.join(maindir, filename)  # 合并成一个完整路径
                result.append(apath)
        return result



    def mkdir(path):
        folder = os.path.exists(path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


