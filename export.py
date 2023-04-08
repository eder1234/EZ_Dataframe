import pandas as pd
import pickle

def save_dataframe_to_pickle(dataframe, file_path):
    try:
        with open(file_path, 'wb') as f:
            pickle.dump(dataframe, f)
        return True
    except Exception as e:
        print(f"Error saving dataframe to pickle file: {e}")
        return False
