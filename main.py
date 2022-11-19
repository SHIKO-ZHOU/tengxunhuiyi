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

now_hour = time.strftime("%H", time.localtime())
sk = 1  # 检测界面开关
music_flag = 1
music_time = 1800  # 播放音乐间隔
num_sleep = 1  # 检测签到页间隔
qd_num = 10  # 循环签到次数
if now_hour > "22":
    music_flag = 0  # 是否定时音乐


def print_time():  # 为线程定义一个函数
    while 1:
        Play_mp3.play('txhyi\zhaotu\swxf.wav')
        time.sleep(music_time)
        print("休息时间关闭提示音乐")


# 创建线程
if music_flag:
    try:
        _thread.start_new_thread(print_time, ())
    except:
        print("Error: 无法启动线程")


def zhaotu(img_father, isqd, img_son):  # 找签到图
    img_father = pyautogui.locateOnScreen(image="txhyi\zhaotu\\"+img_father+".bmp")
    if img_father:
        # 判断是否进入签到界面
        if isqd:
            print("开始签到")
            img_son = pyautogui.locateOnScreen(image="txhyi\zhaotu\\" + img_son + ".bmp", confidence=0.7)
            if (img_son):
                pyautogui.click(img_son.left, img_son.top)
                print("签到成功~")
                Play_mp3.play('txhyi\\zhaotu\\bl.wav')
                pyautogui.moveTo(300, 300)
            else:
                print("未找到按钮")
        else:
            pyautogui.click(img_father.left, img_father.top)


def meeting_Interface():  # 检测界面
    while sk:
        sleep(num_sleep)
        ""
        Interface = pyautogui.locateOnScreen(image="txhyi\zhaotu\sign-survival.bmp")
        if Interface is not None:
            print("签到界面已存在")
            temp = qd_num
            for _ in range(qd_num):
                temp -= 1
                sign_in()
                print("循检第", temp, "次")
        else:
            reconnection()
            print("找不到签到界面")


def sign_in():
    zhaotu("qiandao1", 1, "qiandao1-1")
    zhaotu("qiandao2", 1, "qiandao2-1")
    zhaotu("qiandao", 0, None)
    sleep(0.5)


def reconnection():
    sleep(1)
    print("未找到签到界面，尝试打开~")
    pyautogui.hotkey("ctrl", "alt", "t")
    zhaotu("Interface", 0, None)
    sleep(1)
    zhaotu("Interface1", 0, None)


print("你好我是时空，这是我第一次用python。\n\n使用教程：手动进入会议界面就行了，不能有任何窗口遮挡，程序运行时建议不要使用电脑，挂机就行\n\n每30分会播放音乐来检查程序是否存活(晚上10点后运行程序会自动关闭提示音乐)，签到成功后会有音乐提示\n\n==十五秒后启动==")
sleep(1)
if width == 1920 and height == 1080:
    print("分辨率正常", width, height)
else:
    print("暂不支持该分辨率")
    sys.exit()
meeting_Interface()
