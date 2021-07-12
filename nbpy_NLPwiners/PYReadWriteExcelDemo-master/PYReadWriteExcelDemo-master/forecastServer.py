from socket import *
from time import ctime
from testDataRead import forecastResult

import struct

HOST = "127.0.0.1"
PORT = 2341
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)  # 绑定IP地址和端口号s
tcpSerSock.listen(5)  # 监听，使得主动变为被动

recvdata="testData.csv 航空货物运输合同纠纷.csv"
filenamearrary = recvdata.split(" ")
print(filenamearrary[0],filenamearrary[1])
resultValue = forecastResult("testData.csv", "航空货物运输合同纠纷.csv")

while True:
    print('正在等待连接....')
    tcpCliSock, addr = tcpSerSock.accept()  # 当来新的连接时，会产生一个的新的套接字为客户端服务
    # print('收到来自%d的连接.....tcpSerSock..' % addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)  # 接受数据，缓存区设置为1kb
        print(data)
        if not data:
            break
        # tcp 发送数据格式 "testnamefile trainnamefile"
        data = str(data)
        filenamearrary = data.split(" ")
        pathname="/home/work/"
       # resultValue = forecastResult( pathname + filenamearrary[0] , pathname + filenamearrary[1])    #path为服务器下存储的关键词库的路径
        tcpCliSock.send(struct.pack(resultValue))  # 加上时间戳，并对数据编码
    tcpCliSock.close()

# tcpSerSock.close()