
from openai import AzureOpenAI
import pandas as pd
import numpy as np

def error_handling(data):

    print("Inside the error handling")
    

    # Define ANSI escape codes for different colors
    class Color:
        HEADER = '\033[95m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'

    # data = pd.read_csv("output_test9.csv")

    completeness_scores = (1 - data.isnull().mean()) * 100
    cell_quality_scores = (100 - completeness_scores) / 100
    column_quality_scores = []

    for col in data.columns:
        weighted_sum = (cell_quality_scores * (1 - data[col].isnull().astype(int))).sum()
        sum_completeness = (1 - data[col].isnull().astype(int)).sum()
        col_quality_score = weighted_sum / sum_completeness
        column_quality_scores.append(col_quality_score)

    column_quality_scores = pd.Series(column_quality_scores, index=data.columns)
    row_confidences = 1 - data.isnull().sum(axis=1) / data.shape[1]
    row_quality_scores = row_confidences
    dataset_quality_score = np.mean(cell_quality_scores)
    print("*"*100)
    print(Color.HEADER + "Completeness Scores:" + Color.ENDC)
    print(completeness_scores)
    print(Color.BLUE + "\nCell Quality Scores:" + Color.ENDC)
    print(cell_quality_scores)
    print(Color.GREEN + "\nColumn Quality Scores:" + Color.ENDC)
    print(column_quality_scores)
    print(Color.WARNING + "\nDataset error Score:" + Color.ENDC, dataset_quality_score)

    print("-"*100)

    def find_missing_value_positions(data):

        missing_value_positions = data.isnull()
        rows_with_missing_values = missing_value_positions.any(axis=0)
        cols_with_missing_values = missing_value_positions.any(axis=1)  # Fix: Changed axis=0 to axis=1
        rows = rows_with_missing_values.index[rows_with_missing_values].tolist()
        cols = cols_with_missing_values.index[cols_with_missing_values].tolist()

        return rows, cols

    missing_rows, missing_cols = find_missing_value_positions(data)
    print("After the find_missing_value_positions")

    def coerce_to_correct_dtype(data):

        for col in data.columns:
            col_data = data[col]
            numeric_count = pd.to_numeric(col_data, errors='coerce').notna().sum()
            total_count = col_data.count()
            if numeric_count > total_count / 2:
                try:
                    data[col] = pd.to_numeric(col_data, errors='coerce')
                except ValueError:
                    pass
    
    def data_quality_check(data):
        coerce_to_correct_dtype(data)
        print("after coerce_to_correct_dtype")
        missing_values = data.isnull().sum()
        nan_values = data.isna().sum()
        none_values = data.isin([None]).sum()
        zero_missing_values = ((data == 0) | (data == 0.0) | (data.isnull()) | (data == None) | (data == np.nan)).sum()
        total_missing_values = missing_values + zero_missing_values - nan_values - none_values
        data.replace('', np.nan, inplace=True)
        empty_columns = data.columns[data.isnull().all()]
        empty_rows = data[data.isnull().all(axis=1)]
        empty_rows = pd.concat([empty_rows, data[data.eq('').all(axis=1)]])
        empty_rows.drop_duplicates(inplace=True)
        duplicate_rows = data.duplicated().sum()
        data_types = data.dtypes
        missing_value_positions = [(row + 2, col + 1) for row, col in zip(*np.where(data.isnull()))]

        results = {}
        results["Missing_Values"] = total_missing_values
        results["Empty_Columns"] = empty_columns
        results["Empty_Rows"] = empty_rows
        results["Duplicate_Rows"] = duplicate_rows
        results["Data_Types"] = data_types
        results["Missing_Value_Positions"] = missing_value_positions

        columns_with_missing_values = {}
        for column, count in total_missing_values.items():
            if count > 0:
                columns_with_missing_values[column] = count
        results["Columns_with_missing_values"] = columns_with_missing_values
        return results
 
    results = data_quality_check(data)
    print("After data_quality_check")

    missing_values = results["Missing_Values"]
    empty_columns = results["Empty_Columns"]
    empty_rows = results["Empty_Rows"]
    duplicate_rows = results["Duplicate_Rows"]
    data_types = results["Data_Types"]
    missing_value_positions = results["Missing_Value_Positions"]
    columns_with_missing_values = results["Columns_with_missing_values"]

    print(Color.HEADER + "Data Quality Check Results:" + Color.ENDC)
    for check, result in results.items():
        print(Color.GREEN + f"{check}:" + Color.ENDC)
        print(result)
        print("\n")


   

    
    print("dataset_quality_score",dataset_quality_score)
    return dataset_quality_score