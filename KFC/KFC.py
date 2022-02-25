import time

import requests

import simuse
import demjson
import simuse
with open('data.json', mode='r') as f:
    data = demjson.decode(f.read())

# 连接bot
p = simuse.Get_Session(data=data, getsession=1)
data['session'] = p
if p != 1:
    print('bot连接成功')

    times = 0
    # 每小时检测一次当前时间
    print('开始监听')
    if data['bizui!'] == 'True':
        print('免打扰模式启用中,将会在晚上11-早上8点停止推送')
    while True:
        timelocal = time.localtime()
        startTime = time.strftime("%A", time.localtime())

        # 免打扰时间
        if data['bizui!'] == 'True':
            if timelocal[3] < 8 or timelocal[3] > 22:
                print('当前处于免打扰时间，自动跳过')
                pass
            else:
                if startTime != 'Friday':
                    print('现在是', time.strftime("%A %Y-%m-%d %H:%M", time.localtime()), '未到达指定日期，已跳过')
                if startTime == 'Friday':
                    with open('疯狂星期三！！！.txt', encoding='utf-8') as f:
                        datac = f.readlines()
                        group = str(data['group']).split(',')
                        print('群推送', group[0])
                        try:
                            post = {
                                "sessionKey": data['session'],
                                "target": group[0],
                                "messageChain": [
                                    {"type": "Plain", "text": str(datac[times]).replace('\n', '')}
                                ]
                            }
                            requests.request('post', url='http://'+data['host']+'/sendGroupMessage', json=post)
                        except:
                            times = 0
                    if times < len(datac):
                        times += 1
                    else:
                        pass
                elif startTime == 'Thursday':
                    with open('疯狂星期四！！！.txt', encoding='utf-8') as f:
                        datac = f.readlines()
                        group = str(data['group']).split(',')
                        print('群推送', group[0])
                        try:
                            post = {
                                "sessionKey": data['session'],
                                "target": group[0],
                                "messageChain": [
                                    {"type": "Plain", "text": str(datac[times]).replace('\n', '')}
                                ]
                            }
                            requests.request('post', url='http://' + data['host'] + '/sendGroupMessage', json=post)
                        except:
                            times = 0

                    if times < len(datac):
                        times += 1
                    else:
                        pass
        else:
            if startTime != 'Wednesday':
                print('现在是', time.strftime("%A %Y-%m-%d %H:%M", time.localtime()), '未到达指定日期，已跳过')
            if startTime == 'Wednesday':
                with open('疯狂星期三！！！.txt', encoding='utf-8') as f:
                    datac = f.readlines()
                    group = str(data['group']).split(',')
                    print('群推送', group[0])
                    try:
                        post = {
                            "sessionKey": data['session'],
                            "target": group[0],
                            "messageChain": [
                                {"type": "Plain", "text": str(datac[times]).replace('\n', '')}
                            ]
                        }
                        requests.request('post', url='http://' + data['host'] + '/sendGroupMessage', json=post)
                    except:
                        times = 0
                if times < len(datac):
                    times += 1
                else:
                    pass
            elif startTime == 'Thursday':
                with open('疯狂星期四！！！.txt', encoding='utf-8') as f:
                    datac = f.readlines()
                    group = str(data['group']).split(',')
                    print('群推送', group[0])
                    try:
                        post = {
                            "sessionKey": data['session'],
                            "target": group[0],
                            "messageChain": [
                                {"type": "Plain", "text": str(datac[times]).replace('\n', '')}
                            ]
                        }
                        requests.request('post', url='http://' + data['host'] + '/sendGroupMessage', json=post)
                    except:
                        times = 0

                if times < len(datac):
                    times += 1
else:
    print('连接失败，请检查文件的host设置')

    time.sleep(int(data['times']))

