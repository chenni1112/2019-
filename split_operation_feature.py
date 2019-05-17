# 切分ad_operation.dat 中操作后的字段值：
# 投放时段,人群定向,出价（单位分）:广告状态取值,投放时段,人群定向,出价,,
ad_operation_time_price_res=open("H:\\qq\\result\\ad_operation_time_price.txt","w")
ad_operation_file=open("H:\\qq\\ad_operation.dat","r")
ad_operation_file=ad_operation_file.readlines()
id2_dict={}
id1_dict={}
id3_dict={}
for line in ad_operation_file[1:]:
    line_list=line.strip().split("\t")
#     print(line_list[4])
    id0=line_list[0]
    time=line_list[1]
    print(time)

    if  ":" in line_list[4] :
        # print(line_list[4])

        id2=line_list[4]
        if id0 in id2_dict:
            # print("id2")
            # print(id0)
            # print(id2)
            # print(id2_dict[id0])
            # print(id2_dict)
            # break
            id2_dict[id0] =  id2_dict[id0]+"|"+id2
        else:
            # print( id0)
            id2_dict[id0]=id2
    elif "," in  line_list[4] and ":" not in line_list[4] :
        # print(line_list[4])
        id1=line_list[4]
        if id0 in id1_dict:
            pass
            # print("id1")
            # print(id0)
            # print(id1)
            # print(id1_dict[id0])
            # print(id1_dict)
            # break
        else:
            id1_dict[id0] = id1
    elif  line_list[3]=="2" :
        id3=line_list[4]
        if id0+"|"+ time in id3_dict:
            # pass
            # print("id3")
            # print(time)
            # print(id0)
            # print(id3)
            # print(id3_dict[id0+"|"+ time])
            # break
            id3_dict[id0 + "|" + time].append(id3)
        else:
            id3_dict[id0+"|"+ time] =[ id3]
print( len(id3_dict))
print( len(id1_dict))
print( len(id2_dict))

    # res=id0+"\t"+id1+"\t"+id2+"\t"+id3+"\n"
        # print(line_list[4])
    # ad_operation_file_res.


for key1 in id3_dict:
    id=key1.split("|")[0]
    time1=key1.split("|")[1]
    value=",".join(id3_dict[key1])
    res=id +"\t"+ time1 +"\t"+value+"\n"
    ad_operation_time_price_res.write( res)
ad_operation_time_price_res.close()
