import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button, RadioButtons 
from matplotlib.axis import Axis

plt.style.use('fivethirtyeight')

x1_values = []
y1_values = []
x2_values = []
y2_values = []
x3_values = []
y3_values = []
x4_values = []
y4_values = []
x5_values = []
y5_values = []
x6_values = []
y6_values = []

index = count()

def animate(i):
    data = pd.read_csv('View_log.csv')
    x1_values = data['Time']
    x2_values = data['Time']
    x3_values = data['Time']
    x4_values = data['Time']
    x5_values = data['Time']
    x6_values = data['Time']
    y1_values = data['Asianet']
    y2_values = data['News24']
    y3_values = data['Manorama']
    y4_values = data['MediaOne']
    y5_values = data['AlJazeera']
    y6_values = data['NDTV']
    plt.cla()
    plt.plot(x1_values, y1_values, label = "Asianet")
    plt.plot(x2_values, y2_values, label = "News24")
    plt.plot(x3_values, y3_values, label = "Manorama")
    plt.plot(x4_values, y4_values, label = "MediaOne")
    plt.plot(x1_values, y5_values, label = "AlJazeera")
    plt.plot(x1_values, y6_values, label = "NDTV")
    plt.xlabel('Time')
    plt.ylabel('Views')
    plt.title('Live Views')
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.tight_layout()
    
ani = FuncAnimation(plt.gcf(), animate, 5000)
plt.tight_layout()
plt.show()

