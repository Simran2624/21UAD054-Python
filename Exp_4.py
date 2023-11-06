import csv

#Method to read each row of file and return as string
def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    strings = [','.join(row) for row in data]
    return strings

#Define file path and call the method
file_path = "C:/Users/admin/OneDrive/Desktop/user/UG/Data Wrangling Lab/samplecsv.csv"
strings = read_csv_file(file_path)
print(strings)
