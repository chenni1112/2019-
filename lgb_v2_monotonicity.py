file=open("H:\\qq\\result\\lgv_v2\\lgb_submission_no_price_size_id_log\\submission_for_monotonicity.csv","r")
res_file=open("H:\\qq\\result\\lgv_v2\\lgb_submission_no_price_size_id_log\\调过单调性的\\submission_res.csv","w")
file=file.readlines()
id_dict={}
id_price_dict={}
for line in file:
    if line.startswith("sample"):
        pass
    else:
        line_list=line.strip().split(",")
        # print( line_list)
        if line_list[1] in id_dict:
            id_dict[line_list[1]].append(float(line_list[3]))
            id_price_dict[line_list[1]].append(float(line_list[2]))
        else:
            id_dict[line_list[1]]=[float(line_list[3])]
            id_price_dict[line_list[1]]=[float(line_list[2])]

id_dict_mean={}
id_price_dict_mean={}
for key1 in id_dict:
    id_dict_mean[key1]=sum(id_dict[key1 ])/len(id_dict[key1])
    id_price_dict_mean[key1] = sum(id_price_dict[key1]) / len(id_price_dict[key1])
for line in file:
    if line.startswith("sample"):
        pass
    else:
        line_list = line.strip().split(",")

        # print("res")
        # print(line_list )
        # print(float(line_list[3]))
        # print(id_dict_mean[line_list[1]])
        # print(id_price_dict_mean[line_list[1]])
        bid=(float(line_list[3])/id_dict_mean[line_list[1]])*id_price_dict_mean[line_list[1]]
        # print(bid)
        res=line.strip()+","+str(bid)+"\n"
        print(res)
        res_file.write(res)

        # print(res)
res_file.close()

