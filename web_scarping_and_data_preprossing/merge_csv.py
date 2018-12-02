import pandas as pd
import glob
import argparse

def merge_csv(path: str) -> (pd.DataFrame, str):
    allFiles = glob.glob(path + "/*.csv")
    list_ = []
    name = allFiles[0].split('-')[0]
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=None, header=0)
        list_.append(df)
    merged = pd.concat(list_, axis = 0, ignore_index = True)
    return merged, name

if __name__ == "__main__":

	''' eg-:python merge_csv.py "/Users/chengyilun/Desktop" '''

	argparser = argparse.ArgumentParser()
	argparser.add_argument('path', help='path of the csv files')
	args = argparser.parse_args()
	path = args.path
	print("Merging csv files...")
	output, name = merge_csv(path)
	output.to_csv(name+'.csv', index=False)
	print('Done!')