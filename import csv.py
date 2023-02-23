import os

new_dir = '/Users/zsunny/Python'
os.chdir(new_dir)


import os

print("Current working directory:", os.getcwd())
print("Files in the current directory:", os.listdir())


import csv

try:
    with open('Test CSV.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("The file 'Test CSV.csv' does not exist in the current directory.")
except Exception as e:
    print(f"An error occurred: {e}")
