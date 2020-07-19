import os
import csv

total_votes = 0
khan_votes = 0
li_votes = 0
correy_votes = 0
otooley_votes = 0

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    for row in csvreader:
       total_votes += 1

       if(row[2]) == "Khan":
           khan_votes += 1
       elif(row[2]) == "Li":
            li_votes += 1
       elif(row[2]) == "Correy":
            correy_votes += 1
       else:
            otooley_votes += 1
    khan_percentage = khan_votes / total_votes
    li_percentage = li_votes / total_votes
    correy_percentage = correy_votes/total_votes
    otooley_percentage = otooley_votes / total_votes

    winner = max(khan_percentage, li_percentage, correy_percentage, otooley_percentage)

    
    
            
