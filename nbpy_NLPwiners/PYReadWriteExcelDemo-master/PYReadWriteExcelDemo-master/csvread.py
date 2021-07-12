
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
        print("获赔为1数量:%d"%res_one)
        print("总长度:%d"%len_sum)
        print("获赔概率：%.4f"%percentage_i)
    return percentage_i

#def get_min_tex(df_text):

if __name__=="__main__":
    df = pd.read_csv("dataset.csv")
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
        for col in range(0,len(df.columns)-1):
            # print(len(df.columns))
            if(min_num_check == 0 and df.iloc[row,col] != 0):
                min_num = df.iloc[row,col]
                min_num_check = df.iloc[row,col]
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

   # print("优先级0数据长度:%d"%len(df_0))
    print("最大优先级为1的数据长度:%d"%len(df_1))
    print("最大优先级为2的数据长度:%d"%len(df_2))
    print("最大优先级为3的数据长度:%d"%len(df_3))
    print("最大优先级为4的数据长度:%d"%len(df_4))

  #  df_0_percentage = get_percentage_fun(df_0)
  #  print("优先级0获赔概率：%.4f" % df_0_percentage)
    df_1_percentage = get_percentage_fun(df_1)
    print("优先级1获赔概率：%.4f" % df_1_percentage)
    print("###############")
    df_2_percentage = get_percentage_fun(df_2)
    print("优先级2获赔概率：%.4f" % df_2_percentage)
    print("###############")
    df_3_percentage = get_percentage_fun(df_3)
    print("优先级3获赔概率：%.4f" % df_3_percentage)
    print("###############")
    df_4_percentage = get_percentage_fun(df_4)
    print("优先级4获赔概率：%.4f" % df_4_percentage)
    print("###############")
