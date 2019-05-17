file=open("H:\\qq\\result\\totalExposureLog_count1_static.csv","r")
file=file.readlines()
for line in file:
    line_list=line.strip().split(",")
    if len(line_list) !=10:
        print("line")
        print(line)
        print(line_list)