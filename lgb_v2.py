#历史平均来填充旧广告id的曝光量，新广告id曝光量用广告size、商品id等特征对应历史平均来填充。调整单调性。
file=open("H:\\qq\\totalExposureLog_uniq\\totalExposureLog_count1_static_uniq_res.txt","r")
file=file.readlines()
bid_id_count={}
for line in file:
    line_list=line.strip()
    # print(line_list)
    key1=line_list[1]+"_"+line_list[-2]
    value=line_list[-1]
    if key1 in bid_id_count:
        bid_id_count[key1].append(value)
    else:
        bid_id_count[key1] =[value ]

print(len( bid_id_count))
test_file=open("H:\\qq\\test_sample.dat","r")
test_file=test_file.readlines()
for line in test_file:
    line_list=line.strip().split("\t")
    key2=line_list[1]+"_"+line_list[10]
    if key2 in bid_id_count:
        print(key2)