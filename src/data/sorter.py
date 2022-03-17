# Must install pandas to use
# pip3 install pandas
import pandas as ps

filenames = ['Operating Systems Basic.csv', 'Operating Systems Cloze.csv', 'Programming Languages Basic.csv', 'Programming Languages Cloze.csv']

for file in filenames:
    csvData = ps.read_csv(file)
    print("Old CSV Data:")
    print(csvData)
    csvData.sort_values(["tags"], ascending=True, inplace=True)
    print("New CSV Data:")
    print(csvData)

    print("Do you wish to write to " + file + "? (y/N)")
    if input() == 'y':
        csvData.to_csv(file, index=False)
        print("Wrote to " + file)
    else:
        print("Did not write to " + file)


