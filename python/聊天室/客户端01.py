import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('149.129.100.176', 13142))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
while True:
    # 发送数据:
    data=input("输入：")
    s.send(data.encode(encoding='utf-8'))
    
    print(s.recv(1024).decode('utf-8'))

    if data=='exit':
        s.send('exit')
s.close()