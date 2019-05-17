res_file=open("get_five_exposure_count.txt","r")#  只有id，时间，曝光值
res_file=res_file.readlines()
id_count_dict={}
for line in res_file:
	line_list=line.strip().split("\t")
	id=line_list[0]
	time=line_list[1]
	count=line_list[2]
	if id in id_count_dict:
		id_count_dict[id].append(int( count))
	else:
		id_count_dict[id]=[int( count)]

# 得到静态数据
static_file=open("ad_static_feature_filter.out","r")
static_file=static_file.readlines()

for_train_file_dict={}
for line in static_file:
    if line.startswith("广告 id"):
        pass
    else:
        # print(line)
        line_list=line.strip().split("\t")
        # print(line_list)
        if len(line_list)==6:
            print( line_list)
            # res_str =line_list[0] + "\t" + line_list[1] + "\t" + "-1" + "\t" + line_list[5] + "\t" + line_list[4] + "\t" + line_list[3] + "\t" + line_list[2] + "\n"
        else:
            res_str=line_list[0]+"\t"+line_list[1]+"\t"+line_list[6]+"\t"+line_list[5]+"\t"+line_list[4]+"\t"+line_list[3]+"\t"+line_list[2]+"\n"
            for_train_file_dict[line_list[0]]=res_str

totalExposureLog_count_static=open("totalExposureLog_count1_static_uniq_average.txt","w")
totalExposureLog_count_static.write("id\ttime\tmaterial_size\tad_industry_id\tproduct_type\tproduct_id\tad_count_id\tlabel\n")

for key2 in id_count_dict:
    count=sum(id_count_dict[key2])/len( id_count_dict[key2])
    res = for_train_file_dict[ key2 ].strip("\n") + "\t" +str( count)
    if "," in res:
        print(res)
    totalExposureLog_count_static.write(res+"\n")  
