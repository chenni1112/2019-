# 10 号修改了 11没修改，11号的可以用，10和11都修改了，不能用
ad_operation=open("H:\\qq\\ad_operation.dat","r")
ad_operation_res=open("H:\\qq\\ad_operation_xiugai_time_price.txt","w")
ad_operation_res_no_ok=open("H:\\qq\\result\\5_完整时间\\ad_operation_xiugai_no_ok_time.txt","w")
ad_operation_res1=open("H:\\qq\\result\\5_完整时间\\ad_operation_create_time_price.txt","w")
ad_operation=ad_operation.readlines()
# 统计bid 一天时间 没有修改的广告id
id_gai_time_bid={}
id_gai_time_quanbu_list={} # 全部的time 和value
id_gai_time_no_ok_list={} # 不ok的time
id_crate_bid={}
for line in ad_operation:
    line_list=line.strip().split("\t")
    # 出价被修改的
    bid_label=line_list[3]
    id=line_list[0]
    value=line_list[4]
    # 记录刚刚创建时候的价格
    if bid_label=="2" and  line_list[2]=="2":
        id_crate_bid[id]=value
    if bid_label=="2" and  line_list[2]=="1":
        time = line_list[1][0:8]
        value1 = time + "_" + value
        key1=id +"_"+time
        if key1 in id_gai_time_quanbu_list:
            id_gai_time_quanbu_list[key1].append(value)
        else:
            id_gai_time_quanbu_list[key1] = [value]
for key2 in id_gai_time_quanbu_list:
    value2=list(set(id_gai_time_quanbu_list[key2]))
    if len(value2)==1:
        res=key2.split("_")[0]+"\t" +key2.split("_")[1]+"\t"+ value2[0]+"\n"
        ad_operation_res.write(res+"\n")
    else:
        res = key2.split("_")[0] + "\t" + key2.split("_")[1]
        ad_operation_res_no_ok.write(res + "\n")

ad_operation_res.close()
for key3 in id_crate_bid:

    ad_operation_res1.write(key3+"\t"+id_crate_bid[key3]+"\n")

ad_operation_res1.close()
ad_operation_res_no_ok.close()



