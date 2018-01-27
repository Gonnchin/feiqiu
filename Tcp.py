import socket
import CoreData
import threading


def deal_file_data(recv_file_data):
    """"""
    pass


def send_file(client_socket):
    recv_file_data = client_socket.recv(1024)
    dealt_data = deal_file_data(recv_file_data)
    client_socket.close()



def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定ip和port
    tcp_socket.bind(("", 8080))
    # 监听,使套接字变为可以被动链接
    tcp_socket.listen(128)
    # 等待客户端的链接
    """
    accept(),返回一个cline_socket,和客户端地址，
    cline_socket为已建立连接的客户服务（接受发送消息),tcp_socket用于等待连接
    """
    while True:
        client_socket, addr = tcp_socket.accept()
        send_file_thread = threading.Thread(target=send_file(), args=(client_socket,))
        send_file_thread.start()

if __name__ == "__main__":
    main()


