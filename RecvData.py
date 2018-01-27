import CoreData
import SendData

def deal_msg(recv_data):
    """ 将信息处理－>目的：提取附加选项中发送过来的消息内容"""
    msg = recv_data.decode("gbk", errors="ignore")
    # 版本号: 数据包编号:发送者姓名: 发送者主机名:命令字: 附加选项(发送的消息内容保存在当中)
    # 1: 123456789:itcast - python: localhost:32: hello

    # 未处理的信息是一个字符串,将字符串按：切片,切5次，得到以列表
    recv_list = msg.split(":", 5)
    recv_dict = dict()
    recv_dict['version'] = recv_list[0]
    recv_dict['packet_ip'] = recv_list[1]
    recv_dict['user_name'] = recv_list[2]
    recv_dict['host_name'] = recv_list[3]
    recv_dict['command_num'] = recv_list[4]
    recv_dict['option'] = recv_list[5]

    return recv_dict


def get_command(command_num):
    """提取命令字"""
    command = int(command_num) & 0x000000ff
    option = int(command_num) & 0xffffff00
    return command, option


def recv_msg():
    """接收数据"""
    while True:
        recv_data, recv_addr = CoreData.udp_socket.recvfrom(1024)  # 一次接收1024字节
        recv_dict = deal_msg(recv_data)
        command, option = get_command(recv_dict['command_num'])
        if command == CoreData.IPMSG_BR_ENTRY:
            print("%s上线" % recv_dict['user_name'])
            user_data = dict()
            user_data['user_name'] = recv_dict['user_name']
            user_data['ip'] = recv_addr[0]
            if user_data not in CoreData.online_users:
                CoreData.online_users.append(user_data)
        elif command == CoreData.IPMSG_ANSENTRY:
            print("%s已在线" % recv_dict['user_name'])
            user_data = dict()
            user_data['user_name'] = recv_dict['user_name']
            user_data['ip'] = recv_addr[0]
            if user_data not in CoreData.online_users:
                CoreData.online_users.append(user_data)
        elif command == CoreData.IPMSG_BR_EXIT:
            print("%s下线" % recv_dict['user_name'])
            for user in CoreData.online_users:
                if user['ip'] == recv_addr[0]:
                    CoreData.online_users.remove(user)
                else:
                    break
        elif command == CoreData.IPMSG_SENDMSG:
            print("%s(%s)>>%s" % (recv_dict['user_name'], recv_addr[0], recv_dict['option']))
            recv_ok_msg = SendData.deal_msg(CoreData.IPMSG_RECVMSG)
            SendData.send_msg(recv_ok_msg, recv_addr[0])
