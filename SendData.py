import CoreData
import time
import os

def deal_msg(commend, option=""):
    """按飞秋是协议格式组建信息"""
    # 版本号: 数据包编号:发送者姓名: 发送者主机名:命令字: 附加选项
    # 1: 123456789:itcast - python: localhost:32: hello
    msg = "%d:%d:%s:%s:%d:%s" % (CoreData.feiq_version, int(time.time()),
                                 CoreData.feiq_user_name, CoreData.feiq_host_name,
                                 commend, option)
    # msg,要发送的信息
    return msg


def send_msg(msg, dest_ip):
    """发送数据指定电脑的飞秋中"""
    CoreData.udp_socket.sendto(msg.encode("utf-8"), (dest_ip, CoreData.FeiQ_port))


def send_online_msg():
    """上线时发送上线提醒"""
    online_msg = deal_msg(CoreData.IPMSG_BR_ENTRY, CoreData.feiq_user_name)
    send_msg(online_msg, CoreData.ip)


def send_offline_msg():
    """发送下线提醒"""
    offline_msg = deal_msg(CoreData.IPMSG_BR_EXIT, CoreData.feiq_user_name)
    send_msg(offline_msg, CoreData.ip)


def send_chat_msg():
    """发送聊天信息"""
    dest_ip = input('请输入要发送的ip/或输入0获取列表')
    if dest_ip == "0":
        for i, online_user in enumerate(CoreData.online_users):
            print(i, online_user)
        try:
            num = int(input('请输入用户对应的序号'))
        except:
            print("输入有误...")
            return
        else:
            dest_ip = CoreData.online_users[num]['ip']
    msg = input("请输入要发送的信息")
    chat_msg = deal_msg(CoreData.IPMSG_SENDMSG, msg)
    send_msg(chat_msg, dest_ip)


def send_file():
    """发送文件"""
    dest_ip = input('请输入要发送的ip/或输入0获取列表')
    if dest_ip == "0":
        for i, online_user in enumerate(CoreData.online_users):
            print(i, online_user)
        try:
            num = int(input('请输入用户对应的序号'))
        except:
            print("输入有误...")
            return
        else:
            dest_ip = CoreData.online_users[num]['ip']
    file_name = input('请输入要发送的文件名称')

    # 版本号: 数据包编号:发送者姓名: 发送者主机名:命令字: 附加选项
    # 1: 123456789:itcast - python: localhost:32: hello

    # 版本号: 包编号:用户名: 主机名:命令字:消息 \0文件序号: 文件名:文件大小: 文件修改时间:文件类型:
    # 1: 123123:dongge: ubuntu:文件消息命令字: 消息内容(可以没有) \0 0: hello.py:123: 12123:文件类型:
    # 命令字: IPMSG_SENDMSG | IPMSG_FILEATTACHOPT
    # 文件类型: IPMSG_FILE_REGULAR

    file_size = os.path.getsize(file_name)
    file_ctime = os.path.getctime(file_name)
    option = "%d:%s:%x:%x:%x" % (0, file_name, file_size,
                                 int(file_ctime), CoreData.IPMSG_FILE_REGULAR)
    option_str = '\0' + option
    file_msg = deal_msg(CoreData.IPMSG_SENDMSG | CoreData.IPMSG_FILEATTACHOPT, option_str)
    send_msg(file_msg, dest_ip)


