import matplotlib.pyplot as plt

def plotGraph(xlsxdataframe, xlabel_vale, ylabel_vale):
    order_date = xlsxdataframe[xlabel_vale].tolist()
    order_units = xlsxdataframe[ylabel_vale].tolist()

    plt.title('Units by year')
    plt.bar(order_date, order_units, label = 'YearWise Unit purches',color="violet")
    plt.xlabel('Year Basis')
    plt.ylabel('Units Purches')
    plt.xticks(order_date)
    plt.yticks([100,150,250,500,750,1000,1300])
    plt.show()
    plt.close('all')