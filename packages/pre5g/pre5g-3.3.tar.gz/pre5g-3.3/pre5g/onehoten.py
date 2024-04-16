import pandas as pd

# def one_hot_encoding_selected(data, columns):
#     """
#     Perform one-hot encoding on selected columns while retaining numeric values.

#     Parameters:
#     data (DataFrame): The input DataFrame.
#     columns (list): List of column names to one-hot encode.

#     Returns:
#     list: List of lists with one-hot encoded columns, including column names.
#     """
#     # Copy the original DataFrame
#     encoded_data = data.copy()
    
#     # Initialize a list to store the column names in the output
#     column_names = []
    
#     # Iterate through selected columns
#     for column in columns:
#         # Check if column exists and is categorical
#         if column in data.columns and data[column].dtype == 'object':
#             # Perform one-hot encoding
#             encoded_column = pd.get_dummies(data[column], prefix=column)
#             # Store the names of the one-hot encoded columns
#             column_names.extend(encoded_column.columns)
#             # Drop original column and concatenate one-hot encoded columns
#             encoded_data = pd.concat([encoded_data.drop(column, axis=1), encoded_column], axis=1)
    
#     # Convert DataFrame to list of lists
#     encoded_list = encoded_data.values.tolist()
    
#     return [column_names] + encoded_list
# # update the package , not updated 

def one_hot_encoding_selected(data, columns):
    """
    Perform one-hot encoding on selected columns while retaining numeric values.

    Parameters:
    data (DataFrame): The input DataFrame.
    columns (list): List of column names to one-hot encode.

    Returns:
    list: List of lists with one-hot encoded columns, including column names.
    """
    # Copy the original DataFrame
    encoded_data = data.copy()
    
    # Initialize a list to store the column names in the output
    column_names = []
    
    # Iterate through selected columns
    for column in columns:
        # Check if column exists and is categorical
        if column in data.columns and data[column].dtype == 'object':
            # Perform one-hot encoding
            encoded_column = pd.get_dummies(data[column], prefix=column)
            # Store the names of the one-hot encoded columns
            column_names.extend(encoded_column.columns)
            # Drop original column and concatenate one-hot encoded columns
            encoded_data = pd.concat([encoded_data.drop(column, axis=1), encoded_column], axis=1)
    
    # Convert DataFrame to list of lists
    encoded_list = encoded_data.values.tolist()
    
    # Insert column names as the first element in the list
    encoded_list.insert(0, column_names)
    
    return encoded_list