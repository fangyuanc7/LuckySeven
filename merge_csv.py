import pandas as pd
import glob

def merge_csv(path: str) -> (pd.DataFrame, str):
    allFiles = glob.glob(path + "/*.csv")
    list_ = []
    name = 'BA_job'

    for file_ in allFiles:
        df = pd.read_csv(file_, index_col=None, header=0)
        list_.append(df)
    merged = pd.concat(list_, axis = 0, ignore_index = True)
    return merged, name