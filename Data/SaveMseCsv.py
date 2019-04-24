import pandas
import os
import random


def Main_Save(MSETrainList, MSETestList, Pred_list, FileName):
    MSEDict = Combine_Lists_To_Dict(MSETrainList, MSETestList, Pred_list)
    Save_Mse_Csv(MSEDict, FileName)

def Save_Mse_Csv(MSEDict, FileName):
    MSEDf = MSE_Dict_To_Df(MSEDict)
    MSE_Df_To_CSV(MSEDf, FileName)
    return

def MSE_Dict_To_Df(MSEDict):
    df = pandas.DataFrame(MSEDict)
    return df

def Create_File_Name(Stock, Optimizer, Initializer, CostFuncion):
    FileName = os.getcwd()
    FileName += '/Results/' + Stock + '_' + Optimizer + '_' + Initializer + '_' + CostFuncion + '.csv'
    return FileName

def MSE_Df_To_CSV(MSEDf, FileName):
    MSEDf.to_csv(FileName)
    return

def Combine_Lists_To_Dict(List1, List2, List3):
    OutputDict = {'MSE_Train' : List1}
    OutputDict['MSE_Test'] = List2
    OutputDict['Prediction'] = List3
    return OutputDict




if __name__ == '__main__':
    List1 = [-1, 0, 3]
    List2 = [1, 2, 4]
    List3 = [0, 3, 5]
    ListDict = Combine_Lists_To_Dict(List1, List2, List3)
    print(ListDict)
    Main(List1, List2, List3, 'a', 'b', 'c', 'd')
