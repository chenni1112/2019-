bid_id_count={}
file=open("H:\\qq\\result\\totalExposureLog_count.txt","r")
file=file.readines()

test_file=open("/data1/data/chenli/for_25/test_sample.txt","r")
test_known_res=open("/data1/data/chenli/for_25/known_sample_submission.txt","w")
test_unknown=open("/data1/data/chenli/for_25/unknown_sample.txt","w")
test_file=test_file.readlines()

for line in file:
    line_list=line.strip().split("\t")
    if line_list[0] in bid_id_count:
        bid_id_count[line_list[0]].append(int(line_list[3]))
    else:
        bid_id_count[line_list[0]]=int(line_list[3])

count=0
for line in test_file:
    line_list=line.strip().split("\t")
    # print("line_list")
    # print( line_list)
    key2=line_list[1]+"_"+line_list[10]
    # print("key2")
    # print(key2)
    if key2 in bid_id_count:
        # print(key2)
        count +=1
        res=line_list[0]+"\t"+str(sum(bid_id_count[key2])/len( bid_id_count[key2]))
        test_known_res.write( res+"\n" )
    else:
        test_unknown.write( line )

test_known_res.close()
test_unknown.close()

