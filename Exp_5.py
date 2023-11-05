import csv

#method to read data as dictionary
def read_csv2dict(file_path):
    with open(file_path,'r') as file:
        csv_reader=csv.DictReader(file)
        data=[row for row in csv_reader]
    return data

#method to display disctionary format data
def display(data):
    for row in data:
        for key,value in row.items():
            print(f"{key}: {value}")
        print()

#give path of csv file to varible and call methods
file_path="C:/Users/admin/OneDrive/Desktop/user/UG/Data Wrangling Lab/departments2.csv"
data=read_csv2dict(file_path)

display(data)