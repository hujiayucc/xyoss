#!/usr/bin/python3
# coding=UTF-8

""" 
Author: 小宇
Version: 2.0
Update Time: 2022/03/01 19:30 
"""

import os
import sys
import platform

print('''
┌─────────────────────────────────────────────┐
│               Linux 挂载OSS                 │
├─────────────────────────────────────────────┤
│                 工具介绍:                   │
│        + 挂载OSS为本地磁盘                  │
│        + 阿里服务器内网传输不耗流量         │
│        + 非阿里服务器需要填写外网Endpoint   │
│        + 只支持Python3，否则报错            │
├─────────────────────────────────────────────┤
│         小宇博客：www.hujiayucc.cn          │
└─────────────────────────────────────────────┘
''')

#Ubuntu
def ubuntu():
    print("> 请按照提示输入相关参数")
    bucket = str(input("> 输入你想要挂载的Bucket，不带Endpoint节点域名\n"))
    if bucket == "":
        print("> Bucket名不能为空")
        bucket = str(input("> 输入你想要挂载的Bucket，不带Endpoint节点域名\n"))
        if bucket == "":
            print("> Bucket名不能为空")
            sys.exit()
    accesskey = str(input("> 输入阿里云账号Accesskey ID\n"))
    if accesskey == "":
        print("> Accesskey ID不能为空")
        accesskey = str(input("> 输入阿里云账号Accesskey ID\n"))
        if accesskey == "":
            print("> Accesskey ID不能为空")
            sys.exit()
    secret = str(input("> 输入阿里云账号Accesskey Secret\n"))
    if secret == "":
        print("> Accesskey Secret不能为空")
        secret = str(input("> 输入阿里云账号Accesskey Secret\n"))
        if secret == "":
            print("> Accesskey Secret不能为空")
            sys.exit()
    endpoint = str(input("> 输入Bucket的Endpoint节点，不带Bucket名\n"))
    if secret == "":
        print("> Endpoint节点不能为空")
        endpoint = str(input("> 输入Bucket的Endpoint节点，不带Bucket名\n"))
        if secret == "":
            print("> Endpoint节点不能为空")
            sys.exit()
    sd = str(input("> 输入OSS要挂载的绝对路径，/开头\n"))
    if sd == "":
        print("> 挂载路径不能为空")
        sd = str(input("> 输入OSS要挂载的绝对路径，/开头\n"))
        if sd == "":
            print("> 挂载路径不能为空")
            sys.exit()
    #安装ossfs
    if os.path.exists("/etc/passwd-ossfs") == False:
        os.system("apt update")
        os.system("apt install gdebi-core -y")
        os.system("wget -O ossfs.deb " + deb)
        os.system("gdebi ossfs.deb")
        os.system("rm -rf ossfs.deb")
    
    os.system("echo " + str(bucket) + ":" + str(accesskey) + ":" + str(secret) + ">" + " /etc/passwd-ossfs")
    os.system("chmod 640 /etc/passwd-ossfs")
    os.system("mkdir " + str(sd))
    os.system("ossfs " + str(bucket) + " " + str(sd) + " -o url=http://" + str(endpoint))
    print("> 大功告成，虽然我也不信就这么简单，但是你爱信不信")
    sys.exit()

#CentOS
def centos():
    print("> 请按照提示输入相关参数")
    bucket = str(input("> 输入你想要挂载的Bucket，不带Endpoint节点域名\n"))
    if bucket == "":
        print("> Bucket名不能为空")
        bucket = str(input("> 输入你想要挂载的Bucket，不带Endpoint节点域名\n"))
        if bucket == "":
            print("> Bucket名不能为空")
            sys.exit()
    accesskey = str(input("> 输入阿里云账号Accesskey ID\n"))
    if accesskey == "":
        print("> Accesskey ID不能为空")
        accesskey = str(input("> 输入阿里云账号Accesskey ID\n"))
        if accesskey == "":
            print("> Accesskey ID不能为空")
            sys.exit()
    secret = str(input("> 输入阿里云账号Accesskey Secret\n"))
    if secret == "":
        print("> Accesskey Secret不能为空")
        secret = str(input("> 输入阿里云账号Accesskey Secret\n"))
        if secret == "":
            print("> Accesskey Secret不能为空")
            sys.exit()
    endpoint = str(input("> 输入Bucket的Endpoint节点，不带Bucket名\n"))
    if secret == "":
        print("> Endpoint节点不能为空")
        endpoint = str(input("> 输入Bucket的Endpoint节点，不带Bucket名\n"))
        if secret == "":
            print("> Endpoint节点不能为空")
            sys.exit()
    sd = str(input("> 输入OSS要挂载的绝对路径，/开头\n"))
    if sd == "":
        print("> 挂载路径不能为空")
        sd = str(input("> 输入OSS要挂载的绝对路径，/开头\n"))
        if sd == "":
            print("> 挂载路径不能为空")
            sys.exit()
    #安装ossfs
    if os.path.exists("/etc/passwd-ossfs") == False:
        os.system("wget -O ossfs.rpm " + rpm)
        os.system("yum install ossfs.rpm -y")
        os.system("yum install --downloadonly --downloaddir=./ fuse -y")
        os.system("rm -rf ossfs.rpm")
    os.system("echo " + str(bucket) + ":" + str(accesskey) + ":" + str(secret) + ">" + " /etc/passwd-ossfs")
    os.system("chmod 640 /etc/passwd-ossfs")
    os.system("mkdir " + str(sd))
    os.system("ossfs " + str(bucket) + " " + str(sd) + " -o url=http://" + str(endpoint))
    
    print("> 大功告成，虽然我也不信就这么简单，但是你爱信不信")
    sys.exit()

