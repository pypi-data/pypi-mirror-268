


# from sklearn.preprocessing import LabelEncoder

# def label_encoding_selected(data, columns):
#     """
#     Perform label encoding on selected columns while retaining numeric values.

#     Parameters:
#     data (DataFrame): The input DataFrame.
#     columns (list): List of column names to label encode.

#     Returns:
#     DataFrame: The DataFrame with selected columns label encoded.
#     """
#     # Copy the original DataFrame
#     encoded_data = data.copy()
    
#     # Initialize LabelEncoder
#     label_encoder = LabelEncoder()
    
#     # Iterate through selected columns
#     for column in columns:
#         # Check if column exists and is categorical
#         if column in data.columns and data[column].dtype == 'object':
#             # Perform label encoding
#             encoded_data[column] = label_encoder.fit_transform(data[column])
    
#     return encoded_data


from sklearn.preprocessing import LabelEncoder

def label_encoding_selected(data, columns):
    """
    Perform label encoding on selected columns while retaining numeric values.

    Parameters:
    data (DataFrame): The input DataFrame.
    columns (list): List of column names to label encode.

    Returns:
    DataFrame: The DataFrame with selected columns label encoded.
    dict: A dictionary containing the label encoders used for each column.
    """
    # Copy the original DataFrame
    encoded_data = data.copy()
    
    # Initialize LabelEncoder
    label_encoders = {}
    
    # Iterate through selected columns
    for column in columns:
        # Check if column exists and is categorical
        if column in data.columns and data[column].dtype == 'object':
            # Perform label encoding
            label_encoder = LabelEncoder()
            encoded_data[column] = label_encoder.fit_transform(data[column])
            label_encoders[column] = label_encoder
    
    return encoded_data, label_encoders
