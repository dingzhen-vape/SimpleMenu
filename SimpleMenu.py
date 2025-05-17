from multiprocessing import process
from optparse import Option
import os
import time
import pygetwindow as gw
import win32api
import win32con
import msvcrt
from .Dataclass import *
from functools import singledispatch, singledispatchmethod


def GetActiveWindowHwnd():
    # 获取当前活动窗口的句柄
    try:
        return gw.getActiveWindow()._hWnd # type: ignore
    except:
        return 0


def GetWindowHwnd(name):
    # 根据窗口标题获取窗口句柄，如果未找到则返回 -1
    try:
        return gw.getWindowsWithTitle(name)[0]._hWnd
    except:
        return -1


class SimpleMenu:
    """
    SimpleMenu 类用于创建一个简单的菜单系统，允许用户通过键盘与命令行进行交互。
    """

    def __init__(self, hWnd=0, GlobalListen=True, ShowIndex=False, OneTime=False):
        """
        初始化菜单选项、用户选择等属性。
        
        参数:
        - hWnd: 整数，指示菜单所在的窗口的句柄。如果不为0，则不全局监听。
        - GlobalListen: 布尔值，指示是否全局监听键盘或鼠标事件。
        - ShowIndex: 布尔值，指示菜单项是否显示索引。
        - OneTime: 布尔值，指示菜单是否运行函数后自动退出。
        """
        self.Options = {}
        self.index = 0
        self.Starting = False
        self.isExit = False
        self.isRunningFunc = False
        self.isOneTime = OneTime
        self.ShowIndex = ShowIndex
        self.GlobalListen = GlobalListen
        self.hWnd = hWnd
        self.UserChoice = 0
        self.Down = win32con.VK_DOWN
        self.Up = win32con.VK_UP
        self.Enter = win32con.VK_RETURN
        self.arrow = "<----"
        self.delay = 0.15
        self.enter_delay = 0.15
        if self.hWnd != 0:
            self.GlobalListen = False

    def ClearInput(self):
        while msvcrt.kbhit():
            msvcrt.getch()

    def addOption(self, value, func=lambda: None):
        """
        添加选项和对应的执行函数。

        参数:
        - value: 字符串，菜单选项的显示内容。
        - func: 函数，用户选择该选项时调用的处理函数。
        """
        self.Options[self.index] = Option(value,func)  # 索引和选项内容及执行函数
        self.index += 1
        return self

    @singledispatchmethod
    def removeOption(self, index):
        """
        移除指定索引或内容的菜单选项。
        """
        pass

    @removeOption.register(int)
    def _(self, index: int):
        """
        根据索引移除菜单选项。

        参数:
        - index: 整数，要移除的菜单选项的索引。
        """
        tempdict = {key: value for key, value in self.Options.items() if key != index}
        ttdict = {}
        for i in enumerate(tempdict.keys()):
            ttdict[i[0]] = tempdict[i[1]]
        self.Options = ttdict
        self.ShowOptions()
        return self

    @removeOption.register(str)
    def _(self, OptionContext: str):
        """
        根据选项内容移除菜单选项。

        参数:
        - OptionContext: 字符串，要移除的菜单选项的内容。
        """
        tempdict = {key: value for key, value in self.Options.items() if value[0] != OptionContext}
        ttdict = {}
        for i in enumerate(tempdict.keys()):
            ttdict[i[0]] = tempdict[i[1]]

        self.Options = ttdict
        self.ShowOptions()
        return self

    def ShowOptions(self):
        """
        刷新并显示当前的选项菜单。
        """
        self.Update()
        os.system("cls")
        for index, Option in self.Options.items():
            if self.UserChoice == index:
                print(f"{index}.{Option[0]} {self.arrow}" if self.ShowIndex else f"{Option[0]} {self.arrow}")
            else:
                print(f"{index}.{Option[0]}" if self.ShowIndex else f"{Option[0]}")

    def LimitUserChoice(self):
        """
        限制用户选择的序号范围。
        """
        if self.UserChoice >= len(self.Options):
            self.UserChoice = 0
        if self.UserChoice < 0:
            self.UserChoice = len(self.Options) - 1

    def RunFunc(self):
        """
        根据用户按键执行相应的操作。
        
        方法内部定义了两个函数：
        - checkKey: 检测键盘按键状态，处理上下箭头及回车键的操作。
        - RunFunc: 在延迟一段时间后开始监听键盘输入。
        """
        def checkKey():
            if win32api.GetAsyncKeyState(self.Enter) < 0:
                if not self.Options:
                    self.Exit()
                    raise Exception("没有可用的选项！|No available options!")
                self.isRunningFunc = True
                self.Options[self.UserChoice][1]()
                self.UserChoice = 0
                self.isRunningFunc = False
                if not self.isExit:
                    if self.isOneTime:
                        self.Exit()
                    else:
                        self.LimitUserChoice()
                        self.ShowOptions()
                        time.sleep(self.delay)

            elif win32api.GetAsyncKeyState(self.Up) < 0:
                self.UserChoice -= 1
                if not self.isExit:
                    self.LimitUserChoice()
                    self.ShowOptions()
                    time.sleep(self.delay)

            elif win32api.GetAsyncKeyState(self.Down) < 0:
                self.UserChoice += 1
                if not self.isExit:
                    self.LimitUserChoice()
                    self.ShowOptions()
                    time.sleep(self.delay)

        def RunFunc():
            time.sleep(self.enter_delay)
            while not self.isExit:
                if GetActiveWindowHwnd() == self.hWnd:
                    checkKey()
                elif self.GlobalListen:
                    checkKey()

        if not self.isRunningFunc:
            RunFunc()

    def HookKeyborad(self):
        """
        监听键盘输入。
        """
        self.RunFunc()

    def Update(self):
        """
        刷新菜单时运行的函数。
        用户自行定义。
        """
        pass
    def Start(self):
        """
        显示菜单并开始监听键盘输入。 (入口点，只能运行一次)
        """
        if not self.Starting:
            self.isExit = False
            self.Starting = True
            self.ShowOptions()
            self.HookKeyborad()
        else:
            raise Exception("已经运行了一个实例！|Is already running an instance!")
        return self

    def Exit(self):
        """
        退出菜单并停止监听键盘输入。 (出口点，在运行之前必须显示菜单)
        """
        if self.Starting:
            self.isExit = True
            self.Starting = False
        else:
            raise Exception("你必须在结束一个菜单之前显示它！| You must display the menu before exiting it!")
