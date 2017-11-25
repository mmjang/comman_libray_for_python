import os
import re

import matplotlib.pyplot as plt
import numpy as np


def read_dat(fname, frame_size = 1326, number_of_points = 640, start_of_signal = 5):
    '''
    读取时域系统 dat 数据
    用法：
        read_dat('test.dat')
    参数：
        fname - 文件名
        frame_size - 帧长度
        number_of_points - 信号点数
        start_of_signal - 信号开始位置
    '''
    f = open(fname, 'rb')
    arr = np.fromfile(f, dtype = np.int16)
    arr = arr.reshape(int(arr.shape[0] / (frame_size / 2)), int(frame_size / 2))
    signal = arr[:, start_of_signal : start_of_signal + number_of_points]
    return signal

def remove_background(data):

    mean = np.mean(data.T, axis = 1)
    return data - mean

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
    signal = read_dat(fname)
    if rmbk:
        out = ax.imshow(remove_background(signal))
    else:
        out = ax.imshow(signal)
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
            im = plot_time_2d(ax, fname, rmbk = rmbk)
            plot.colorbar(im)
            fig.savefig(fname + '.png')
            print('{0} 已绘制并保存'.format(fname))
        except Exception:
            print('{0} 出错'.format(fname))

if __name__ == '__main__':

    name = 'D:\\1123\\20171123174059.dat'
    print(read_dat(name).shape)
