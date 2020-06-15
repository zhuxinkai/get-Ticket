#coding=utf-8

import requests
import time
import emailmodule

departDateList = []

#   服务一直运行，2个小时进行一次轮询。
#  2020年5月26日，进行了改版。 1.1 更改了深圳到东莞，和东莞到深圳两个数据包格式，不使用同一一个格式得数据。防止放票时数据不对称得问题。
#  如果在一个for 循环中发送了两封邮件，那么将休眠3天。另外将查询时间从1个小时，改为2个小时，缓解接口压力。

while 1==1:
    count = 0
    for i in range(2,15):
        localtime = time.localtime(time.time() + 86400*i)
        #print(localtime)
        #print (i)

        header = {
            'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            'Cookie': 'JSESSIONID=5969ED4FBD7AD8E00755D7EBB2032B51',
            'userToken': 'ZWJjNzdhNGViNTE1OTI2Yjk3Y2VhMWY2N2U1ZjMxMjYyMDIwMDUxMTEwNDAwMzMzNjQ0NA==',
            'appVersion': '1.3.9',
            'deviceVersion': '13.3.1', 'imei': 'cd2bf0fd0da5967beeb6504def8142ad', 'phoneBrand': 'iPhone'}
        url = 'http://passenger.wyebus.com/api/v4/bus/search'
        departDate = time.strftime("%Y-%m-%d", localtime)
             #判断是否为周五或者周一

        if (localtime.tm_wday == 0 or localtime.tm_wday == 4):
            if(localtime.tm_wday == 0):
                print("今天是订票的日子,今天是星期%s，开始订票吧！！！"%localtime.tm_wday)
                d1 = {'arriveCityName': '深圳', 'arriveDistrictName': '', 'arriveStationCode': 'ST0636',
                      'departCityName': '东莞',
                      'departDate': departDate, 'departDistrictName': '', 'departStationCode': 'ST0088', 'lineIds': '',
                      'lineType': '2', 'searchCombined': '0'}
                #格式化日期，按照2020-05-12格式输出。将该格式输出道数据 d中。

                r = requests.post(url, d1, headers=header)


            if(localtime.tm_wday == 4):

                print(departDate)
                d5 = {'arriveCityName': '东莞', 'arriveDistrictName': '', 'arriveStationCode': 'ST0567',
                      'departCityName': '深圳',
                      'departDate': departDate, 'departDistrictName': '', 'departStationCode': 'ST0122', 'lineIds': '',
                      'lineType': '2', 'searchCombined': '0'}
                r = requests.post(url, d5, headers=header)
                # post 请求中的中文编码？

                # 对数据进行多层分解

            result = eval(r.text)
            result = result['data']
            if len(result['busList']):
                print("有票了")
                # 判断是否已经发送过邮件了，发送过邮件的日期存放于数组中。

                if (departDate not in departDateList):
                    emailmodule.mailsendrun(departDate)
                    count+=1
                    if (count>=2):
                        print("一次性发了两封邮件了，睡眠3天")
                        time.sleep(259200)

                        count = 0
                    departDateList.append(departDate)
                    # 为了防止存放数组过长，当数组长度大于20时，弹出最前面的日期。
                    if (len(departDateList) > 20):
                        departDateList.pop(0)
            print(result)
            # print(r.text)
        else:
            continue
            print(localtime)

    #2个小时查询一次
    time.sleep(7200)












