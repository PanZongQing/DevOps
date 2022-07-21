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

hosts = {}


def main():
    logo = '''

    ###################################
    #####   GPU算力池自动化部署脚本   #####
    ###################################

    1.初始化操作系统
    2.部署K8S节点
    3.部署PASS相关应用
    4.部署GPU算力池应用
    5.上传部署相关脚本

    '''
    print(logo)

def config_sys():



def file_check():
    ssh = SFTPClient(hostname)
    # print(ssh.file_exits(f'{src2}{filename}'))
    while True:
        if ssh.file_exits(f'{src2}{filename}') == '':
            ssh.put(f'{src1}{filename}', f'{src2}{filename}')
            print('文件传输完成')
            continue
        else:
            if ssh.file_exits(f'/home/xiaopan/lx') == '':
                ssh.exec_command(cmd)
                print('解压成功')
            else:
                print('文件夹已存在，无需解压')
        break


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # print_hi('PyCharm')
    while True:
        main()
        num = str(input("请输入你的操作："))
        if num == '5':
            file_check()
            continue


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
