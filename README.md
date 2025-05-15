# 🌟 SimpleMenu

### 简介 | Introduction 📖

**SimpleMenu** 是一个用 Python 编写的轻量级命令行菜单类，可通过键盘快速创建交互式菜单。适合构建简洁、灵活的命令行应用程序。

**SimpleMenu** is a lightweight, Python-based command-line menu class for quickly creating interactive menus using the keyboard. Ideal for simple and flexible command-line applications.

---

### ✨ 功能特点 | Features 🔑
- ✅ **动态选项添加**: 支持随时向菜单添加选项。
- 🎮 **方向键导航**: 使用方向键（上下）选择，回车键确认。
- 📋 **索引显示**: 可选择显示选项索引，清晰明了。
- 🌐 **全局监听**: 支持全局或窗口内的键盘事件监听。

- ✅ **Dynamic Option Addition**: Add options to the menu at any time.
- 🎮 **Keyboard Navigation**: Navigate with arrow keys (Up/Down) and confirm with Enter.
- 📋 **Index Display**: Optional display of item indices for clarity.
- 🌐 **Global Listening**: Supports both global and window-specific keyboard event listening.

---

### 🚀 快速开始 | Quick Start

#### 安装 | Install 📦
在命令行中安装：

Install from command line:
```bash
pip install CL-Simple-Menu
```

---

#### 使用案例（来自 PyPI） | Usage Example (from PyPI) 💡

以下是一个简单菜单的示例，包括一个打印 "Hello World" 的选项：
Here’s a simple menu example that includes a "Hello World" option:

```python
import clsMenu
import time

# 定义一个选项对应的函数 | Define a function for a menu option
def HelloWorld():
    print("Hello World!")
    time.sleep(2)  # 停顿 2 秒观察效果 | Pause for 2 seconds to observe the output

# 创建菜单实例 | Create a menu instance
menu = clsMenu.SimpleMenu(hWnd=0, GlobalListen=True, ShowIndex=False, OneTime=False)
#参数分别为 hWnd 全局监听 显示索引 运行一次

# 添加选项 | Add options
menu.addOption("🌟 Print Hello World", HelloWorld)
menu.addOption("❌ Exit Menu", menu.Exit)

# 显示菜单 | Display the menu
menu.Start()

#多选菜单
demo = clsMenu.MultiSelectMenu() #继承自SimpleMenu 支持多选
demo.ChoiceComplete #完成选择，请在菜单页面的一个选项内添加这个函数
demo.GetSlects:dict[int,Option] #返回一个字典,键为自定数据类 Value为选项的内容，func为执行的函数

#多页菜单
OptionsPerPageNum = 5
demo = clsMenu.MultiPageMenu(OptionsPerPageNum) #每页显示多少个选项
#这个类会自动根据你加入的选项数量自行安排页数
#按左和右可以切换页数
#切换选项时如果超出了当前页的选项会自动跳转到下一页
demo.GotoPage(Num) #传入要去的页数
```

运行该代码后，通过键盘上下方向键导航选项，按下回车键执行选项操作。🎉  
Run the code, navigate options with the arrow keys, and press Enter to execute actions. 🎉

---

### 🛠️ API 文档 | API Documentation 📚

#### `SimpleMenu.__init__(hWnd=0, GlobalListen=True, ShowIndex=False)`
初始化菜单系统。  
Initialize the menu system.

参数 | Parameters:
- **`hWnd`**: 窗口句柄 (默认值为 0，表示全局监听)。  
  Window handle (default is 0 for global listening).
- **`GlobalListen`**: 是否启用全局键盘监听 (默认为 True)。  
  Enable global keyboard listening (default is True).
- **`ShowIndex`**: 菜单项是否显示序号 (默认为 False)。  
  Display menu item indices (default is False).

---

#### `addOption(value, func=lambda: None)`
向菜单添加一个选项。  
Add an option to the menu.

参数 | Parameters:
- **`value`**: 选项的显示名称。  
  The name of the menu option.
- **`func`**: 选项对应的执行函数 (默认为空函数)。  
  The function to execute when the option is selected (default is a no-op).

---

#### `Start()`
📜 显示菜单并开始监听用户输入。  
Display the menu and start listening for user input.
---

#### `Exit()`
🚪 退出菜单并停止监听。  
Exit the menu and stop input listening.

---

### 🎨 示例输出 | Example Output
```text
🌟 Print Hello World <----
❌ Exit Menu
```
通过上下方向键移动箭头选择选项，并按下回车键确认操作。  
Use the arrow keys to move the selection and press Enter to confirm.
---

### 📜 许可协议 | License
该项目基于 **MIT License** 开源，您可以自由使用、修改和分发。⚖️  
This project is open-sourced under the **MIT License**, allowing free use, modification, and distribution. ⚖️

---

🎉 **SimpleMenu，简约的命令行菜单解决方案！期待您的反馈！**  
🎉 **SimpleMenu, a minimal yet powerful CLI menu solution! Looking forward to your feedback!**
