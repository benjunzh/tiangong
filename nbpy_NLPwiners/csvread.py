
import pandas as pd
import numpy as np



def get_percentage_fun(df_num):
    res_one = float()
    len_sum = len(df_num)
    percentage_i = float(0)
    for i in range(0,len_sum):
        # print(df_num[i].loc['是否获赔'])
        if df_num[i].loc['是否获赔']==1:
            res_one += 1
    if len_sum != 0:
        percentage_i = float(res_one)/float(len_sum)
        print("获赔为1数量:%d"%res_one)
        print("总长度:%d"%len_sum)
        print("获赔概率：%.4f"%percentage_i)
    return percentage_i

if __name__=="__main__":
    df = pd.read_csv("junjun.csv")
    df_0 = []
    df_1 = []
    df_2 = []
    df_3 = []
    df_4 = []
    key_dict = {}
    min_num = 4
    print("行总数:%d"%len(df))
    print("列总数:%d"%len(df.columns))
    for row in range(0,len(df)):
        # print(len(df))
        min_num = 0
        min_num_check = 0
        for col in range(0,len(df.columns)-1):
            # print(len(df.columns))
            if(min_num_check == 0 and df.iloc[row,col] != 0):
                min_num = df.iloc[row,col]
                min_num_check = df.iloc[row,col]
                if df.columns[col] not in key_dict.keys():
                    key_dict[df.columns[col]] = df.iloc[row, col]
                    print("%s:%d" % (df.columns[col], key_dict[df.columns[col]]))
                if df.columns[col] in key_dict.keys() and key_dict[df.columns[col]] < df.iloc[row,col]:
                    key_dict[df.columns[col]] = df.iloc[row,col]
                    print("%s:%d"%(df.columns[col],key_dict[df.columns[col]]))
                # print("%s:%d"%(df.columns[col],key_dict[df.columns[col]]))
            if(df.iloc[row,col] != 0 and df.iloc[row,col]<min_num):
                min_num = df.iloc[row,col]
        if min_num != 0:
            if min_num == 1:
                df_1.append(df.iloc[row,:])
            elif min_num == 2:
                df_2.append(df.iloc[row,:])
            elif min_num == 3:
                df_3.append(df.iloc[row,:])
            elif min_num == 4:
                df_4.append(df.iloc[row,:])
        else:
            df_0.append(df.iloc[row, :])

    print("优先级0数据长度:%d"%len(df_0))
    print("优先级1数据长度:%d"%len(df_1))
    print("优先级2数据长度:%d"%len(df_2))
    print("优先级3数据长度:%d"%len(df_3))
    print("优先级4数据长度:%d"%len(df_4))

    df_0_percentage = get_percentage_fun(df_0)
    print("优先级0获赔概率：%.4f" % df_0_percentage)
    df_1_percentage = get_percentage_fun(df_1)
    print("优先级1获赔概率：%.4f" % df_1_percentage)
    df_2_percentage = get_percentage_fun(df_2)
    print("优先级2获赔概率：%.4f" % df_2_percentage)
    df_3_percentage = get_percentage_fun(df_3)
    print("优先级3获赔概率：%.4f" % df_3_percentage)
    df_4_percentage = get_percentage_fun(df_4)
    print("优先级4获赔概率：%.4f" % df_4_percentage)

    print("关键字：键值对 %s" % key_dict)
