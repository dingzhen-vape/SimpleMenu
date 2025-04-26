

from SimpleMenu import *
class Callable:
    pass

class MultiSelectMenu(SimpleMenu):
    def __init__(self, hWnd=0, GlobalListen=True, ShowIndex=False):
        super().__init__(hWnd, GlobalListen, ShowIndex)



        self.ChoicedOptions:dict[int,bool] = {}
        self.selects:dict[int,Callable] = None

    def addOption(self, value, func=lambda: None):
        self.Options[self.index] = [value, func]  # 索引和选项内容及执行函数
        self.index += 1
        self.RefershSelects()
        return self
    def RefershSelects(self):
        for i in range(self.Options.__len__()):
            self.ChoicedOptions[i] = False
    def ShowOptions(self):
        """
        刷新并显示当前的选项菜单。
        """
        self.Update()
        os.system("cls")
        for index, Option in self.Options.items():
            if self.UserChoice == index:
                if self.ChoicedOptions[index]:
                    print(f"{index}.{Option[0]}  ■ {self.arrow}" if self.ShowIndex else f"{Option[0]} ■ {self.arrow}")
                else:
                    print(f"{index}.{Option[0]} □ {self.arrow}" if self.ShowIndex else f"{Option[0]} □ {self.arrow}")
            else:
                if self.ChoicedOptions[index]:
                    print(f"{index}.{Option[0]}  ■" if self.ShowIndex else f"{Option[0]} ■")
                else:
                    print(f"{index}.{Option[0]} □" if self.ShowIndex else f"{Option[0]} □")


    def RunFunc(self):
        def CheckIsExit():
            if not self.isExit:
                self.LimitUserChoice()

                self.ShowOptions()
                time.sleep(self.delay)

        def checkKey():
            if win32api.GetAsyncKeyState(self.Enter) < 0:
                if not self.Options:
                    self.Exit()
                    raise Exception("没有可用的选项！|No available options!")
                self.isRunningFunc = True
                self.ChoicedOptions[self.UserChoice] = not self.ChoicedOptions[self.UserChoice]
                if self.Options[self.UserChoice][1] == self.ChoiceComplete:
                    self.Options[self.UserChoice][1]()
                self.isRunningFunc = False
                CheckIsExit()

            elif win32api.GetAsyncKeyState(self.Up) < 0:
                self.UserChoice -= 1
                CheckIsExit()

            elif win32api.GetAsyncKeyState(self.Down) < 0:
                self.UserChoice += 1
                CheckIsExit()
        def RunFunc():
            time.sleep(self.enter_delay)
            while not self.isExit:
                if GetActiveWindowHwnd() == self.hWnd:
                    checkKey()
                elif self.GlobalListen:
                    checkKey()

        if not self.isRunningFunc:
            RunFunc()
    

    def ChoiceComplete(self) -> dict[int, list[str, Callable]]:
        self.Exit()
        self.selects = {key:self.Options[key] for key,value in self.ChoicedOptions.items() if value and self.Options[key][1]!= self.ChoiceComplete}
        self.RefershSelects()
        return self.selects
    def GetSlects(self):# -> dict | None:
        if self.selects:
            return self.selects
        else:
            return None
