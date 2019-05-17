# 对每个id 记录每天的修改值，每个id 的value为一个list，记录时间
# 保存每个有效段，然后看曝光是否是在有效段内
file=open("H:\\qq\\ad_operation.dat","r")
file=file.readlines()
id_value_dict={}
id_time_price_dict={}
for line in file:
    line_list=line.strip().split("\t")
    if line_list[2]=="1" and line_list[3]=="2":
        time=line_list[1]
        id_time_price_dict[line_list[0]+"_"+time]=line_list[4]
        if line_list[0] in id_value_dict:
            id_value_dict[line_list[0]].append(int(time))
        else:
            id_value_dict[line_list[0]]=[int(time)]
# print("id_time_price_dict")
# print(id_time_price_dict)
for key1 in id_value_dict:
    new_value_list=[]
    new_price_list=[]
    value_sort_list=id_value_dict[key1]
    value_sort_list.sort()
    # print(value_sort_list)
    for  i in range(len(value_sort_list)):
        value=value_sort_list[i]
        value_1=value+1000000
        for value1 in value_sort_list[i+1:]:
            if value1<value and id_time_price_dict[key1+"_"+str(value_1day)] !=id_time_price_dict[key1+"_"+str(value)]:
                pass
            else:
                new_value_list.append(  value)
                new_price_list.append(id_time_price_dict[key1+"_"+str(value)]  )
    print("value_sort_list")
    print(value_sort_list)
    print(new_value_list)
    print(new_price_list)









