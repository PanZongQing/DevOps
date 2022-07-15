import paramiko


class SFTPClient:
    def __init__(self, host, port=22, user='root', password='123456'):
        self.user = user
        self.host = host
        self.port = port
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, self.password)
        self._sftp = self.ssh.open_sftp()

    def exec_command(self, cmd):
        _, stdout, _ = self.ssh.exec_command(cmd)
        return stdout.read().decode('utf-8')

    def file_exits(self, filename):
        _, stdout, _ = self.ssh.exec_command(f'ls {filename}')
        return stdout.read().decode('utf-8')

    # def file_dec(self, src_path, dst_path):
    #     self.ssh.exec_command(f'tar -zxvf {src_path} -C {dst_path}')

    def put(self, src_path, dst_path):
        self._sftp.put(f'{src_path}', f'{dst_path}')

    def get(self, src_path, dst_path):
        self._sftp.get(f'{src_path}', f'{dst_path}')

    def close(self):
        self._sftp.close()
