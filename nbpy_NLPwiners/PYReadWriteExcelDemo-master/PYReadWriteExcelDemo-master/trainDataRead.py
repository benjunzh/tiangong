
import pandas as pd
import numpy as np

def tongji_data(data):
    data_new = data.copy()

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
        # percentage_i = float(len(df_1))/float(res_one)
        print("获赔为1数量:%d"%res_one)
        print("总长度:%d"%len_sum)
        print("获赔概率：%.4f"%percentage_i)
    else:
        percentage_i = 0
        print("注意：此案例样本不足!")

    return percentage_i

name_arrary = []
key_dict = {}
levelPercentage = []

def read2(filename):
    # trainData.csv
    # path = ''+data()
    # df = pd.read_csv(path)
    df = pd.read_csv(filename)
    df_0 = []
    df_1 = []
    df_2 = []
    df_3 = []
    df_4 = []
    min_num = 4
    print("行总数:%d"%len(df))
    print("列总数:%d"%len(df.columns))
    for row in range(0,len(df)):
        # print(len(df))
        min_num = 0
        min_num_check = 0
        # 遍历列
        for col in range(0,len(df.columns)-1):
            # print(len(df.columns))
            if(min_num_check == 0 and df.iloc[row,col] != 0):
                min_num = df.iloc[row,col]
                min_num_check = df.iloc[row,col]
                if df.columns[col] not in key_dict.keys():
                    key_dict[df.columns[col]] = df.iloc[row, col]
                    print("%s:%d" % (df.columns[col], key_dict[df.columns[col]]))

                    name_arrary.append(df.columns[col])

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

# 概率判断
        df_1_percentage = get_percentage_fun(df_1)
        if df_1_percentage >= 0.7:
            df_1_percentage = get_percentage_fun(df_1)
        else:
            df_1_percentage = 1.0

    df_2_percentage = get_percentage_fun(df_2)
    if df_2_percentage >= 0.5:
        df_2_percentage = get_percentage_fun(df_2)
    else:
        df_2_percentage = get_percentage_fun(df_2) + 0.3

    df_3_percentage = get_percentage_fun(df_3)
    if df_3_percentage >= 0.3:
        df_3_percentage = get_percentage_fun(df_3)
    else:
        df_3_percentage = get_percentage_fun(df_3) + 0.2

    df_4_percentage = get_percentage_fun(df_4)
    if df_4_percentage >= 0.1:
        df_4_percentage = get_percentage_fun(df_4)
    else:
        df_4_percentage = get_percentage_fun(df_4) + 0.1


    if True:
        # print("优先级0数据长度:%d"%len(df_0))
        print("最大优先级为1的数据长度:%d"%len(df_1))
        print("最大优先级为2的数据长度:%d"%len(df_2))
        print("最大优先级为3的数据长度:%d"%len(df_3))
        print("最大优先级为4的数据长度:%d"%len(df_4))


        print("优先级1获赔概率：%.4f" % df_1_percentage)
        print("优先级2获赔概率：%.4f" % df_2_percentage)
        print("优先级3获赔概率：%.4f" % df_3_percentage)
        print("优先级4获赔概率：%.4f" % df_4_percentage)
        print("关键字：键值对应 %s" % key_dict)
        print("###################################################################################")
        levelPercentage.append(df_1_percentage)
        levelPercentage.append(df_2_percentage)
        levelPercentage.append(df_3_percentage)
        levelPercentage.append(df_4_percentage)
