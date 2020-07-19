import os
import csv

total_votes=0
khan_votes=0
correy_votes=0
li_votes=0
otooley_votes=0

csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    total_votes = khan_votes+correy_votes+li_votes+otooley_votes

    khan_wins = khan_votes/total_votes
    correy_wins = correy_votes/total_votes
    li_wins = li_votes/total_votes
    otooley_wins = otooley_votes/total_votes

    