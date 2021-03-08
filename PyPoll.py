# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter(Add the total vote counter before the with open()statement)
total_votes = 0

#Print the candidate options and candidate votes
candidate_options = []
# Declare empty dictionary
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.(Increment the total_votes by 1 after the for loop)
        total_votes += 1
    #Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list 
            candidate_options.append(candidate_name)
        # 2. Begin tracking that candidate's vote count. When this is added were setting each candidate vote count to zero
            candidate_votes[candidate_name] = 0
            #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Print the candidate list.
print(candidate_votes)
