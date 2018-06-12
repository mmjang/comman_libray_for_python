import os
import re

import matplotlib.pyplot as plt
import numpy as np
import scipy.io

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

    '''
    对 read_dat 的结果平均去背景
    '''
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
        # try:
            fig, ax = plt.subplots(1,1)
            im = plot_time_2d(ax, directory + fname, rmbk = rmbk)
            fig.savefig(fname + '.png')
            print('{0} 已绘制并保存'.format(fname))
        # except Exception:
        #     print('{0} 出错'.format(fname))


def position_range_list_to_binary_tag(length, pos_list):
    '''
    将目标位置范围列表转化为 0 1 列表
    length - 0, 1 列表的长度
    pos_list - 目标范围列表 [[a1, a2], [b1, b2]...] 

    例子：
    position_range_list_to_binary_tag(10, 
                                  [
                                      [1,4], [6,8]
                                  ])
    --> [0, 1, 1, 1, 1, 0, 1, 1, 1, 0]
    '''
    result = [0] * length;
    for rng in pos_list:
        for i in range(rng[0], rng[1] + 1):
            result[i] = 1
    return result

def what_label(length, pos_list):
    '''
    将目标位置范围列表转化为 label 列表
    length - 0, 1 列表的长度
    pos_list - 目标范围列表 [[a1, a2], [b1, b2]...] 
    '''
    result = [[0,1]] * length;
    for rng in pos_list:
        for i in range(rng[0], rng[1] + 1):
            result[i] = [1,0]
    return result

import scipy.io

def toNP(x):
    '''
    convert matlab array in python to numpy array
    x is a matlab array;
    returns numpy array
    '''
    return np.array(x._data).reshape(x.size, order='F')

def toMAT(eng, n_array):
    '''
    convert numpy array to matlab array
    eng is the matlab engine in python
    n_array is a numpy array;
    returns matlab array
    '''
    scipy.io.savemat('temp', {'temp': n_array})
    return eng.load('temp.mat')['temp']

if __name__ == '__main__':

    name = 'D:\\1123\\20171123174059.dat'
    print(read_dat(name).shape)
