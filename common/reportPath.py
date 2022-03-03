import time
import  os


#############
###报告路径
#############


def reportPath():
    current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    absPath = os.path.abspath('../result')
    print('报告创建时间' + current_time)
    repot_path = os.path.join(absPath, 'interface_report' + str(current_time))

    return  repot_path




