import os
import csv

total_votes = 0
khan_votes = 0
li_votes = 0
correy_votes = 0
otooley_votes = 0

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

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

    khan_percentage = (khan_votes / total_votes)*100
    li_percentage = (li_votes / total_votes)*100
    correy_percentage = (correy_votes/total_votes)*100
    otooley_percentage = (otooley_votes / total_votes)*100

    winner = max(khan_votes, li_votes, correy_votes, otooley_votes)
    if winner == khan_votes:
        winner="Khan"
    elif winner == li_votes:
        winner="Li"
    elif winner == correy_votes:
        winner="Correy"
    else:
        winner="O'Tooley"

print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Khan: {khan_percentage}({khan_votes})")
print(f"Correy: {correy_percentage}({correy_votes})")
print(f"Li: {li_percentage}({li_votes})")
print(f"O'Tooley: {otooley_percentage}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner}")
print(f"---------------------------")

output_file=os.path.join('.','PyPoll', 'Resources', 'election_data_revised.txt')
with open(output_file, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes} \n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Khan: {khan_percentage}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percentage}({correy_votes})\n")
    txtfile.write(f"Li: {li_percentage}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percentage}({otooley_votes})\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"-------------------\n")

    
    
            
