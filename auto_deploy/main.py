# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import paramiko

from ssh import SFTPClient

# hostname = str(input("请输入要访问的主机:"))
hostname = '192.168.78.104'
filename = 'nanhang.tar.gz'
src1 = 'D:/BaiduNetdiskDownload/'
src2 = '/tmp/'
cmd = f'tar -zxvf /tmp/{filename} -C /home/xiaopan/'


logo = '''



'''

def main():
    ssh = SFTPClient(hostname)
    # print(ssh.file_exits(f'{src2}{filename}'))
    while True:
        if ssh.file_exits(f'{src2}{filename}') == '':
            ssh.put(f'{src1}{filename}', f'{src2}{filename}')
            print('文件传输完成')
            continue
        else:
            ssh.exec_command(cmd)
            print('解压成功')
            break
# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # print_hi('PyCharm')
    main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
