# 对每个id 记录每天的修改值，每个id 的value为一个list，记录时间
# 保存每个有效段，然后看曝光是否是在有效段内
import time, datetime
file=open("./ad_operation.dat","r")
file=file.readlines()
id_value_dict={}
id_create_bid_dict={}
# id_price_dict={}
id_time_price_dict={}
for line in file:
    line_list=line.strip().split("\t")
    if line_list[2]=="1" and line_list[3]=="2":
        time=str(int(line_list[1]))
        id_time_price_dict[line_list[0]+"_"+time]=line_list[4]
        if line_list[0] in id_value_dict:
            id_value_dict[line_list[0]].append(int(time))
            # id_price_dict[line_list[0]].append(int(line_list[4]))
        else:
            id_value_dict[line_list[0]]=[int(time)]
    elif line_list[2]=="2" and line_list[3]=="2":
        id_create_bid_dict[line_list[0]]=line_list[4]


            # id_price_dict[line_list[0]]=[int(line_list[4])]
# print("id_time_price_dict")
# print(id_time_price_dict)
id_price_sort_dict={}
id_time_sort_dict={}
for key1 in id_value_dict:
    new_value_list=[]
    new_price_list=[]
    price_sort_list=[]
    value_sort_list=id_value_dict[key1]
    value_sort_list.sort()
    for value in value_sort_list:
        price_sort_list.append(id_time_price_dict[key1+"_"+str(value)] )
    id_price_sort_dict[key1]=price_sort_list
    id_time_sort_dict[key1]=value_sort_list
    # print("value_sort_list")
    # print(value_sort_list)
    # if len(value_sort_list )==1:
    #     new_value_list=value_sort_list
    #     new_price_list=id_time_price_dict[key1+"_"+str(value_sort_list[0])] 


    # else:
    #     # print( "key")
    #     # print( key1)
    #     # print(value_sort_list )
    #     # print(price_sort_list )
    #     for  i in range(len(value_sort_list)):
    #         pass_list=[]
    #         value=value_sort_list[i]

            
    #         # print("value")
    #         # print(value)
    #         # print(value_sort_list[i+1:])
    #         for value2 in value_sort_list[i+1:]:
    #             value1=value+1000000
    #             if str(value2)[5]=="3" and str(value)[5]=="2":
    #                 value1=value+73000000
    #             # print(value1)
    #             # print("value2")
    #             # print(value2)
    #             if value1>value2 and id_time_price_dict[key1+"_"+str(value2)] !=id_time_price_dict[key1+"_"+str(value)]:
    #                 # pass
    #                 pass_list.append("no_pass")
    #             else:
    #                 pass_list.append("pass")
    #         if "no_pass" in pass_list:
    #             pass
    #         else:
    #             new_value_list.append(  value)
    #             new_price_list.append(id_time_price_dict[key1+"_"+str(value)]  )
    #         print("new_value_list ")
    #         print(new_value_list)
    #         print(new_price_list)
    # print("value_sort_list")
    # print(value_sort_list)
    # print(price_sort_list)
    # print(new_value_list)
    # print(new_price_list)


#  读取静态数据 ，获得创建时间
static_file=open("ad_static_feature_filter.out")
static_file=static_file.readlines()
id_create_time_dict={}
for line in static_file:
    line_list=line.strip().split("\t")
    create_time=int(line_list[1])
    id=line_list[0]
    dateArray = datetime.datetime.utcfromtimestamp(create_time)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S.%f")
    # print(" otherStyleTime")
    # print( otherStyleTime)
    time1 = otherStyleTime.split(" ")[0]
    time2=otherStyleTime.split(" ")[1].split(".")[0]
    # print("time")
    # print( time1)
    create_time1="".join(time1.split("-"))
    create_time2="".join( time2.split(":")  )
    id_create_time_dict[id]=create_time1+create_time2
print("len( id_create_time_dict )")
print(len( id_create_time_dict ))
print(len(id_time_sort_dict))
# id,创建2，修改1，time，bid
#如果修改中后一个的价格跟前一个的一样，不记录
# 操作数据中有记录创建bid 的，和有修改记录的
id_time_bid_operation=open("id_time_bid_operation.txt","w")
for id in id_create_time_dict:
    time=id_create_time_dict[id]
    bid=-1

    if id in id_create_bid_dict:
        bid=id_create_bid_dict[id]
        
    before_bid=bid
    res=id+"\t2\t"+str(time)+"\t"+str(bid)+"\n"
    id_time_bid_operation.write(res )
    if id in id_time_sort_dict:
            xiugai_list=id_time_sort_dict[id]
            bid_list=id_price_sort_dict[id]
            for i  in range(len(bid_list)):
                bid=bid_list[i]
                if bid==before_bid:
                    pass
                else:
                    xiugai_time=xiugai_list[i]
                    res=id+"\t1\t"+str(xiugai_time)+"\t"+str(bid)+"\n"
                    before_bid=bid
                    id_time_bid_operation.write(res )
    else:
        pass


id_time_bid_operation.close()





                # id_time_baoguang_count[id+"_"+time[:8]]+=1


                    


















