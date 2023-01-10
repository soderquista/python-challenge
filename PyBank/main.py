import os
import csv
#initializing path
csv_path = os.path.join("PyBank","Resources","budget_data.csv")
#setting variables to track (name denoted in parenthesis): months, net profit over period (net), sum of change between months (old, diffsum) and then the average change between months(avg), highest monthly increase in profits (top), highest monthly decrease in profits (bottom)
months=0
net = 0
old = 0
diffsum = 0
avg = 0
top = 0
topmonth = ""
bottom = 0
bottommonth = ""
with open(csv_path, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    row1 = next(csvreader)
    row2 = next(csvreader)
    old = int(row2[1])
    net += old
    months+=1
    top = old
    topmonth = row2[0]
    for row in csvreader:
        #the summed difference of each month to the next is the new monthly profit minus the old, and add that to the total for ALL monthly differences (diffsum!)
        diffsum = diffsum + int(row[1]) - old
        old = int(row[1])
        net += int(row[1])
        #recordbreaker months: top, topmonth, bottom, and bottommonth
        if top < int(row[1]):
            top = int(row[1])
            topmonth = row[0]
        if bottom > int(row[1]):
            bottom = int(row[1])
            bottommonth = row[0]
        #tracking the number of months in the file.
        months+=1
#calculating average difference given the sum of the differences of all months.
avg = diffsum/(months-1)
#printing results
print(f'Financial Analysis \n----------------------- \nTotal Months: {months} \nTotal: ${net} \nAverage Change: ${avg} \n Greatest Increase in Profits: {topmonth} (${top}) \nGreatest Decrease in Profits: {bottommonth} (${bottom})')
#writing results to a text file, titled: 'results.txt'
with open('results.txt', 'w') as f:
    f.write('Financial Analysis\n')
    f.write('---------------------\n')
    f.write('Total Months: ' + str(months) +'\n')
    f.write('Total: $' + str(net) +'\n')
    f.write('Average Change: $' + str(round(avg, 2)) +'\n')
    f.write('Greatest Increase in Profits: ' + str(topmonth) + ' ($' + str(top) + ')'+'\n')
    f.write('Greatest Decrease in Profits: ' + str(bottommonth) + ' ($' + str(bottom) + ')'+'\n')
