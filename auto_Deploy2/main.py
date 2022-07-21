# 这是一个示例 Python 脚本。
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
app = QApplication([])
windows = QMainWindow()
windows.resize(500, 400)
windows.move(300, 310)
windows.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(windows)
textEdit.setPlaceholderText('请输入薪资表')
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton('统计', windows)
button.move(380, 80)

windows.show()
app.exec_()


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
