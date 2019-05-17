# file=open("H:\\qq\\result\\lgv_v2\\from_all_data\\submission_before.csv","r")
res_file=open("H:\\qq\\result\\4_train_data_without_bid\\lgb_submission_size_id_log_CV3_no_product_type_no_price\\submission.csv","w")
# file=file.readlines()
# id_dict={}
# id_price_dict={}

known_sample=open("H:\\qq\\result\\4_train_data_without_bid\\totalExposureLog_count1_static_uniq_res_without_price_float.txt","r")
known_sample=known_sample.readlines()
known_sample_dict={}
for line in known_sample:
    line_list=line.strip().split("\t")
    known_sample_dict[line_list[0] ]=line_list[-1]

# 预测的文件
file=open("H:\\qq\\result\\4_train_data_without_bid\\lgb_submission_size_id_log_CV3_no_product_type_no_price\\lgb_submission_size_id_log_CV3_no_product_type_no_price.csv","r")
file=file.readlines()
same_sample_target_dict={}
for line in file:
    if line.startswith("id"):
        pass
    else:
        line_list=line.strip().split(",")
        id=line_list[0]
         # 根据第一个id 找到sample id 和bid
        same_sample_target_dict[id]=line_list[1]

# test 的bid
test_file=open("H:\\qq\\result\\test_sample.dat","r")
test_file=test_file.readlines()
test_bid_dict={}
sample_bid_id={}
count=0
for line in test_file:
    if line.startswith("样本"):
        pass
    else:
        line_list=line.strip().split("\t")
        # print("line_list")
        # print(line_list)

        key1=line_list[1]+"_"+line_list[10] # sample id 和bid
        print(key1)
        if line_list[1] in known_sample_dict:
            count +=1
            value=float(known_sample_dict[line_list[1]])
            value += float(line_list[10])/10000
        else:
            value=float(same_sample_target_dict[line_list[1] ])

            if value>=0:
                value += float(line_list[10])/10000
            else:
                value=0+float(line_list[10])/10000
        res= line_list[0] +","+str(value )
        res_file.write( res+"\n")

res_file.close()
        # test_bid_dict[line_list[1]]=int(line_list[10])
        # sample_bid_id[line_list[0]]=key1