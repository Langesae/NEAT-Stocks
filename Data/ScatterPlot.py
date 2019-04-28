import pandas
import os
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def Plot_Scatter(stock, prediction, actual):
    FileName = os.getcwd()
    FileName += '/Results/' + stock + '-Prediction_vs_Actual'
    plt.ion()
    fig = plt.figure()
    plt.title(stock + " -- Model Predictions vs Observed")
    ax1 = fig.add_subplot(111)
    ax1.scatter(prediction, actual)
    plt.savefig(FileName)
    plt.pause(1)
