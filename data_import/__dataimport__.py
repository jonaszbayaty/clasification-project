import csv


array = []  

for row in csv.reader(open('data_import/mnist_test.csv')):
    array.append(row)                                                                   
def find_number(number):
    for row in array:
        if int(row[0]) == number:
            return row

    return None


print(find_number(9))
