import os
import csv
def read_csv(file_path='autoSign.csv'):
    if not os.path.exists(file_path):
        raise FileExistsError(file_path)
    with open(file_path,'r') as f:
        reader=csv.reader(f)
        result=list(reader)
    return result

# res=read_csv()
# print(res[0][1])