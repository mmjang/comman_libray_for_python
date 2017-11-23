def plot_time_2d(fname, rmbk = True, save_fig = False):
    '''
    绘制时域系统dat数据二维图
    plot_time_2d(fname, rmbk = True, save_fig = False)
    fname - dat 文件名
    rmbk - 是否去背景
    save_fig - 是否保存图片
    '''
    f = open(fname,'rb')
    arr = np.fromfile(f, dtype=np.int16)
    arr = arr.reshape(int(arr.shape[0]/ (frame_size/2)),int(frame_size /2))
    %matplotlib notebook
    signal = arr[:,5:5+640]
    mean = np.mean(signal.T,axis=1)
    if rmbk:
        plt.imshow(arr[:,5:5+ 640] - mean)
    else:
        plt.imshow(arr[:,5:5+ 640])
    if save_fig:
        plt.savefig(fname + '.png')
    else:
        plt.show()