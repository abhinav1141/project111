import plotly.figure_factory as ff 
import statistics
import random
import csv
import pandas as pd 
import plotly.graph_objects as go 

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].to_list()
mean = statistics.mean(data)
std_dev = statistics.stdev(data)

print("Mean of the sampling data {}".format(mean))
print("Standard Deviation of Sample Distribution {}".format(std_dev))

def random_set_of_mean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

meanlist = []
for i in range(0,100):
    set_of_mean = random_set_of_mean(30)
    meanlist.append(set_of_mean)

std_dev = statistics.stdev(meanlist)
mean = statistics.mean(meanlist)

first_std_dev_start, first_std_dev_end = mean - std_dev, mean + std_dev
second_std_dev_start, second_std_dev_end = mean - 2*(std_dev), mean + 2*(std_dev)
third_std_dev_start, third_std_dev_end = mean - 3*(std_dev), mean + 3*(std_dev)

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].to_list()
meanOfSample = statistics.mean(data)
print("Mean of Sample 1 :-", meanOfSample)

z_score = (meanOfSample - mean)/std_dev
print("the z score is =", z_score)

fig = ff.create_distplot([meanlist],["reading_time"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17],mode = "lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[meanOfSample, meanOfSample], y=[0,0.17],mode="lines",name="Mean of Sample"))
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0,0.17],mode="lines",name="Standard Deviation 1 Start"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0,0.17],mode="lines",name="Standard Deviation 1 End"))
fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0,0.17],mode="lines",name="Standard Deviation 2 Start"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0,0.17],mode="lines",name="Standard Deviation 2 End"))
fig.add_trace(go.Scatter(x=[third_std_dev_start, third_std_dev_start], y=[0,0.17],mode="lines",name="Standard Deviation 3 Start"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[0,0.17],mode="lines",name="Standard Deviation 3 End"))
fig.show()