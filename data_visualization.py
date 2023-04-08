import matplotlib.pyplot as plt

def create_plot(dataframe, plot_type, x_column, y_column):
    if plot_type == 'scatter':
        dataframe.plot.scatter(x=x_column, y=y_column)
    elif plot_type == 'line':
        dataframe.plot.line(x=x_column, y=y_column)
    elif plot_type == 'bar':
        dataframe.plot.bar(x=x_column, y=y_column)
    elif plot_type == 'hist':
        dataframe[y_column].plot.hist()

    plt.show()
