# Import Modules

import os
import csv

# Variables Declaration
total_votes = 0
khan_votes = 0 
correy_votes = 0
li_votes = 0
otooley_votes = 0

# csv Path
csvpath = os.path.join('Resources', 'election_data.csv')

# Read csv File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        
        # Total Number Of Votes Cast
        total_votes += 1
        
        # Total Number Of Votes Each Candidate Won
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
    # Calculate Percentage Of Votes Each Candidate Won
    khan_percent = round((khan_votes / total_votes) * 100)
    correy_percent = round((correy_votes / total_votes) * 100)
    li_percent = round((li_votes / total_votes) * 100)
    otooley_percent = round((otooley_votes / total_votes) * 100)
    
    # Calculate Winner Of The Election Based On Popular Vote
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print the analysis to the terminal
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"khan: {khan_percent}({khan_votes})")
print(f"Correy: {correy_percent}({correy_votes})")
print(f"Li: {li_percent}({li_votes})")
print(f"O'Tooley: {otooley_percent}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")


# Export the analysis to text file
PyPoll = open("analysis/output.txt","w+")
PyPoll.write(f"Election Results\n")  
PyPoll.write(f"---------------------------\n")
PyPoll.write(f"Total Votes: {total_votes}\n") 
PyPoll.write(f"---------------------------\n")
PyPoll.write(f"khan: {khan_percent}({khan_votes})\n")
PyPoll.write(f"Correy: {correy_percent}({correy_votes})\n")
PyPoll.write(f"Li: {li_percent}({li_votes})\n")
PyPoll.write(f"O'Tooley: {otooley_percent}({otooley_votes})\n")
PyPoll.write(f"---------------------------\n")
PyPoll.write(f"Winner: {winner_name}\n")
PyPoll.write(f"---------------------------\n")

    