# 去掉素材尺寸为空，行业id 有多值的记录，商品id 为-1和行业id 为-1 变成0，素材尺寸 有多值，不去掉。商品id 中的619,928,123 不是多值。
ad_static_file = open('H:\\qq\\ad_static_feature.out', "r")
ad_static_file_res = open('H:\\qq\\ad_static_feature_filter.out', "w")
#ad_static = ad_static.sort_values(by=[0, 1])
ad_static_file=ad_static_file.readlines()
for line in ad_static_file:
    line_list=line.strip().split("\t")
    # print( line_list )
    if len(line_list )==6:
        pass
    elif "," in  line_list[5]:
        pass
    else:
        if line_list[3] =="-1":
            line_list[3] ="0"
        if line_list[5] =="-1":
            line_list[5] = "0"
        str1="\t".join(line_list )
        # print (str1 )
        ad_static_file_res.write(str1+"\n")
ad_static_file_res.close()

