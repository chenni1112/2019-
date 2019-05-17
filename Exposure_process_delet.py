#没有日期不对的，同一用户，同一广告id，同一请求时间，同一请求id，同一广告位id，同一素材尺寸 #同一请求同一广告位同一广告多次曝光去掉，
import time, datetime
from dateutil.parser import parse
file=open("H:\\qq\\dat_top10K\\totalExposureLog_top10000.out","r")
file=file.readlines()
time_list=[]
for line in file:
    line_list=line.strip().split("\t")
    if line.startswith("广告"):
        # print(line)
        pass
    else:

        time = int(line_list[1])
        dateArray = datetime.datetime.utcfromtimestamp(time)
        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S.%f")
        time1 = otherStyleTime.split(" ")[0]
        # print(time1 )
        time_list.append(time1)

print(list(set(time_list)))



