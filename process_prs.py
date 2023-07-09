import datetime
import json
import csv
import sys
import getopt
from time import strftime, time


def extract_data(version, row):
    final_file = "./agent_bug_fixes.csv"
    input_file = "./bugfix.csv"
    output = []

    print("info", "Processing file: " + input_file)

    # Reading from the cloud_provider file and writing in the final CSV file

    output.insert(0, version)

    for i in range(0, 6):
        print ("column "+str(i)+" is: "+row[i])
        if i == 5:
            new_date= datetime.datetime.strptime(row[i],'%Y-%m-%d %H:%M:%S %z %Z')
            date2=new_date.strftime('%Y-%m-%d')
            print ("updated date is: " +date2)
            output.insert(i + 1, date2)
        else:
            output.insert(i + 1, row[i])



    if "team" in row[4]:
        new_row=row[4]
        new_row2=new_row.split(',')
        j=0
        print("len of new_row2: "+str(len(new_row2)))
        while j < len(new_row2):
            if "team" in new_row2[j]:
                print("the team is: "+new_row2[j])
                output.insert(8, new_row2[j])
                break
            else:
                j=j+1

    if "bugfix/functional" in row[4]:
        output.insert(9, "functional")
    elif "bugfix/security" in row[4]:
        output.insert(9, "security")
    elif "bugfix/performance" in row[4]:
        output.insert(9, "performance")
    else:
        output.insert(9, "undefined")

    if "changelog/no-changelog" in row[4]:
        output.insert(10, "NO")
    else:
        output.insert(10, "YES")

    if "qa/skip-qa" in row[4]:
        output.insert(11, "NO")
    else:
        output.insert(11, "YES")

    return output


def add_data(version):
    final_file = "./agent_bug_fixes.csv"
    input_file = "./bugfix.csv"

    with open(input_file, 'r') as file:
        csv_file = csv.reader(file, delimiter='|')
        for row in csv_file:
            print(row)
            added_row=extract_data(version,row)
            with open(final_file, 'a') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(added_row)



def main():
    print('info', 'Program starting...')
    print('info')

    print(type(sys.argv))
    print('The command line arguments are:')
    for i in sys.argv:
        print(i)
        version = i
    # collect cloud providers data...
    add_data(version)

    print('info', 'Program successfully finished.')

    return 0


# Execute main() function
if __name__ == '__main__':
    main()



