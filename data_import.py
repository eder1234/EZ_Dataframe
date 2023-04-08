import pandas as pd

def import_csv_to_dataframe(file_path):
    try:
        dataframe = pd.read_csv(file_path)
        return dataframe
    except Exception as e:
        print(f"Error importing CSV file: {e}")
        return None
