
import pandas as pd
import trainDataRead

def tongji_data(data):
    data_new = data.copy()


def forecastResult(testFilename, trainFileName):
    data = pd.read_csv(testFilename, encoding='gb18030')

    trainDataRead.read2(trainFileName)
    # print("test name: ", csvread2.name_arrary)

    # 列名
    # print(data.columns)
    # 索引
    # print(data.index)

    print(trainDataRead.name_arrary)
    print(data.columns)
    existsColumns = []
    nameSet = set(trainDataRead.name_arrary)
    priorityMin = 999
    for columnName in data.columns:
        if columnName in nameSet:
            existsColumns.append(columnName)
            print("columnsName ", columnName, " value :", trainDataRead.key_dict[columnName])
            if priorityMin > trainDataRead.key_dict[columnName]:
                priorityMin = trainDataRead.key_dict[columnName]
    print("min value ", priorityMin)
    print("level percent ",trainDataRead.levelPercentage)
    print("result percent ", trainDataRead.levelPercentage[priorityMin-1])
    return trainDataRead.levelPercentage[priorityMin-1]
