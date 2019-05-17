#素材尺寸 有多值，拆行
# file=open("H:\\qq\\result\\totalExposureLog_count1_static_1000.txt","r")
# file_res=open("H:\\qq\\result\\totalExposureLog_count1_static_1000_v1.csv","w")

file=open("H:\\qq\\totalExposureLog_uniq\\totalExposureLog_count1_static_uniq.txt ","r")
file_res=open("H:\\qq\\totalExposureLog_uniq\\totalExposureLog_count1_static_uniq_res.txt","w")
header="sample_id,id,time,material_size,ad_industry_id,product_type,product_id,ad_count_id,price,label\n"
header="sample_id\tid\ttime\tmaterial_size\tad_industry_id\tproduct_type\tproduct_id\tad_count_id\tprice\tlabel\n"
file_res.write( header)
file=file.readlines()
index=0
for line in file:
    if line.startswith("id"):
        pass
    else:
        line_list=line.strip().split("\t")
        # print( line_list)
        # print(len(line_list))
        material_size=line_list[2]

        # str1=line_list[3]#ad_industry_id
        product_id=line_list[5]
        if "," in product_id:
            print( )
            print( product_id)
        line_list[5]="".join(line_list[5].split(","))
        # product_id=line_list[6]
        # if product_id=="-1":
        #     product_id=""
        # if str1=="-1":
        #     str1=""
        if "," in material_size:
            # print(material_size)
            material_size_list=material_size.strip("\"\"").split(",")
            for item1 in material_size_list:
                index+=1
                print( item1)
                res=str(index)+"\t"+line_list[0].strip("\"")+"\t"+line_list[1].strip("\"")+"\t"+item1+"\t"+line_list[3].strip("\"")+"\t"+line_list[4].strip("\"")+"\t"+line_list[5].strip("\"")+"\t"+line_list[6].strip("\"")+"\t"+line_list[7].strip("\"")+"\t"+line_list[8].strip("\"")+"\n"
                file_res.write(res)
        else:
            index += 1
            res = str(index) + "\t" + line_list[0].strip("\"") + "\t" + line_list[1].strip("\"") + "\t" + line_list[2].strip("\"") + "\t" + line_list[3].strip("\"")+ "\t" + \
                        line_list[4].strip("\"") + "\t" +  line_list[5].strip("\"") + "\t" + line_list[6].strip("\"") + "\t" + line_list[7].strip("\"") + "\t" + line_list[8].strip("\"") + "\n"
                    # print("res")
                    # print(line_list)
                    # print(res)
            file_res.write(res)

file_res.close()
#43253,219111,1543397154,1,164,8,6199,28123,5206,35,1



