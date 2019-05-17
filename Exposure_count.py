# 统计每个id 在每个bid 下的每天的曝光量
import time, datetime
from dateutil.parser import parse
# from datetime import datetime
totalExposureLog = open('H:\\qq\\dat_top10K\\totalExposureLog_top10000.out', "r")
totalExposureLog_count = open('H:\\qq\\dat_top10K\\totalExposureLog_count.txt', "w")
totalExposureLog=totalExposureLog.readlines()

# a = parse('2017-10-01/12:12:12')
Expo_count={}
for line in totalExposureLog[1:]:
    line_list=line.strip().split("\t")
    id=line_list[4]
    price=line_list[6]
    time=int(line_list[1])
    #时间戳转换为指定格式
    # print("time")
    # print(time)

    dateArray = datetime.datetime.utcfromtimestamp(time)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S.%f")
    # print(  otherStyleTime)
    # print("type")
    # print(type( otherStyleTime))
    otherStyleTime1=datetime.datetime.strptime(otherStyleTime, "%Y-%m-%d %H:%M:%S.%f")
    # print(type( otherStyleTime1))
    # print(otherStyleTime1)
    # print(" a-time")
    # print((otherStyleTime1 - a).days)
    # print((otherStyleTime1-a ).total_seconds() )# 时间差
    # break
    time1=otherStyleTime.split(" ")[0]
    key1=id+"|"+price+"|"+time1
    # print("key1")
    # print(key1)
    if key1 in Expo_count:
        Expo_count[key1]+=1
    else:
        Expo_count[key1] = 1
for k1 in Expo_count:
    totalExposureLog_count.write(k1+"\t"+str(Expo_count[k1])+"\n")

totalExposureLog_count.close()


    # print(  time1)
    # break



# ad_operation_time_price_res=open("H:\\qq\\result\\ad_operation_time_price.txt","w")
# ad_operation_file=open("H:\\qq\\ad_operation.dat","r")
# ad_operation_file=ad_operation_file.readlines()