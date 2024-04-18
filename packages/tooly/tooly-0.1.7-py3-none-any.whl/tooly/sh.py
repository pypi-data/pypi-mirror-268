import argparse
import os
import subprocess
import sys
import zipfile
from typing import Union, Dict, Callable

from tooly.types import Encoding, Literal

defaultShellEncoding: Encoding = 'utf8'
if sys.platform.find('win'):
    defaultShellEncoding = 'gbk'

isDir = os.path.isdir


def run(cmd, encoding=defaultShellEncoding, failExit=True, withRetCode=False, log=print, showCmd=True, showOutput=True):
    if not log:
        log = lambda *args: None
    if isinstance(cmd, list):
        if showCmd:
            log(' \\\n\t'.join(cmd))
        cmd = ' '.join(cmd)
    else:
        if showCmd:
            log(cmd)
    p = subprocess.Popen(cmd, shell=True, encoding=encoding, stdout=subprocess.PIPE)
    cmd = " ".join((i.strip("\\") for i in cmd.splitlines()))
    contents = []
    try:
        while p.poll() is None:
            line = p.stdout.readline()
            if showOutput:
                log(line, end="")
            contents.append(line)
    except KeyboardInterrupt:
        sys.exit()
    if failExit and p.returncode != 0:
        log(f'{cmd} 执行失败, code = {p.returncode}, stdout = \n {"".join(contents)}')
        sys.exit()
    if withRetCode:
        return p.returncode, "".join(contents).strip()
    else:
        return "".join(contents).strip()


def runS(cmd, encoding=defaultShellEncoding, failExit=True, withRetCode=False, log=print, showCmd=False,
         showOutput=False):
    """
    以silent的模式运行命令，仅返回结果
    """
    return run(cmd, encoding=encoding, failExit=failExit, withRetCode=withRetCode, log=log, showCmd=showCmd,
               showOutput=showOutput)


class CustomHelpFormatter(argparse.HelpFormatter):
    """
    argparse的自定义help信息生成器，能在parser.add_argument函数没有help信息时打印default信息
    使用时，只需要在创建parser时传入即可，示例如下：
    >>> parser = argparse.ArgumentParser(formatter_class=CustomHelpFormatter)
    """

    def _format_args(self, action: argparse.Action, default_metavar: str) -> str:
        if action.default != argparse.SUPPRESS and action.default:
            default_val = "{" + f"{default_metavar}:{action.default}" + "}"
            return super()._format_args(action, default_val)
        else:
            return super()._format_args(action, default_metavar)


def writeText(fname: str, *contents: str, encoding: Encoding = "utf8"):
    mode = 'w'
    with open(fname, mode, encoding=encoding) as fd:
        for content in contents:
            fd.write(content)


def appendText(fname: str, *content: str, encoding: Encoding = 'utf8'):
    with open(fname, 'a+', encoding=encoding) as fd:
        for c in content:
            fd.write(c)


def readAsBytes(fname: str) -> bytes:
    with open(fname, 'rb') as fd:
        return fd.read()


def readAsText(fname: str, encoding: Encoding = "utf8") -> str:
    with open(fname, 'r', encoding=encoding) as fd:
        return fd.read()


def zipFiles(dst: str, *srcFiles: str):
    """
    :param dst: 压缩的目标文件
    :param srcFiles: 要压缩文件列表，支持文件通配符。需要传递相对路径否则会在压缩文件中创建全路径
    :return:
    """
    run(f"tar czf {dst} {' '.join(srcFiles)}")


def unzip(zipFname: str, dstDir: str):
    with zipfile.ZipFile(zipFname) as fd:
        fd.extractall(dstDir)


def p7zip(dst: str, *srcFiles: str):
    run(f"7z a {dst} {' '.join(srcFiles)}")


def p7unzip(zipFname: str, dstDir: str = ""):
    if dstDir:
        dstDir = "-o " + dstDir
    run(f"7z x {zipFname} {dstDir}")


def gitCommitId(requireClean: bool = True, shortId: bool = False, branch: str = "") -> Union[str, None]:
    """
    获取当前文件夹下的git commit id
    :param requireClean: 是否要求git status状态为clean
    :param shortId: 是否返回短ID（8字节）
    :param branch:若不为空，则要求当前的branch为指定branch
    :return:
    """
    if requireClean:
        ret = run("git status")
        if ret.find("nothing to commit, working tree clean") < 0:
            print("git代码未commit")
            return None

    if branch:
        if branch != gitBranch():
            print("git分支与预期不符")
            return None

    ret = run("git rev-parse HEAD")
    if shortId:
        return ret.strip()[:8]
    return ret.strip()


def gitBranch():
    ret = run("git branch")
    lines = ret.splitlines()
    for line in lines:
        line = line.strip()
        if line.startswith("*"):
            return line.split(" ")[1]


