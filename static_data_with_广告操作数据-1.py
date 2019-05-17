import time, datetime
id_gai_time_quanbu_list=open("H:\\qq\\result\\5_完整时间\\ad_operation_xiugai_time_price.txt","r")
id_gai_time_quanbu_list_file=id_gai_time_quanbu_list.readlines()
id_gai_time_quanbu_list_dict={}
# print(id_gai_time_quanbu_list_file )
all_available_id_time_prcie=open("H:\\qq\\result\\5_完整时间\\all_available_id_time_prcie_from_static_and_operation.txt","w")

for line in id_gai_time_quanbu_list_file:
    line_list=line.strip().split("\t")
    # print("line_list")
    # print( line )
    id=line_list[0]
    time=line_list[1]
    price=line_list[2]
    id_gai_time_quanbu_list_dict[id+"_"+time]=price

id_gai_time_create_list=open("H:\\qq\\result\\5_完整时间\\ad_operation_create_time_price.txt","r")
id_gai_time_create_list=id_gai_time_create_list.readlines()
id_gai_time_create_list_dict={}
for line in id_gai_time_create_list:
    line_list=line.strip().split("\t")
    id=line_list[0]
    # time=line_list[1]
    price=line_list[1]
    id_gai_time_create_list_dict[id]=price
# 静态数据
static_file=open("H:\\qq\\result\\5_完整时间\\ad_static_feature_filter.out","r")
static_file=static_file.readlines()
for line in static_file:
    if line.startswith("id"):
        pass
    else:
        line_list=line.strip().split("\t")
        id=line_list[0]
        create_time=line_list[1]
        create_time1=int(create_time)
    #时间戳转换为指定格式
    # print("time")
    # print(time)

        dateArray = datetime.datetime.utcfromtimestamp(create_time1)
        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S.%f")
        time1 = otherStyleTime.split(" ")[0]

        create_time="".join(time1.split("-"))
        print("time1")
        print(create_time)
        if id in id_gai_time_create_list_dict:
            key1=id+"_"+create_time
            create_price = id_gai_time_create_list_dict[id]
            if  key1 in id_gai_time_quanbu_list_dict:
                xiu_gai_price=id_gai_time_quanbu_list_dict[key1]

                if create_price== xiu_gai_price:
                    res=id+"\t"+create_time+"\t"+create_price
                    all_available_id_time_prcie.write( res+"\n")
                else:
                    pass
            else:
                res = id + "\t" + create_time + "\t" + create_price
                all_available_id_time_prcie.write(res + "\n")

        else:
            pass

