

# 统计static 中的null 情况
file =open("H:\\qq\\ad_static_feature.out")
file=file.readlines()
time=0
shang_pin_id=0
hang_ye_id=0
sucaichicun=0
for line in file:
    if line.startswith("广告"):
        pass
    else:
        line_list=line.strip().split("\t")
        # print(len(line_list ))
        if line_list[1] =="0":
            time +=1
        elif line_list[3] =="-1":
            shang_pin_id +=1
        elif line_list[5] =="-1":
            hang_ye_id +=1
        elif len(line_list ) ==6:
            sucaichicun +=1

print(time)
print(shang_pin_id)
print(hang_ye_id)
print(sucaichicun)
# 9290
# 238932
# 229
# 135686