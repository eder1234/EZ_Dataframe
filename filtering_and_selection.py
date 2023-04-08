import pandas as pd

def filter_dataframe(dataframe, filters):
    filtered_dataframe = dataframe.copy()
    
    for filter_column, filter_value in filters.items():
        if filter_column in filtered_dataframe.columns:
            filtered_dataframe = filtered_dataframe[filtered_dataframe[filter_column] == filter_value]
    
    return filtered_dataframe
