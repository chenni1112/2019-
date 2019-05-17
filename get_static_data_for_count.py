# for_train_file.write("广告id\t创建时间\t素材尺寸\t广告行业\t商品类型\t商品\t广告账户\n")
# ad_static_feature.out 得到id 属性的字典

# 一部分train 数据
ad_static_file = open('H:\\qq\\ad_static_feature.out', "r")
#ad_static = ad_static.sort_values(by=[0, 1])
ad_static_file=ad_static_file.readlines()
for_train_file=open("H:\\qq\\result\\for_train1.txt","w")
for_train_file_dict={}
for line in ad_static_file:
    if line.startswith("广告 id"):
        pass
    else:
        # print(line)
        line_list=line.strip().split("\t")
        # print(line_list)
        if len(line_list)==6:
            res_str =line_list[0] + "\t" + line_list[1] + "\t" + "-1" + "\t" + line_list[5] + "\t" + line_list[4] + "\t" + line_list[3] + "\t" + line_list[2] + "\n"
        else:
            res_str=line_list[0]+"\t"+line_list[1]+"\t"+line_list[6]+"\t"+line_list[5]+"\t"+line_list[4]+"\t"+line_list[3]+"\t"+line_list[2]+"\n"
        for_train_file_dict[line_list[0]]=res_str

totalExposureLog_count=open("H:\\qq\\result\\totalExposureLog_count.txt","r")
totalExposureLog_count_static=open("H:\\qq\\result\\totalExposureLog_count1_static.txt","w")
totalExposureLog_count=totalExposureLog_count.readlines()
totalExposureLog_count_static.write("id\ttime\tmaterial_size\tad_industry_id\tproduct_type\tproduct_id\tad_count_id\n")
for line in totalExposureLog_count:
    line_list=line.strip().split("\t")
    id=line_list[0]
    # print (  line_list)
    if id in  for_train_file_dict:
        # print("id")
        # print(id)
        # print(id)
        res = for_train_file_dict[ id ].strip("\n") + "\t" + line_list[1] + "\t" + line_list[3]
        if id =="222150":
            print(  line_list)
            print(res)

    else:
        res = id+"\t\t\t\t\t\t\t" + line_list[1] + "\t" + line_list[3]
    totalExposureLog_count_static.write(res+"\n")