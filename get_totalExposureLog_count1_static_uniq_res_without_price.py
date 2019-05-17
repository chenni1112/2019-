file=open("H:\\qq\\result\\4_train_data_without_bid\\totalExposureLog_count1_static_uniq_res.txt","r")
file_res=open("H:\\qq\\result\\4_train_data_without_bid\\totalExposureLog_count1_static_uniq_res_without_price_float.txt","w")
file=file.readlines()
id_count_dict={}
header="id\ttime\tmaterial_size\tad_industry_id\tproduct_type\tproduct_id\tad_count_id\tlabel"
id_count_other_dict={}
for line in file:
    if line.startswith("sample"):
        pass
    else:
        line_list=line.strip().split("\t")
        if line_list[1] in id_count_dict:
            id_count_dict[line_list[1]].append(int(line_list[-1]))
        else:
            id_count_dict[line_list[1]]=[int(line_list[-1])]
            id_count_other_dict[line_list[1]]=line_list
print(len(id_count_other_dict))
file_res.write(header+"\n")
for key1 in  id_count_dict:
    value_list=id_count_other_dict[key1]
    value_list[8]=str(sum(id_count_dict[key1])/len( id_count_dict[key1]))
    res="\t".join(value_list[1:9])+"\n"
    file_res.write(res)
file_res.close()



