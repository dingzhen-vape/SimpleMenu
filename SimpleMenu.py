
import os
import time
import pygetwindow as gw
import win32api
import win32con

def GetActiveWindowHwnd():
    # 获取当前活动窗口的句柄
    try:
        return gw.getActiveWindow()._hWnd
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
    
    属性:
    - Options: 字典，存储菜单选项及其对应的处理函数。
    - index: 当前选中的菜单选项的索引。
    - Starting: 布尔值，指示菜单是否正在启动。
    - isExit: 布尔值，指示菜单是否应该退出。
    - isRunningFunc: 布尔值，指示当前是否有菜单选项的处理函数正在运行。
    - isOneTime: 布尔值，指示菜单是否运行函数后自动退出。
    - ShowIndex: 布尔值，指示菜单项是否显示索引。
    - GlobalListen: 布尔值，指示是否全局监听键盘或鼠标事件。
    - Down: 整数，指示向下选择所需按键的虚拟键码。
    - Up: 整数，指示向上选择所需按键的虚拟键码。
    - Enter: 整数，指示回车所需按键的虚拟键码。
    - arrow: 字符串，指示当前选中的菜单项的箭头。
    - delay: 数字，指示菜单项切换的延迟时间。
    - enter_delay: 数字，指示按下回车键后的延迟时间。
    - hWnd: 整数，指示菜单所在的窗口的句柄。
    - UserChoice: 整数，指示用户当前选择的菜单项的索引。
    
    方法:
    - __init__ : 初始化菜单选项、用户选择等属性。
    - addOption : 添加选项和对应的执行函数。
    - ShowOptions : 刷新并显示当前的选项菜单。
    - LimitUserChoice : 限制用户选择的序号范围。
    - RunFunc : 根据用户按键执行相应的操作。
    - HookKeyborad : 监听键盘输入。
    - ShowMenu : 显示菜单并开始监听键盘输入。（入口，只能运行一次）
    - Exit : 退出菜单并停止监听键盘输入。（出口，在运行之前必须显示菜单）
    
    使用方法:
    - t = SimpleMenu.SimpleMenu()
    - t.addOption("hello", YourFunction)
    - t.ShowMenu()

    内置函数:
    - GetActiveWindowHwnd : 获取当前活动窗口的句柄。
    - GetWindowHwnd : 根据窗口标题获取窗口句柄，如果未找到则返回 -1。

    SimpleMenu class is used to create a simple menu system that allows users to interact with the menu via the keyboard.
    
    Attributes:
    - Options: Dictionary, stores menu options and their corresponding handler functions.
    - index: The index of the currently selected menu option.
    - Starting: Boolean, indicates whether the menu is currently starting.
    - isExit: Boolean, indicates whether the menu should exit.
    - isRunningFunc: Boolean, indicates whether a handler function for a menu option is currently running.
    - ShowIndex: Boolean, indicates whether menu items should display their indexes.
    - GlobalListen: Boolean, indicates whether to globally listen to keyboard or mouse events.
    - Down: Integer, indicates the virtual key code for the Down arrow.
    - Up: Integer, indicates the virtual key code for the Up arrow.
    - Enter: Integer, indicates the virtual key code for the Enter key.
    - arrow: String, indicates the arrow for the currently selected menu item.
    - delay: Numeric, indicates the delay time for switching menu items.
    - enter_delay: Numeric, indicates the delay time after pressing the Enter key.
    - hWnd: Integer, indicates the handle of the window where the menu is located.
    - UserChoice: Integer, indicates the index of the menu item currently selected by the user.
    
    Methods:
    - __init__ : Initializes the menu options, user selection, etc.
    - addOption : Adds an option and its corresponding execution function.
    - ShowOptions : Refreshes and displays the current options menu.
    - LimitUserChoice : Restricts the range of user selection indices.
    - RunFunc : Executes the corresponding operation based on the user's key press.
    - HookKeyborad : Listens to keyboard input.
    - ShowMenu : Displays the menu and starts listening to keyboard input. (Entry point, can only run once)
    - Exit : Exits the menu and stops listening to keyboard input. (Exit point, must display the menu before running)
    
    Usage:
    - t = SimpleMenu.SimpleMenu()
    - t.addOption("hello", YourFunction)
    - t.ShowMenu()

    Built-in functions:
    - GetActiveWindowHwnd : Gets the handle of the current active window.
    - GetWindowHwnd : Gets the handle of the window with the specified title, or -1 if not found.
    """

    def __init__(self,hWnd = 0,GlobalListen = True , ShowIndex = False ,OneTime = False):
        # 初始化菜单选项、用户选择等属性
        self.Options = {}
        self.index = 0
        self.Starting = False
        self.isExit = False
        self.isRunningFunc = False
        self.isOneTime = OneTime
        self.ShowIndex = ShowIndex
        self.GlobalListen = GlobalListen
        self.hWnd= hWnd
        self.UserChoice = 0
        self.Down = win32con.VK_DOWN
        self.Up = win32con.VK_UP
        self.Enter = win32con.VK_RETURN
        self.arrow = "<----"
        self.delay = 0.15
        self.enter_delay = 0.15
        if self.hWnd != 0:
            self.GlobalListen = False
    # 添加选项和对应的执行函数
    def addOption(self,value, func = lambda:None):
        self.Options[self.index] = [value,func]#索引和选项内容和执行函数
        self.index += 1
        return self
    # 显示当前的选项菜单
    def ShowOptions(self):
        os.system("cls")
        for index, Option in self.Options.items():
            if self.UserChoice == index:
                if self.ShowIndex:
                    print(f"{index}.{Option[0]} {self.arrow}")
                else:
                    print(f"{Option[0]} {self.arrow}")
            else:
                if self.ShowIndex:
                    print(f"{index}.{Option[0]}")
                else:
                    print(f"{Option[0]}")

    # 限制用户选择的序号范围
    def LimitUserChoice(self):
        if self.UserChoice >= len(self.Options):
            self.UserChoice = 0
        if self.UserChoice < 0:
            self.UserChoice = len(self.Options) - 1
    # 根据用户按键执行相应的操作
    def RunFunc(self):
        def checkKey():
                if win32api.GetAsyncKeyState(self.Enter) < 0:
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
    # 监听键盘输入
    def HookKeyborad(self):
        self.RunFunc()
    # 显示菜单并开始监听键盘输入
    def ShowMenu(self):
        if not self.Starting:
            self.isExit = False
            self.Starting = True
            self.ShowOptions()
            self.HookKeyborad()
        else:
            raise Exception("已经运行了一个实例！|Is already running an instance!")
        return self
    # 退出菜单并停止监听键盘输入
    def Exit(self):
        if self.Starting:
            self.isExit = True
            self.Starting = False
        else:
            raise Exception("你必须在结束一个菜单之前显示它！| You must display the menu before exiting it!")
