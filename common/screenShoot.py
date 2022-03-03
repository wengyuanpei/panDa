import time
from PIL import ImageGrab
import os

def screenShoot():
    absPath = os.path.abspath('../result')
    nowtime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    print('创建目录时间'+nowtime)
    # print(absPath)
    #创建目录
    pngPath = os.path.join(absPath,'pic_shoot_'+str(nowtime))
    os.mkdir(pngPath)
    print('创建目录'+pngPath)
    #截屏
    shoot=0
    # while shoot <10:
        # 截屏语句很简单的
    im = ImageGrab.grab()
    shoot=shoot+1
    # 保存(图个有png路径或者别的路径需要在这个路径下有这个目录，不然报错，所以我前面是做了规避，没路径我就自己建一个)
    nowtime_s = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    im.save(pngPath+'\%s.png' %(nowtime_s))
    print("截图！"+str(shoot))
        # time.sleep(10)

if __name__=="__main__":
    screenShoot()