#安装ossfs和挂载OSS
def install():
    global deb
    global rpm
    version_str = str(platform.platform())
    verstr = version_str.lower()

    #Ubuntu
    ubuntuos = ("ubuntu" in verstr)
    ubuntuos1804 = ("18.04" in verstr)
    ubuntuos1604 = ("16.04" in verstr)
    ubuntuos1404 = ("14.04" in verstr)
    #CentOS
    centosos = ("centos" in verstr)
    centosos8 = ("centos-8" in verstr)
    centosos7 = ("centos-7" in verstr)

    if (ubuntuos == True):
        if (ubuntuos1804 == True):
            deb = str("https://gosspublic.alicdn.com/ossfs/ossfs_1.80.6_ubuntu18.04_amd64.deb")
            ubuntu()
        elif (ubuntuos1604 == True):
            deb = str("https://gosspublic.alicdn.com/ossfs/ossfs_1.80.6_ubuntu16.04_amd64.deb")
            ubuntu()
        elif (ubuntuos1404 == True):
            deb = str("https://gosspublic.alicdn.com/ossfs/ossfs_1.80.6_ubuntu14.04_amd64.deb")
            ubuntu()
        else:
            print("不支持你的操作系统1：" + verstr)
            sys.exit()
    elif (centosos == True):
        if (centosos8 == True):
            rpm = str("https://gosspublic.alicdn.com/ossfs/ossfs_1.80.6_centos8.0_x86_64.rpm")
            centos()
        elif (centosos7 == True):
            rpm = str("https://gosspublic.alicdn.com/ossfs/ossfs_1.80.6_centos7.0_x86_64.rpm")
            centos()
        else:
            print("不支持你的操作系统1：" + verstr)
            sys.exit()
    else:
        print("不支持你的操作系统2：" + verstr)
        sys.exit()

#卸载已挂载的oss
def remove():
    sd = str(input("> 输入你想要卸载的OSS挂载路径\n"))
    if sd == "":
        print("路径不能为空")
        sys.exit()
    else:
        os.system("fusermount -u " + str(sd))
        os.system("rm -rf " + str(sd))
        print("卸载操作完成，请检查是否卸载成功")
        sys.exit()

#菜单
def main():
    cpu = str(platform.machine())
    if cpu == "X86_64":
        print("> 你想要做什么？\n\n1.挂载新OSS\n2.卸载已挂载的OSS\n3.退出")
        menu = str(input("> 请输入功能对应的数字\n"))
        if menu == "1":
            install()
        elif menu == "2":
            remove()
        elif menu == "3":
            sys.exit()
        elif menu == "":
            print("选项不能为空")
            main()
        else:
            print("输入不正确")
            main()
    if cpu == "x86_64":
        print("> 你想要做什么？\n\n1.挂载新OSS\n2.卸载已挂载的OSS\n3.退出")
        menu = str(input("> 请输入功能对应的数字\n"))
        if menu == "1":
            install()
        elif menu == "2":
            remove()
        elif menu == "3":
            sys.exit()
        elif menu == "":
            print("选项不能为空")
            main()
        else:
            print("输入不正确")
            main()
    elif cpu == "amd64":
        print("> 你想要做什么？\n\n1.挂载新OSS\n2.卸载已挂载的OSS\n3.退出")
        menu = str(input("> 请输入功能对应的数字\n"))
        if menu == "1":
            install()
        elif menu == "2":
            remove()
        elif menu == "3":
            sys.exit()
        elif menu == "":
            print("选项不能为空")
            main()
        else:
            print("输入不正确")
            main()
    elif cpu == "AMD64":
        print("> 你想要做什么？\n\n1.挂载新OSS\n2.卸载已挂载的OSS\n3.退出")
        menu = str(input("> 请输入功能对应的数字\n"))
        if menu == "1":
            install()
        elif menu == "2":
            remove()
        elif menu == "3":
            sys.exit()
        elif menu == "":
            print("选项不能为空")
            main()
        else:
            print("输入不正确")
            main()
    else:
        print("暂不支持您的CPU架构：" + cpu)

#初始化
if __name__ == "__main__":
    main()