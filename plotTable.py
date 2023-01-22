import matplotlib.pyplot as plt
import seaborn as sns

def plotGraph(xlsxdataframe, xlabel_vale, ylabel_vale,plot_title,color):
    order_date = xlsxdataframe[xlabel_vale].tolist()
    order_units = xlsxdataframe[ylabel_vale].tolist()

    plt.title(plot_title)
    plt.bar(order_date, order_units, label = plot_title,color=color)
    plt.xlabel(xlabel_vale)
    plt.ylabel(ylabel_vale+' Purches')
    plt.xticks(order_date)
    plt.yticks([100,150,250,500,750,1000,1500,1700,2200])
    plt.show(block=False)
    #plt.pause(1)
    plt.savefig(plot_title+'.png')
    plt.close()
