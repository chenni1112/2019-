# file=open("H:\\qq\\result\\lgv_v2\\from_all_data\\submission_before.csv","r")
import math

res_file=open("submission.csv","w")
# file=file.readlines()
# id_dict={}
# id_price_dict={}

known_sample=open("../totalExposureLog_count1_static_uniq_average_process.txt","r")
known_sample=known_sample.readlines()
known_sample_dict={}
for line in known_sample:
    line_list=line.strip().split("\t")
    known_sample_dict[line_list[0] ]=line_list[-1]

# 预测的文件
file=open("lgb_submission_new_static.csv","r")
file=file.readlines()
same_sample_target_dict={}
yuce_value=[]
for line in file:
    if line.startswith("id"):
        pass
    else:
        line_list=line.strip().split(",")
        # print("line_list" )
        # print(line_list )
        # print(line_list[0] )
        # print(line_list[0].split(".")  )
        id=line_list[0].split(".")[0]
        # print("id")
        # print(id)
         # 根据第一个id 找到sample id 和bid
        yuce_value.append(float(line_list[1] ))
        same_sample_target_dict[str(int(id))]=str(float(line_list[1]))
max_value=max(yuce_value)
min_value=min(yuce_value)
same_sample_target_dict1={}
for key2 in same_sample_target_dict:
    same_sample_target_dict1[key2]=((float(same_sample_target_dict[key2])-min_value)/(max_value-min_value  ))*25
    # if float(same_sample_target_dict[key2 ])>float(0):
    #     same_sample_target_dict1[key2]=( math.log(float(same_sample_target_dict[key2])+1))*2.2
    # else:
    #     same_sample_target_dict1[key2]=((float(same_sample_target_dict[key2])-min_value)/(max_value-min_value  ))*32



# test 的bid
# print( same_sample_target_dict)
test_file=open("../Btest_sample_new.dat","r")
test_file=test_file.readlines()
test_bid_dict={}
sample_bid_id={}
count=0
known_sample_list=[]
for line in test_file:
    if line.startswith("sample"):
        pass
    else:
        line_list=line.strip().split("\t")
        # print("line_list")
        # print(line_list)

        key1=line_list[1]+"_"+line_list[10] # sample id 和bid
        print(key1)
        if line_list[1] in known_sample_dict:

            count +=1
            known_sample_list.append( float(known_sample_dict[line_list[1]]))

            # value=float(known_sample_dict[line_list[1]])
            # value=float(same_sample_target_dict1[line_list[1] ])
            # value += float(line_list[10])/10000
        else:
            pass
min_know_sample=min(known_sample_list)
max_know_sample=max(known_sample_list)
mean1=sum(known_sample_list )/len( known_sample_list)
know_after=[]
new_list=[]
for line in test_file:
    if line.startswith("sample"):
        pass
    else:
        line_list=line.strip().split("\t")
        # print("line_list")
        # print(line_list)

        key1=line_list[1]+"_"+line_list[10] # sample id 和bid
        print(key1)
        if line_list[1] in known_sample_dict:

            # count +=1
            # known_sample_list.append( float(known_sample_dict[line_list[1]]))

            value=((float(known_sample_dict[line_list[1]])-min_know_sample)/(max_know_sample-min_know_sample))*5100
            # value=float(same_sample_target_dict1[line_list[1] ])
            value += float(line_list[10])/10000
            know_after.append( value)

        else:
            # 
            value=float(same_sample_target_dict1[line_list[1] ])

            if value>=0:
                value += float(line_list[10])/10000
                new_list.append( value)
            else:
                value=0+float(line_list[10])/10000
                new_list.append( value)

        res= line_list[0] +","+str(value )
        res_file.write( res+"\n")


mean2=sum(know_after )/len( know_after)
mean3=sum(new_list )/len( new_list)
print("mean1")
print(mean1)
print("mean2")
print(mean2)
print("mean3")
print(mean3)
res_file.close()
print("count")
print(count)
        # test_bid_dict[line_list[1]]=int(line_list[10])
        # sample_bid_id[line_list[0]]=key1