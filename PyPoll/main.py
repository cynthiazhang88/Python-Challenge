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
        total_votes =1
        
        if row[2]=="Khan":
            khan_votes = 1
        elif row[2]=="Correy":
            correy_votes = 1
        elif row[2]=="Li":
            li_votes = 1
        else:
            otooley_votes = 1
            
            khan_percentage = khan_votes/total_votes
            correy_percentage = correy_votes/total_votes
            li_percentage = li_votes/total_votes
            otooley_percentage = otooley_votes/total_votes

            election_winner = max(khan_percentage, correy_percentage, li_percentage, otooley_percentage)
            election_winner

            if election_winner == "Khan":
                winner= "Khan"
            elif election_winner == "Correy":
                winner = "Correy"
            elif election_winner == "Li":
                winner = "Li"
            else:
                winner = "O'Tooley"
            print(f"Election Results")
            print(f"................")
            print(f"Total Votes {total_votes}")
            print(f"................")
            print(f"Khan: {khan_percentage}({khan_votes})")
            print(f"Correy: {correy_percentage}({correy_votes})")
            print(f"Li: {li_percentage}({li_votes})")
            print("O'Tooley: {otooley_percentage}({otooley_votes})")
            
