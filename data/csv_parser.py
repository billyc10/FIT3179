import csv
import requests

URL = "https://epsg.io/trans"

with open('fatal_crashes_vic.csv', 'r') as source_file, open('converted_times.csv', 'w', newline='') as write_file:
    csv_source = csv.reader(source_file)
    csv_write = csv.writer(write_file)
    
    header = []
    header = next(csv_source)

    csv_write.writerow(['LINE', 'TIME'])

    year_index = header.index('ACCIDENT_D')
    time_index = header.index('ACC_TIME')

    line = 2

    for row in csv_source:    
        # Extract year and time
        time_string = row[time_index]

        time_string = time_string[0:2] + ':00'

        csv_write.writerow([line, time_string])

        line += 1
