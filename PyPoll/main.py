#PyPoll
#Load packages
import os
import csv

#Declare variables
total_votes = 0
candidate1 = "Charles Casper Stockham"
candidate1_count = 0
candidate2 = "Diana DeGette"
candidate2_count = 0
candidate3 = "Raymon Anthony Doane"
candidate3_count = 0
candidate_list = []

#Import csv data
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        #print(row)

        #Count total votes
        total_votes = total_votes + 1

        #Candidate votes
        if row[2] == candidate1:
            candidate1_count = candidate1_count + 1
        elif row[2] == candidate2:
            candidate2_count = candidate2_count + 1
        else: candidate3_count = candidate3_count + 1

        #Candidate winner
        if candidate1_count > candidate2_count and candidate1_count > candidate3_count:
            winner = candidate1
        elif candidate2_count > candidate1_count and candidate2_count > candidate3_count:
            winner = candidate2
        else: winner = candidate3

#Result variables
candidate1_pct = round((candidate1_count / total_votes) * 100, 3)
candidate2_pct = round((candidate2_count / total_votes) * 100, 3)
candidate3_pct = round((candidate3_count / total_votes) * 100, 3)

#Print results  
results1 = f"Election Results"
results2 = f"-------------------------"
results3 = f"Total Votes: {total_votes}"
results4 = f"-------------------------"
results5 = f"{candidate1}: {candidate1_pct}% ({candidate1_count})"
results6 = f"{candidate2}: {candidate2_pct}% ({candidate2_count})"
results7 = f"{candidate3}: {candidate3_pct}% ({candidate3_count})"
results8 = f"-------------------------"
results9 = f"Winner: {winner}"
results10 = f"-------------------------"
resultsfinal = [results1, results2, results3, results4, results5, results6, results7, results8, results9, results10]

for item in resultsfinal:
    print(item)
    print('\n')

#Export to txt file
with open('analysis/results.txt', 'w') as f:
    for item in resultsfinal:
        f.write(item)
        f.write('\n')
