#importing dependencies
import csv
import os
#Save file path to variable
csv_path = os.path.join("PyPoll","Resources","election_data.csv")

#setting main variables as described in the module prompt; total votes cast, list of candidates who received votes, percentage of votes each candidate received, total votes each candidate received, and the winner of the popular vote.
total = 0
candnames = []
candvotes = []
candprop = []
winner = ""
#checking candidate variable while iterating; 'i' denotes value count of given candidate, 'j' denotes index of candidates after summing together
diffcheck = ""
i = 0
j = -1
#Read with csv
with open(csv_path, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    for row in csvreader:
        total+=1
        if row[2] == diffcheck:
            candvotes[i] += 1
        else:
            if row[2] in candnames:
                i = candnames.index(row[2])
                candvotes[i] += 1
                diffcheck = row[2]
            else:
                j += 1
                candnames.append(row[2])
                i = candnames.index(row[2])
                candvotes.append(0)
                candvotes[i] += 1
                candprop.append(0)
                diffcheck = row[2]

#calculating proportions
i = 0
for k in candvotes:
    candprop[i] = round(k/total,5)*100
    i += 1

#printing results as succinctly as possible
print(f'Election Results \n ---------------------- \n')
print(f'Total Votes: {total} \n ---------------------- ')

i = 0
for k in candnames:
    print(f'{k}: {candprop[i]}% ({candvotes[i]})')
    i += 1

print(f'-----------------------\n')

#finding winner
i = max(candvotes)
winner = candvotes.index(i)
winner = candnames[winner]

print(f'Winner: {winner}\n ----------------------')

#writing results to a text file, titled: 'results.txt'
with open('results.txt', 'w') as f:
    f.write('Election Results\n-------------------------\nTotal Votes: '+str(total)+'\n')
    i = 0
    for k in candnames:
        f.write(k + ": " + str(candprop[i]) + "% (" + str(candvotes[i])+ ")\n")
        i += 1
    
    f.write('-------------------------------\nWinner: ' + winner + '\n-------------------------------')
