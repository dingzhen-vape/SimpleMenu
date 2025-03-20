# 🌟 SimpleMenu

### 简介 | Introduction 📖

**SimpleMenu** 是一个用 Python 编写的轻量级命令行菜单系统，可以通过键盘与菜单进行交互。适合用于构建交互式命令行程序。

**SimpleMenu** is a lightweight command-line menu system written in Python. It allows users to interact with the menu using the keyboard, making it ideal for building interactive terminal-based applications.

---

### ✨ 功能特点 | Features 🔑
- ✅ 支持菜单选项动态添加。
- 🎮 使用方向键 (上下键) 和回车键进行选项导航和选择。
- 📋 支持显示选项索引。
- 🌐 支持全局或窗口内键盘监听。
- ⏱ 自定义键盘延迟和箭头显示符号。

- ✅ Dynamically add menu options.
- 🎮 Navigate and select options with arrow keys (Up/Down) and Enter key.
- 📋 Option to display menu item indexes.
- 🌐 Supports global or window-specific keyboard input listening.
- ⏱ Configurable keyboard delay and arrow symbol display.

---

### 🚀 快速开始 | Quick Start

#### 安装依赖 | Install Dependencies 📦

在命令行中安装依赖库：

Install the required libraries via the terminal:
```bash
pip install pygetwindow pywin32
```

#### 使用案例 | Usage Example 💡

以下是一个包含 "Hello World" 的简单示例：
Here is a simple example that includes a "Hello World" menu option:

```python
import SimpleMenu
import time

# 定义一个选项对应的函数 | Define a function for a menu option
def HelloWorld():
    print("Hello World!")
    time.sleep(2)  # 停顿2秒观察效果 | Pause for 2 seconds to observe the output

# 创建菜单实例 | Create a menu instance
menu = SimpleMenu.SimpleMenu()

# 添加选项 | Add options
menu.addOption(" Print Hello World", HelloWorld)
menu.addOption(" Exit Menu", menu.Exit)

# 显示菜单 | Display the menu
menu.ShowMenu()
```

运行上述代码后，你将能够通过键盘选择并执行选项。🎉

After running the code, you can use the keyboard to navigate and execute the menu options. 🎉

---

### 🛠️ API 文档 | API Documentation 📚

#### `SimpleMenu.__init__(hWnd=0, GlobalListen=True, ShowIndex=False)`
初始化菜单系统。
- **`hWnd`**: 窗口句柄 (默认值为 0，表示全局监听)。
- **`GlobalListen`**: 是否启用全局键盘监听 (默认为 True)。
- **`ShowIndex`**: 菜单项是否显示序号 (默认为 False)。

Initialize the menu system.
- **`hWnd`**: Window handle (default is 0 for global listening).
- **`GlobalListen`**: Enable global keyboard listening (default is True).
- **`ShowIndex`**: Display menu item indexes (default is False).

---

#### `addOption(value, func=lambda: None)`
向菜单添加一个选项。
- **`value`**: 选项的显示名称。
- **`func`**: 选项对应的执行函数 (默认为空函数)。

Add an option to the menu.
- **`value`**: Name of the menu option.
- **`func`**: Function to execute when the option is selected (default is a no-op).

---

#### `ShowMenu()`
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
使用上下方向键移动箭头到选项上，并按下回车键执行该选项。

Use the Up and Down arrow keys to move the arrow to an option, and press Enter to execute it.

---

### 📜 许可协议 | License
您可以根据 **MIT License** 自由使用和修改此项目。⚖️

You are free to use and modify this project under the **MIT License**. ⚖️

---
