import socket
import threading
import RecvData
import SendData
import CoreData


def create_socket():
    # 1.创建socket套接字
    CoreData.udp_socket = socket. socket(socket.AF_INET, socket.SOCK_DGRAM)
    CoreData.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定端口号
    CoreData.udp_socket.bind(("", CoreData.FeiQ_port))  # 元组形式
    # 设置允许广播
    CoreData.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def print_mean():
    print("--------mean---------")
    print("1.发送上线提醒")
    print("2.发送下线提醒")
    print("3.发送消息")
    print("4.发送文件")
    print("5.接收消息")
    print("0.退出")


def main():
    # 创建套接字
    create_socket()
    # 创建一个子线程，接收数据
    recv_msg_thread = threading.Thread(target=RecvData.recv_msg)
    recv_msg_thread.start()
    while True:
        # 打印菜单
        print_mean()
        number = input("请输入进行操作的选项")
        if number == "1":
            # 发送上线提醒
            SendData.send_online_msg()
        elif number == "2":
            # 发送下线提醒
            SendData.send_offline_msg()
        elif number == "3":
            # 发送消息
            SendData.send_chat_msg()
        elif number == "4":
            # 发送文件
            SendData.send_file()
        elif number == "5":
            # 接收消息
            RecvData.recv_msg()
        elif number == "0":
            # 关闭套接字
            CoreData.udp_socket.close()
            exit()
if __name__ == "__main__":
    main()
