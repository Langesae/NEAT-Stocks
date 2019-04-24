import pandas
import os
from sklearn.preprocessing import MinMaxScaler
from DataPreprocessing import preprocess
import numpy



def Begin_Processing_Prediction_CSV(ModelOutputCSVPath):
    modelOutputDF = pandas.read_csv(ModelOutputCSVPath)
    predictionsOutputDF = modelOutputDF.iloc[-1: ]
    finalPredictionsOutput = predictionsOutputDF['Prediction']

    #allows a workaround so I can later split it up into a true list
    predictions = []
    for o in finalPredictionsOutput:
        predictions.append(o)
    return predictions

def Processing_Prediction_To_Array(PredictionProcessedOnce):

    #Puts all the prediction values in a list
    #[-] pulls out the string and [2:-2] removes [[]]
    #then it splits on spaces and places it into a list
    predictionProssesedList = list(map(float, PredictionProcessedOnce[-1][2:-2].split()))

    predictionProssesedArray = [[val] for val in predictionProssesedList]
    return predictionProssesedArray

def Unscale_Prediction_To_DF(PreddictionArray, Stock):

    #pulls data similar to in the stockpredictionfile
    unscaledTrainData = preprocess(Stock, 'TrainData')
    unscaledTestData = preprocess(Stock, 'TestData')

    #Scale and then Unscale
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(unscaledTrainData)


    scaledTest = scaler.transform(unscaledTestData)

    scaledTest = numpy.delete(scaledTest, 0, 1)
    scaledTest = numpy.insert(scaledTest, [0], PreddictionArray, axis = 1)



    unscaledTest = scaler.inverse_transform(scaledTest)

    unscaledTestDF = pandas.DataFrame(unscaledTest)
    uscaledTestDFOutput = unscaledTestDF.iloc[:, 0:1]

    return uscaledTestDFOutput

def Read_Daily_Adj(stock):
    filename = os.getcwd() + '/TestData/DailyAdjusted/' + stock + '_DailyAdjusted.csv'
    unscaledDailyAdj = pandas.read_csv(filename)
    return unscaledDailyAdj

def Combine_DailyAdj_With_Prediction(DailyAdjDF, PredictionDf):
    dailyadjAndPredictionDF = pandas.concat([DailyAdjDF, PredictionDf], axis=1, join_axes=[DailyAdjDF.index])
    return dailyadjAndPredictionDF

def Save_Predictions_DF(PredictionsDF, ModelOutputCSVPath):
    filenameIndexStart = ModelOutputCSVPath.rfind('/')
    filenameIndexEnd = ModelOutputCSVPath.rfind('.')
    filename = os.getcwd() +'/Results/' + ModelOutputCSVPath[filenameIndexStart:filenameIndexEnd] + \
               '_FinalPredictions.csv'
    PredictionsDF.to_csv(filename)
    return

def Full_Processing(ModelOutputCSVPath, Stock):
    predictionProcessedOnce  = Begin_Processing_Prediction_CSV(ModelOutputCSVPath)
    predictionsArray = Processing_Prediction_To_Array(predictionProcessedOnce)
    unscaledPredictionsDF = Unscale_Prediction_To_DF(predictionsArray, Stock)
    dailyadj = Read_Daily_Adj(stock)
    combinedDF = Combine_DailyAdj_With_Prediction(dailyadj, unscaledPredictionsDF)
    Save_Predictions_DF(combinedDF, ModelOutputCSVPath)
    return



if __name__ == '__main__':
    stock = 'AXP'
    filename = os.getcwd() + '/Results/' + stock + '_Optimizer_Initializer_CostFunction.csv'

    #data_train = preprocess(stock, 'TrainData')
    data_test = preprocess(stock, 'TestData')
    print(data_test.shape)
    print(data_test)


    testpred = Begin_Processing_Prediction_CSV(filename)
    print(testpred)


    testpred2 = Processing_Prediction_To_Array(testpred)
    dailyadj = Read_Daily_Adj(stock)


    testpred3 = Unscale_Prediction_To_DF(testpred2, stock)
    print(testpred3)

    dailyadjAndPred = Combine_DailyAdj_With_Prediction(dailyadj, testpred3)
    print(dailyadjAndPred)

    Full_Processing(filename, stock)


