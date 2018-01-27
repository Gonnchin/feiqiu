udp_socket = None  # 保存套接字
FeiQ_port = 2425  # 飞秋端口号
ip = "255.255.255.255"  # 目的ip/广播ip
feiq_version = 1  # 版本号
feiq_user_name = "QQ"  # 用户名
feiq_host_name = "ubuntu-1"  # 主机名

IPMSG_BR_ENTRY = 0x00000001  # 上线
IPMSG_BR_EXIT = 0x00000002  # 下线
IPMSG_SENDMSG = 0x00000020  # 发送消息
IPMSG_ANSENTRY = 0x00000003  # 应答在线
IPMSG_RECVMSG = 0x00000021  # 告知对方 已收到消息
IPMSG_FILEATTACHOPT = 0x00200000  # 表示文件消息
IPMSG_FILE_REGULAR = 0x00000001  # 表示普通文件

online_users = list()
