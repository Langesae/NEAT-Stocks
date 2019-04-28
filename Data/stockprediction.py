# Import
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from DataPreprocessing import preprocess
from SaveMseCsv import Main_Save, Create_File_Name
from PredictionDataProcessing import Full_Processing
from ScatterPlot import Plot_Scatter

stock = 'USB'

# Import data
#data = pd.read_csv('C:\\Users\\BabyHulk\\PycharmProjects\\stockprediction-master\\02_code\\data_stocks.csv')

# Drop date variable
#data = data.drop(['DATE'], 1)

# Dimensions of dataset
#n = data.shape[0]
#p = data.shape[1]

# Make data a np.array


# Training and test data

data_train = preprocess(stock, 'TrainData')
data_test = preprocess(stock, 'TestData')

# Scale data
scaler = MinMaxScaler(feature_range=(-1, 1))
scaler.fit(data_train)
data_train = scaler.transform(data_train)
data_test = scaler.transform(data_test)

# Build X and y
X_train = data_train[:, 1:]
y_train = data_train[:, 0]
X_test = data_test[:, 1:]
y_test = data_test[:, 0]

# Number of stocks in training data
n_stocks = X_train.shape[1]

# Neurons
n_neurons_1 = 1024
n_neurons_2 = 512
n_neurons_3 = 256
n_neurons_4 = 128

# Session
net = tf.InteractiveSession()

# Placeholder
X = tf.placeholder(dtype=tf.float32, shape=[None, n_stocks])
Y = tf.placeholder(dtype=tf.float32, shape=[None])

# Initializers
sigma = 1
weight_initializer = tf.variance_scaling_initializer(mode="fan_avg", distribution="uniform", scale=sigma)
bias_initializer = tf.zeros_initializer()

# Hidden weights
W_hidden_1 = tf.Variable(weight_initializer([n_stocks, n_neurons_1]))
bias_hidden_1 = tf.Variable(bias_initializer([n_neurons_1]))
W_hidden_2 = tf.Variable(weight_initializer([n_neurons_1, n_neurons_2]))
bias_hidden_2 = tf.Variable(bias_initializer([n_neurons_2]))
W_hidden_3 = tf.Variable(weight_initializer([n_neurons_2, n_neurons_3]))
bias_hidden_3 = tf.Variable(bias_initializer([n_neurons_3]))
W_hidden_4 = tf.Variable(weight_initializer([n_neurons_3, n_neurons_4]))
bias_hidden_4 = tf.Variable(bias_initializer([n_neurons_4]))

# Output weights
W_out = tf.Variable(weight_initializer([n_neurons_4, 1]))
bias_out = tf.Variable(bias_initializer([1]))

# Hidden layer
hidden_1 = tf.nn.relu(tf.add(tf.matmul(X, W_hidden_1), bias_hidden_1))
hidden_2 = tf.nn.relu(tf.add(tf.matmul(hidden_1, W_hidden_2), bias_hidden_2))
hidden_3 = tf.nn.relu(tf.add(tf.matmul(hidden_2, W_hidden_3), bias_hidden_3))
hidden_4 = tf.nn.relu(tf.add(tf.matmul(hidden_3, W_hidden_4), bias_hidden_4))

# Output layer (transpose!)
out = tf.transpose(tf.add(tf.matmul(hidden_4, W_out), bias_out))

# Cost function
mse = tf.reduce_mean(tf.squared_difference(out, Y))


# Optimizer
opt = tf.train.AdamOptimizer().minimize(mse)

# Init
net.run(tf.global_variables_initializer())

# Setup plot
plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(111)
line1, = ax1.plot(y_test)
line2, = ax1.plot(y_test * 0.5)
plt.show()

# Fit neural net
batch_size = 50
mse_train = []
mse_test = []

#addition of pred_list
pred_list = []

# Run
epochs = 10
for e in range(epochs):

    # Shuffle training data
    shuffle_indices = np.random.permutation(np.arange(len(y_train)))
    X_train = X_train[shuffle_indices]
    y_train = y_train[shuffle_indices]

    # Minibatch training
    for i in range(0, len(y_train) // batch_size):
        start = i * batch_size
        batch_x = X_train[start:start + batch_size]
        batch_y = y_train[start:start + batch_size]
        # Run optimizer with batch
        net.run(opt, feed_dict={X: batch_x, Y: batch_y})

        # MSE train and test
        mse_train.append(net.run(mse, feed_dict={X: X_train, Y: y_train}))
        mse_test.append(net.run(mse, feed_dict={X: X_test, Y: y_test}))

        # Prediction
        pred = net.run(out, feed_dict={X: X_test})
        line2.set_ydata(pred)
        pred_list.append(pred)

        # Graph
        plt.title('Epoch ' + str(e) + ', Batch ' + str(i))
        plt.pause(.01)

#Dot Plot
actual_close = []

pred = pred_list[-1]
for i in data_test:
    actual_close.append(i[0])

Plot_Scatter(stock, pred, actual_close)
FileName = Create_File_Name(stock, 'Optimizer', 'Initializer', 'CostFunction')
Main_Save(mse_train, mse_test, pred_list, FileName)
Full_Processing(FileName, stock)
