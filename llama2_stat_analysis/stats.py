import pandas as pd
from sklearn.preprocessing import LabelEncoder

#Loading the csv file
def load_csv(file_path):
    data = pd.read_csv(file_path)
    return data

# encoding the object type data into integers
#As this is required for building graphs 
def encode_data(data):
    label_encoders = {}
    for column in data.columns:
        if data[column].dtype == 'object':
            le = LabelEncoder()
            data[column] = le.fit_transform(data[column])
            label_encoders[column] = le
    return data, label_encoders

# calculating some basic statistics for both the encoded and original data
def basic_statistics(data, encoders):
    stats = {
        'mean': data.mean(),
        'median': data.median(),
        'mode': data.mode().iloc[0],
        'std_dev': data.std(),
        'correlation': data.corr()
    }

    decoded_stats = {}
    for col in stats:
        if col in encoders:
            decoded_stats[col] = {
                'encoded': stats[col].tolist(),
                'decoded': encoders[col].inverse_transform(stats[col].astype(int)).tolist()
            }
        else:
            decoded_stats[col] = stats[col]

    return decoded_stats


