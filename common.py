import numpy as np
import matplotlib.pyplot as plt
import os
import re

def plot_time_2d(ax, fname, rmbk = True):
    '''
    绘制时域系统dat数据二维图
    用法:
        fig, ax = plt.subplots(1,1)
        plot_time_2d(ax, '20171123170725.dat')
        fig.show()
    参数:
    fname - dat 文件名
    rmbk - 是否去背景
    save_fig - 是否保存图片
    '''
    frame_size = 1326
    f = open(fname,'rb')
    arr = np.fromfile(f, dtype=np.int16)
    arr = arr.reshape(int(arr.shape[0]/ (frame_size/2)),int(frame_size /2))
    signal = arr[:,5:5+640]
    mean = np.mean(signal.T,axis=1)
    if rmbk:
        out = ax.imshow(arr[:,5:5+ 640] - mean)
    else:
        out = ax.imshow(arr[:,5:5+ 640])
    return out

def plot_all_in_directory(directory, rmbk = True):
    '''
    对于时域系统dat数据文件，绘制并保存 directory 文件夹下的所有 dat 文件，默认去直达波
    directory - 文件夹路径
    rmbk - 是否去直达波
    '''
    plt.ioff()
    for fname in [f for f in os.listdir(directory) if re.match(r'[0-9]+\.dat$', f)]:
        try:
            fig, ax = plt.subplots(1,1)
            plot_time_2d(ax, fname, rmbk = rmbk)
            fig.savefig(fname + '.png')
            print('{0} 已绘制并保存'.format(fname))
        except Exception:
            print('{0} 出错'.format(fname))