def genDockerRunCmd(dockerName: str,
                    dockerImage: str,
                    command: str = "",
                    customParams: str = "",
                    daemomMode=False,
                    envs: Dict[str, str] = {},
                    fileMapping: Dict[str, str] = {},
                    portMapping: Dict[int, int] = {},
                    workingDirInDocker: str = None,
                    multiLine: bool = False,
                    removeOnExit: bool = True):
    """
    生成docker运行的命令
    :param dockerName: docker名称
    :param dockerImage: docker image
    :param command: 可选，docker的启动命令
    :param customParams: 额外的命令行参数可以在此指定
    :param daemomMode: 是否在后台运行
    :param envs: 环境变量列表
    :param fileMapping: 文件映射列表 host -> docker
    :param portMapping: 端口映射列表 host -> docker
    :param workingDirInDocker: docker内pwd
    :param removeOnExit: docker结束后是否删除docker
    :param multiLine 命令是否分割成多行
    :return:
    """
    if not dockerImage:
        raise Exception("docker image不能为空")
    if not dockerName:
        raise Exception("docker name不能为空")

    _removeOnExit = " --rm" if removeOnExit else ""
    _daemonMode = " -d" if daemomMode else ""

    lineStart = "\t" if multiLine else ""
    lineEnd = " \\\n" if multiLine else ""

    mappings = []
    mappings += [f'{lineStart}-e {k}={v}{lineEnd}' for (k, v) in envs.items()]
    mappings += [f'{lineStart}-v {k}:{v}{lineEnd}' for (k, v) in fileMapping.items()]
    mappings += [f'{lineStart}-p {k}:{v}{lineEnd}' for (k, v) in portMapping.items()]
    _workdingDir = f" -w {workingDirInDocker}" if workingDirInDocker else ""

    _mappings = " ".join(mappings)

    return f"docker run{_removeOnExit}{_daemonMode}{customParams} --name {dockerName}{lineEnd}{_mappings}{lineStart}{_workdingDir}{dockerImage}{command}"


def runInTmux(cmd: str, sessionName: str = None):
    """
    新建一个tmux，并在其中运行命令（python脚本退出后，tmux中的命令仍然在运行
    """
    try:
        import libtmux
    except:
        raise Exception("libtmux未安装，请使用如下命令安装：pip install libtmux")
    server = libtmux.Server()
    if sessionName:
        sess = server.find_where({"session_name": sessionName})
        if sess:
            sess.kill_session()
    sess = server.new_session(session_name=sessionName)
    sess.attached_pane.send_keys(cmd.strip() + "\n")


def sshExecWithParamiko(cmd: str):
    try:
        import paramiko
    except:
        raise Exception("libtmux未安装，请使用如下命令安装：pip install paramiko")


def withParamiko(host: str, userName: str, fun: Callable,
                 port: int = 23,
                 isScp: bool = False,
                 passwd: str = None,
                 rsaFile: str = None,
                 rsaPasswd: str = None):
    try:
        import paramiko
        from scp import SCPClient
    except:
        raise Exception("libtmux未安装，请使用如下命令安装：pip install paramiko")

    ssh = paramiko.SSHClient()
    try:
        ssh.load_system_host_keys()
        pkey = None
        if rsaFile:
            pkey = paramiko.RSAKey.from_private_key_file(filename=rsaFile, password=rsaPasswd)
        ssh.connect(hostname=host, port=port, username=userName, pkey=pkey, password=passwd)

        if isScp:
            with SCPClient(ssh.get_transport()) as scp:
                fun(scp)
        else:
            fun(ssh)

    finally:
        ssh.close()


def scpWithParamiko(srcPath: str,
                    dstPath: str,
                    host: str,
                    userName: str,
                    port: int = 23,
                    passwd: str = None,
                    rsaFile: str = None,
                    rsaPasswd: str = None,
                    recursive: bool = True,
                    method: Literal["put", "get"] = "put"):
    def f(scp):
        if "put" == method:
            scp.put(srcPath, dstPath, recursive=recursive)
        else:
            scp.get(srcPath, dstPath, recursive=recursive)

    withParamiko(host, userName, f, isScp=True, port=port, passwd=passwd, rsaFile=rsaFile, rsaPasswd=rsaPasswd)


if __name__ == '__main__':
    # print(ls("*.py"))
    # touch("a/b/c.txt")
    # move("a/*.txt","a/b")
    # rm("a/b/*.txt")
    # print(ls("a/b/"))
    # rm("a")
    # print(ls("a/b/"))
    # touch("a/b/c.txt")
    # touch("a/b.txt")
    # mkdir("a/d")
    # zip("a/", "f.zip")
    # zip("f.zip", "a", excludeFiles=["a/d"])
    # touch("a/b/b1.txt")
    # mkdir("a/b/c/")
    # touch("a/d.txt")
    # mkdir("a/d/")
    # p7zip("out.7z", "a")
    # unzip("out.zip", "extract")
    # p7unzip("out.7z", "extract")
    # print(gitCommitId(requireClean=False))
    # print(genDockerRunCmd("ddd", "nginx", fileMapping={
    #     "/hostDir": "/dockerDir",
    #     "/hostDir2": "/dockerDir"
    # }, portMapping={
    #     22: 33,
    #     44: 55,
    #     23: 4403
    # }, envs={
    #     "NAME": "liyuan"
    # }, multiLine=True))
    run("ls")
