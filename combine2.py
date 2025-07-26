
import os
import pandas as pd
def combine(path):
    all_files = [os.path.join(path, file) for file in os.listdir(path) if file.endswith('.csv')]
    df = pd.concat((pd.read_csv(f) for f in all_files),ignore_index=True)
    return df



if __name__=='__main__':
     path='dataFrames/'
     df=combine(path)
     df.to_csv(f"dataFrames/combined.csv")
