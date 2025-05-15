import functools # type: ignore
from SimpleMenu import *
class MultiPageMenu(SimpleMenu):
    def __init__(self, hWnd=0, GlobalListen=True, ShowIndex=False, OneTime=False,OptionsPerPageNum = 5):
        super().__init__(hWnd, GlobalListen, ShowIndex, OneTime)
        self.OptionsPerPageNum = OptionsPerPageNum
        self.CurrentPage = 1
        self.Pages:list[list[tuple[int,Option]]] = [] #存出所有页数和每个页的索引和内容
        self.forward = win32con.VK_RIGHT
        self.backward = win32con.VK_LEFT
    

    def ShowOptions(self):
        """
        刷新并显示当前的选项菜单。
        """
        self.Update()
        os.system("cls")
        for index, Option in self.Pages[self.CurrentPage-1]:
            if self.UserChoice == index:
                print(f"{index}.{Option.Value} {self.arrow}" if self.ShowIndex else f"{Option.Value} {self.arrow}")
            else:
                print(f"{index}.{Option.Value}" if self.ShowIndex else f"{Option.Value}")
        print(f"({self.CurrentPage}/{len(self.Pages)-1})")
    def RunFunc(self):
        def SetDefultChoice():
                self.UserChoice = self.Pages[self.CurrentPage-1][0][0]
                self.ShowOptions()
        def CheckIsExit(delay):
            if not self.isExit:
                    self.LimitUserChoice()
                    self.ShowOptions()
                    time.sleep(delay)
        def checkKey():
            self.ClearInput()
            if win32api.GetAsyncKeyState(self.Enter) < 0:
                if not self.Options:
                    self.Exit()
                    raise Exception("没有可用的选项！|No available options!")
                self.Options[self.UserChoice].func()  
                self.UserChoice = self.Pages[self.CurrentPage-1][0][0]
                if not self.isExit:
                    if self.isOneTime: #只运行一次
                        self.Exit()
                    else:
                        self.LimitUserChoice()
                        self.ShowOptions()
                        time.sleep(self.delay)

            elif win32api.GetAsyncKeyState(self.Up) < 0:
                self.UserChoice -= 1
            elif win32api.GetAsyncKeyState(self.Down) < 0:
                self.UserChoice += 1
            elif win32api.GetAsyncKeyState(self.forward) < 0:
                if self.CurrentPage < len(self.Pages)-1:
                    self.CurrentPage += 1
                else:
                    self.CurrentPage = 1
                SetDefultChoice()
            elif win32api.GetAsyncKeyState(self.backward) < 0:
                if self.CurrentPage > 1:
                    self.CurrentPage -= 1
                else:
                    self.CurrentPage = len(self.Pages)-1
                SetDefultChoice()
            CheckIsExit(self.delay)

        def RunFunc():
            time.sleep(self.enter_delay)
            while not self.isExit:
                if GetActiveWindowHwnd() == self.hWnd:
                    checkKey()
                elif self.GlobalListen:
                    checkKey()
        RunFunc()

    def LimitUserChoice(self):
        super().LimitUserChoice() 
        #如果当前选项超出了当前页的范围，则跳转到下一页
        if self.UserChoice > self.Pages[self.CurrentPage-1][-1][0]:
            self.CurrentPage += 1
        elif self.UserChoice < self.Pages[self.CurrentPage-1][0][0]:
            self.CurrentPage -= 1

    def GotoPage(self, pageNum):
        self.CurrentPage = pageNum
        self.UserChoice = self.Pages[self.CurrentPage-1][0][0]
        self.ShowOptions()
    
    def PlanEachPage(self):
        self.Pages.clear()
        num = 0
        flag = 0
        OptionsList = list(self.Options.items())
        while flag + self.OptionsPerPageNum <= len(self.Options):#判断是否可以分成多页
            flag = num*self.OptionsPerPageNum
            self.Pages.append(OptionsList[flag:flag+self.OptionsPerPageNum])#将选项分成每页的数量
            num += 1
        self.Pages.append(OptionsList[num*self.OptionsPerPageNum:])

    def Start(self):
        self.PlanEachPage()
        super().Start()
