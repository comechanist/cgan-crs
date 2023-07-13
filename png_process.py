import os

class ImageRename():
    def __init__(self):
        self.path = 'E:/照片/hxy_DATA/dataset/test_label'

    def rename(self):
        filelist = os.listdir(self.path)
        totalnum = len(filelist)

        i = 1

        for item in filelist:
            if item.endswith('.png'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(
                    self.path), '0001' + format(str(i), '0>3s') + '.jpg')
                os.rename(src, dst)
                i = i + 1


if __name__ == '__main__':
    newname = ImageRename()
    newname.rename()