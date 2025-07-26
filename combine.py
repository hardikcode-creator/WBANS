import os
import pandas as pd
def combine(path, files_per_patient,index,no_of_patients):
    start=index*no_of_patients
    data=[]
    for i in range(1,files_per_patient+1):
        data.append(f"{os.path.join(path,f"{start+i}")}.csv")
    df=pd.concat(map(pd.read_csv,data),ignore_index=True)
    return df


if __name__=="__main__":
    no_of_patients=16
    dataset_path="dataFrames"
    path="dataset"
    os.makedirs(dataset_path,exist_ok=True)
    for i in range(no_of_patients-1):
        df=combine(path,15,i,no_of_patients)
        df.to_csv(f"{os.path.join(dataset_path,f"{i+1}")}.csv")

