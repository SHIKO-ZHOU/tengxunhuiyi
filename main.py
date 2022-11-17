import time
import _thread
from time import sleep
from turtle import width
import Play_mp3
import pyautogui
import sys
import _thread
import time

width, height = pyautogui.size()  # 获取屏幕分辨率


sk = 1  # 检测界面开关
music_flag = 1  # 是否定时音乐
music_time = 300  # 播放英语间隔
num_sleep = 1  # 检测签到页间隔
qd_num = 10  # 循环签到次数


def print_time():  # 为线程定义一个函数
    while 1:
        Play_mp3.play('C:\\zhaotu\\swxf.wav')
        time.sleep(music_time)


# 创建线程
if music_flag:
    try:
        _thread.start_new_thread(print_time, ())
    except:
        print("Error: 无法启动线程")


def zhaotu(img_name, isqd):  # 找签到图
    img_name = pyautogui.locateOnScreen(image="C:\\zhaotu\\" + img_name + ".bmp")
    if img_name:
        pyautogui.click(img_name.left, img_name.top)
        if isqd:
            print(img_name)
            print("签到成功~休息几分钟")
            Play_mp3.play('C:\\zhaotu\\music.wav')
            pyautogui.moveTo(300, 300)


def meeting_Interface():  # 检测界面
    while sk:
        sleep(num_sleep)
        Interface = pyautogui.locateOnScreen(image="C:\\zhaotu\\sign_survival.bmp")
        if Interface is not None:
            print("签到界面存在")
            temp = qd_num
            for _ in range(qd_num):
                temp -= 1
                sign_in()
                print("循检第", temp, "次")
        else:
            reconnection()
            print("找不到签到界面")


def sign_in():
    zhaotu("qiandao1", 1)
    zhaotu("qiandao2", 1)
    zhaotu("qiandao3", 1)
    zhaotu("qiandao", 0)


def reconnection():
    sleep(1)
    print("未找到签到界面，尝试打开")
    pyautogui.hotkey("ctrl", "alt", "t")
    zhaotu("Interface", 0)
    sleep(1)
    zhaotu("Interface1", 0)


if __name__ == '__main__':
    if width == 1920 and height == 1080:
        print("分辨率正常", width, height)
    else:
        print("暂不支持该分辨率")
        sys.exit()

    meeting_Interface()
