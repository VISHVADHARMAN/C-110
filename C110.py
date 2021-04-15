import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random
import pandas as pd 
import csv

df=pd.read_csv(r"D:/C-110/newdata.csv")
data=df["average"].tolist()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("Population Mean:- ",population_mean)
print("Std Deviation:- ",std_deviation)

#Function to plot mean as the graph
def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["average"],show_hist=False)
    fig.show()

#Function to get the mean of the given data samples
def random_set_of_mean(counter):
    dataset=[] 
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

#Function to get mean of 100 data points 1000 times and plot the graph
def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)

    show_fig(mean_list)

setup()

