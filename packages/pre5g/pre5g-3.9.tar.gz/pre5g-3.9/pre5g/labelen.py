


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
    dict: A dictionary containing legends for each column.
    """
    # Copy the original DataFrame
    encoded_data = data.copy()
    
    # Initialize LabelEncoder
    label_encoders = {}
    
    # Initialize legend dictionary
    legend = {}
    
    # Iterate through selected columns
    for column in columns:
        # Check if column exists and is categorical
        if column in data.columns and data[column].dtype == 'object':
            # Initialize LabelEncoder for the column
            encoder = LabelEncoder()
            # Perform label encoding
            encoded_data[column] = encoder.fit_transform(data[column])
            # Store the label encoder for future reference
            label_encoders[column] = encoder
            # Store the legend for the column
            legend[column] = {label: category for label, category in enumerate(encoder.classes_)}
    
    return encoded_data, legend

