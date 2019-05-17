#1 -1 的缺失值转为空
#2 ad_industry_id 中有，分割的多个值，拆为多行
# file=open("H:\\qq\\result\\totalExposureLog_count1_static_1000.txt","r")
# file_res=open("H:\\qq\\result\\totalExposureLog_count1_static_1000_v1.csv","w")

file=open("H:\\qq\\result\\totalExposureLog_count1_static.txt","r")
file_res=open("H:\\qq\\result\\totalExposureLog_count1_static.csv","w")
header="sample_id,id,time,material_size,ad_industry_id,product_type,product_id,ad_count_id,price,label\n"
file_res.write( header)
file=file.readlines()
index=0
for line in file[1:]:
    line_list=line.strip().split("\t")
    # print( line_list)
    # print(len(line_list))
    str1=line_list[3]#ad_industry_id
    product_id=line_list[5]
    material_size=line_list[2]

    # product_id=line_list[6]
    # if product_id=="-1":
    #     product_id=""
    # if str1=="-1":
    #     str1=""
    if "," in product_id:
        product_id_list=product_id.strip().split(",")
        for item1 in product_id_list:
            if "," in str1:
                str_list=str1.split(",")
                for  item in str_list:
                    index+=1
                    res=str(index)+","+line_list[0]+","+line_list[1]+","+line_list[2]+","+item+","+line_list[4]+","+item1+","+line_list[6]+","+line_list[7]+","+line_list[8]+"\n"
                    # print("res")
                    # print(line_list)
                    # print(res)
                    file_res.write(res)
            else:
                index += 1
                res=str(index)+","+line_list[0]+","+line_list[1]+","+line_list[2]+","+str1+","+line_list[4]+","+item1+","+line_list[6]+","+line_list[7]+","+line_list[8]+"\n"
                file_res.write(res)
    else:
        if "," in str1:
            str_list = str1.split(",")
            for item in str_list:
                index += 1
                res = str(index) + "," + line_list[0] + "," + line_list[1] + "," + line_list[2] + "," + item + "," + \
                      line_list[4] + "," + product_id + "," + line_list[6] + "," + line_list[7] + "," + line_list[8] + "\n"
                # print("res")
                # print(line_list)
                # print(res)
                file_res.write(res)
        else:
            index += 1
            res = str(index) + "," + line_list[0] + "," + line_list[1] + "," + line_list[2] + "," + str1 + "," + \
                  line_list[4] + "," + product_id + "," + line_list[6] + "," + line_list[7] + "," + line_list[8] + "\n"
            file_res.write(res)

file_res.close()
#43253,219111,1543397154,1,164,8,6199,28123,5206,35,1



