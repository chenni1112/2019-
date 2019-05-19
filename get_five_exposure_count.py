#如果在id_time_bid_operation.txt 只有创建数据，统计除了创建时间的每天曝光
# 如果在id_time_bid_operation.txt 只有修改数据,没有这样的数据
# 如果在id_time_bid_operation.txt 有创建和修改数据，统计每天的曝光，去掉有修改天和创建天的记录
import time, datetime
#构建修改的字典
id_time_bid_operation=open("id_time_bid_operation.txt","r")
id_time_bid_operation=id_time_bid_operation.readlines()
create_dict={}
xiugai_dict={}
xiugai_bid_dict={}
for line in id_time_bid_operation:
    line_List=line.strip().split("\t")
    if line_List[1]=="2":
        create_dict[line_List[0]]=line_List
    else:
        xiugai_bid_dict[line_List[0]+"_"+line_List[2]]=line_List[3]#line_List[2] 是时间，3 是出价
        if line_List[0] in xiugai_dict:
            xiugai_dict[line_List[0]].append( line_List[2])
        else:
            xiugai_dict[line_List[0]]=[line_List[2]]
print("len(xiugai_dict)" )
print(len(xiugai_dict) )
print(len(create_dict) )
#曝光数据
file1=open("totalExposureLog_uniq.log","r")
file1=file1.readlines()
id_time_baoguang_count={}
for line in file1:
    line_List=line.strip().split("\t")
    id=line_List[4]
    time1=line_List[1]
    # print(time1 )
    dateArray = datetime.datetime.utcfromtimestamp(int(time1))
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S.%f")
    time1 = otherStyleTime.split(" ")[0]
    time2=otherStyleTime.split(" ")[1].split(".")[0]
    create_time1="".join(time1.split("-"))
    create_time2="".join( time2.split(":")  )
    time=create_time1+create_time2 # 爆光时间
    
    if id in create_dict:

        create_time=create_dict[id][2] #  曝光时间要大于创建时间
        # print(id )
        # print("time" )
        # print(time)
        # print("create_time")
        # print(create_time)
        bid=create_dict[id][3]
        if  not id in xiugai_dict:
            if int(time[:8]) > int(create_time[:8]):
                id_time_baoguang_count.setdefault(id+"_"+time[:8], 1)+1
                id_time_baoguang_count[id+"_"+time[:8] ]=id_time_baoguang_count.setdefault(id+"_"+time[:8], 0)+1
        else:
            xiugai_list=xiugai_dict[id]
            create_xiugai_day_list=[create_time[:8]]
            for xiugai_time in xiugai_list:
                create_xiugai_day_list.append( xiugai_time[:8])

            if int(time[:8]) >int(create_time[:8]) and time[:8] not in create_xiugai_day_list:
                id_time_baoguang_count[id+"_"+time[:8]]=id_time_baoguang_count.setdefault(id+"_"+time[:8], 0)+1
    else:
        pass
# print(id_time_baoguang_count )

res_file=open("get_five_exposure_count.txt","w")#  只有id，时间，曝光值
for  key2 in id_time_baoguang_count:
    res=key2.split("_")[0]+"\t"+key2.split("_")[1]+"\t"+str(id_time_baoguang_count[key2])+"\n"
    res_file.write( res)


#id，时间，曝光值和出价
# 
# file1=open("totalExposureLog_uniq.log","r")
# file1=file1.readlines()
# id_time_baoguang_bid_count={}
# for line in file1:
#     line_List=line.strip().split("\t")
#     id=line_List[0]
#     time1=line_List[1]
#     # print(time1 )
#     dateArray = datetime.datetime.utcfromtimestamp(int(time1))
#     otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S.%f")
#     time1 = otherStyleTime.split(" ")[0]
#     time2=otherStyleTime.split(" ")[1].split(".")[0]
#     create_time1="".join(time1.split("-"))
#     create_time2="".join( time2.split(":")  )
#     time=create_time1+create_time2 # 爆光时间
    
#     if id in create_dict:

#         create_time=create_dict[id][2] #  曝光时间要大于创建时间
#         # print(id )
#         # print("time" )
#         # print(time)
#         # print("create_time")
#         # print(create_time)
#         bid=create_dict[id][3]
#         if  not id in xiugai_dict:
#             if int(time[:8]) > int(create_time[:8]):
#                 id_time_baoguang_count[id+"_"+time[:8]+"_"+bid]=id_time_baoguang_count.setdefault(id+"_"+time[:8]+"_"+bid, 1)+1
#         else:
#             xiugai_list=xiugai_dict[id]
#             create_xiugai_list=[create_time]+xiugai_list
#             create_xiugai_day_list=[create_time[:8]]
#             for xiugai_time in xiugai_list:
#                 create_xiugai_day_list.append( xiugai_time[:8])


#             if int(time[:8]) >int(create_time[:8]) and time[:8] not in create_xiugai_day_list:
#                 # for j in range(len(create_xiugai_list)):
#                 j=0
#                 while create_xiugai_list[j] <time and j<len(create_xiugai_list):
#                         j+=1
#                 bid=xiugai_bid_dict[id+"_"+reate_xiugai_list[j-1]]
#                 id_time_baoguang_count[id+"_"+time[:8]+"_"+bid]=id_time_baoguang_count.setdefault(id+"_"+time[:8]+"_"+bid, 0)+1
# # print(id_time_baoguang_count )
# res_file=open("get_five_exposure_count_bid.txt","w")#  只有id，时间，曝光值
# for  key2 in id_time_baoguang_count:
#     res=key2.split("_")[0]+"\t"+key2.split("_")[1]+"\t"+str(id_time_baoguang_count[key2])+"\n"
#     res_file.write( res)
