import datetime
import json
import csv
import sys
import getopt
from time import strftime, time


def extract_data(version, code_freeze, prod_deploy, row, var):
    final_file = "agent_bug_fixes.csv"
    input_file = "./bugfix.csv"
    output = []

    print("info", "Processing file: " + input_file)

    # Reading from the cloud_provider file and writing in the final CSV file

    output.insert(0, version)
    freeze=datetime.datetime.strptime(code_freeze,'%Y-%m-%d')
    freeze2=freeze.strftime('%Y-%m-%d')
    output.insert(1, freeze2)
    deploy=datetime.datetime.strptime(prod_deploy,'%Y-%m-%d')
    deploy2=deploy.strftime('%Y-%m-%d')
    output.insert(2, deploy2)

    for i in range(0, 6):
        print("column " + str(i) + " is: " + row[i])
        if i==1:
            key = version +':'+row[i]
            output.insert(3,key)
            output.insert(i + 4, row[i])
        elif i == 5:
            new_date = datetime.datetime.strptime(row[i], '%Y-%m-%d %H:%M:%S %z %Z')
            date2 = new_date.strftime('%Y-%m-%d')
            print("updated date is: " + date2)
            output.insert(i + 4, date2)
        else:
            output.insert(i + 4, row[i])

    if "team" in row[4]:
        new_row = row[4]
        new_row2 = new_row.split(',')
        j = 0
        print("len of new_row2: " + str(len(new_row2)))
        while j < len(new_row2):
            if "team" in new_row2[j]:
                print("the team is: " + new_row2[j])
                output.insert(12, new_row2[j])
                break
            else:
                j = j + 1

    if "bugfix/functional" in row[4]:
        output.insert(13, "functional")
    elif "bugfix/security" in row[4]:
        output.insert(13, "security")
    elif "bugfix/performance" in row[4]:
        output.insert(13, "performance")
    else:
        output.insert(13, "undefined")

    if "changelog/no-changelog" in row[4]:
        output.insert(14, "NO")
    else:
        output.insert(14, "YES")

    items = "qa/skip-qa" , "qa/done" , "qa/no-code-change"
    if not any(i in row[4] for i in items) :
        output.insert(15, "NO")
        output.insert (16,"NA")
    else:
        output.insert(15, "YES")
        if "qa/done" in row[4]:
            output.insert (16, "QAed")
        elif "qa/no-code-change" in row[4]:
            output.insert (16, "no code change")
        else:
            output.insert(16, "undefined")


    return output


def add_data(version, code_freeze, prod_deploy):
    final_file = "agent_bug_fixes.csv"
    input_file = "./bugfix.csv"

    lines = len(list(final_file))
    var = lines + 1
    print('number of lines is:', var)

    with open(input_file, 'r') as file:
        csv_file = csv.reader(file, delimiter='|')
        for row in csv_file:
            print(row)
            added_row = extract_data(version, code_freeze, prod_deploy, row, var)
            with open(final_file, 'a') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(added_row)



def main():
    print('info', 'Program starting...')
    print('info')

    version = sys.argv[1]
    code_freeze = sys.argv[2]
    prod_deploy = sys.argv[3]

    print('info', 'current version is', str(version), "code freeze is", str(code_freeze), "and prod deploy is ",
          str(prod_deploy))
    add_data(version, code_freeze, prod_deploy)

    print('info', 'Program successfully finished.')

    return 0


# Execute main() function
if __name__ == '__main__':
    main()
