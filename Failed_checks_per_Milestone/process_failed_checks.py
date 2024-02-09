import datetime
import json
import csv
import sys
import getopt
from time import strftime, time


def extract_data(version, row, var):
    final_file = "./agent_failed_checks.csv"
    input_file = "../failed_checks.csv"
    output = []

    print("info", "Processing file: " + input_file)

    # Reading from the cloud_provider file and writing in the final CSV file

    output.insert(0, version)

    for i in range(0, 6):
        print("column " + str(i) + " is: " + row[i])
        if i==1:
            key = version +':'+row[i]
            output.insert(1,key)
            output.insert(i + 2, row[i])
        elif i == 5:
            new_date = datetime.datetime.strptime(row[i], '%Y-%m-%d %H:%M:%S %z %Z')
            date2 = new_date.strftime('%Y-%m-%d')
            print("updated date is: " + date2)
            output.insert(i + 3, date2)
        else:
            output.insert(i + 3, row[i])

    if "team" in row[4]:
        new_row = row[4]
        new_row2 = new_row.split(',')
        j = 0
        print("len of new_row2: " + str(len(new_row2)))
        while j < len(new_row2):
            if "team" in new_row2[j]:
                print("the team is: " + new_row2[j])
                output.insert(8, new_row2[j])
                break
            else:
                j = j + 1
    else:
        output.insert(8, "undefined")

    return output


def add_data(version):
    final_file = "./agent_failed_checks.csv"
    input_file = "../failed_checks.csv"

    lines = len(list(final_file))
    var = lines + 1
    print('number of lines is:', var)

    with open(input_file, 'r') as file:
        csv_file = csv.reader(file, delimiter='|')
        for row in csv_file:
            print(row)
            added_row = extract_data(version, row, var)
            with open(final_file, 'a') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(added_row)



def main():
    print('info', 'Program starting...')
    print('info')

    version = sys.argv[1]

    print('info', 'current version is', str(version))
    add_data(version)

    print('info', 'Program successfully finished.')

    return 0


# Execute main() function
if __name__ == '__main__':
    main()
