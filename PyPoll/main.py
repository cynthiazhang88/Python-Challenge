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

    