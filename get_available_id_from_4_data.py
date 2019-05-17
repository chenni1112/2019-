import time, datetime
#使用available id 提取第四版数据中的训练集，就是有完整一天的曝光，以及价格
all_available_id_time_prcie_from_static_and_operation=open("H:\\qq\\result\\5_完整时间\\all_available_id_time_prcie_from_static_and_operation.txt","r")
all_available_id_time_prcie_from_static_and_operation=all_available_id_time_prcie_from_static_and_operation.readlines()
id_time_dict={}
for line in all_available_id_time_prcie_from_static_and_operation:
    line_list=line.strip().split("\t")
    # print(line_list)
    id=line_list[0]
    price=line_list[2]
    time=line_list[1]

# 根据时间和id 筛选， 价格先不管
old_train=open("H:\\qq\\result\\4_train_data_without_bid\\totalExposureLog_count1_static_uniq_res.txt","r")
old_train=old_train.readlines()
for line in old_train:
    if line.startswith("sample"):
        pass
    else:
        line_list=line.strip().split("\t")
        id=line_list[1]
        time=line_list[2]
        time1 = int(time)
        # 时间戳转换为指定格式
        dateArray = datetime.datetime.utcfromtimestamp(time1)
        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S.%f")
        # print("otherStyleTime")
        # print(otherStyleTime)
        time1 = otherStyleTime.split(" ")[0]
        time2 = "".join(time1.split("-"))
        # print("time2")
        # print(time2)

