'''
Overview
A function that when provided a csv file (or excel file) and an array of cell locations (a3, b5, like in excel) returns the values in the cells. 

Inputs:
csv file
array of cell locations

Output:
json with key value pairs cell location - value
Test:
'''
import csv
import json
def csv(file, list_of_locations):
    with open(file,'r') as csv_file:
        print(type(csv_file))
        csv_reader = csv.reader(csv_file, dialect="excel")
        dic = {}
        for i in list_of_locations:
            y = ord(i[0]) - 97
            x = int(i[1]) - 1
            counter_x = 0
            counter_y = 0
            for line in csv_reader:
                if counter_x == x:
                    for word in line:
                        if counter_y == y:
                            dic[i] = word
                        counter_y += 1
                counter_x += 1
            csv_file.seek(0)
    r = json.dumps(dic)
    return r
