import pandas as pd
def fix_errors(data):
    def fillna_with_mean_median_mode(data):
        for col in data.columns:
            if data[col].dtype == 'float':
                data[col] = data[col].fillna(data[col].mean())
            elif data[col].dtype == 'object':
                data[col] = data[col].fillna(data[col].mode()[0])
        

    # Fill missing values with the mean, median, and mode
    data1 = data
    fillna_with_mean_median_mode(data1)

    # Save the DataFrame to a CSV file
    return data1
