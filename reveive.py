import socket
import json
import requests
import random
from sendmsg import *
ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ListenSocket.bind(('127.0.0.1',5800))
ListenSocket.listen(100)
HttpResponseHeader = '''HTTP/1.1 200 OK
Content-Type: text/html
'''
def request_to_json(msg):
    for i in range(len(msg)):
        if msg[i]=="{" and msg[-1]=="\n":
            return json.loads(msg[i:])
    return None
#需要循环执行，返回值为json格式
def rev_msg():# json or None
    Client, Address = ListenSocket.accept()
    Request = Client.recv(1024).decode(encoding='utf-8')
    rev_json=request_to_json(Request)
    Client.sendall((HttpResponseHeader).encode(encoding='utf-8'))
    Client.close()
    return rev_json

while True:
    try:
        rev = rev_msg()
        print(rev)
        if rev == None:
            continue
    except:
        continue
    if rev["post_type"] == "message":
        #print(rev) #需要功能自己DIY
        if rev["message_type"] == "private": #私聊
            if rev['raw_message']=='在吗':
                qq = rev['sender']['user_id']
                send_msg({'msg_type':'private','number':qq,'msg':'我在'})
        elif rev["message_type"] == "group": #群聊
            group = rev['group_id']
            if "[CQ:at,qq=机器人的QQ号]" in rev["raw_message"]:
                if rev['raw_message'].split(' ')[1]=='在吗':
                    qq=rev['sender']['user_id']
                    send_msg({'msg_type':'group','number':group,'msg':'{}我在'.format(qq)})
        else:
            continue
    else:  # rev["post_type"]=="meta_event":
        continue
