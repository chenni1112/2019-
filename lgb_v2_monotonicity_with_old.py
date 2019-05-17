# file=open("H:\\qq\\result\\lgv_v2\\from_all_data\\submission_before.csv","r")
res_file=open("H:\\qq\\result\\lgv_v2\\lgb_submission_with_price_size_id\\submission.csv","w")
# file=file.readlines()
# id_dict={}
# id_price_dict={}

known_sample=open("H:\\qq\\result\\lgv_v2\\from_all_data\\known_sample_submission.txt","r")
known_sample=known_sample.readlines()
known_sample_dict={}
for line in known_sample:
    line_list=line.strip().split("\t")
    known_sample_dict[line_list[1]+"_"+line_list[10] ]=line_list[11]
# test 的bid/10000
test_file=open("H:\\qq\\result\\test_sample.dat","r")
test_file=test_file.readlines()
test_bid_dict={}
sample_bid_id={}
for line in test_file:
    if line.startswith("样本"):
        pass
    else:
        line_list=line.strip().split("\t")
        # print("line_list")
        # print(line_list)

        key1=line_list[1]+"_"+line_list[10] # sample id 和bid
        print(key1)
        test_bid_dict[key1]=int(line_list[10])/10
        sample_bid_id[line_list[0]]=key1
# 预测的文件
file=open("H:\\qq\\result\\lgv_v2\\lgb_submission_with_price_size_id\\lgb_submission_with_price_size_id.csv","r")
file=file.readlines()
same_sample_count_dict={}
same_sample_bid_dict={}
count=0
for line in file:
    if line.startswith("sample"):
        pass
    else:
        line_list=line.strip().split(",")
        id=line_list[0]
         # 根据第一个id 找到sample id 和bid
        key2=sample_bid_id[id]
        sample_id=key2.split("_")[0]
        bid=key2.split("_")[1]
        # 把sample id 相同的放在dict 中
        # print(key2)
        if key2 in known_sample_dict:
            count+=1
            print(key2)
            value=known_sample_dict[key2]
        elif float(line_list[0])<0:
            value = test_bid_dict[key2]
        else:
            value=line_list[0]
        if sample_id in same_sample_count_dict:
            same_sample_count_dict[sample_id].append(float( value) )
        else:
            same_sample_count_dict[sample_id]=[float(value)]
        if sample_id in same_sample_bid_dict:
            same_sample_bid_dict[sample_id].append( int(bid))
        else:
            same_sample_bid_dict[sample_id]=[int(bid)]
print(count)
id_dict_mean={}
id_price_dict_mean={}
for key1 in same_sample_count_dict:
    id_dict_mean[key1]=sum(same_sample_count_dict[key1 ])/len(same_sample_count_dict[key1])
    id_price_dict_mean[key1] = sum(same_sample_bid_dict[key1]) / len(same_sample_bid_dict[key1])

for line in test_file:
    if line.startswith("样本"):
        pass
    else:
        line_list=line.strip().split("\t")
        bid=(float(line_list[10])/id_dict_mean[line_list[1]])*id_price_dict_mean[line_list[1]]
        # print(bid)

        res=line_list[0]+","+str(bid)+"\n"
        res_file.write(res)

        # print(res)
res_file.close()

