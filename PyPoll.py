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
# Winning Candidate and Winning Count Tracker
winning_candidate = "" #Declare a variable that holds an empty string value for winning candidate
winning_count = 0 #Declare a variable for the "winning count" equal to zero
winning_percentage = 0 #Declare a variable for the "winning_percentage" equal to zero
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
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

#Print the final vote to the terminal
    election_results = ( #variable has 4 strings
        f"\nElection_Results\n" #1st string, newline character, will be the 2nd line, then newline is created
        f"-------------------------\n" # 25 dashes will be printed then newline will be created 
        f"Total Votes: {total_votes:,}\n" #printed with the votes formatted with a thousands separator, and then a new line created
        f"-------------------------\n") # 25 dashes will be printed then newline will be created
    print(election_results, end="") #print election results with the parameter end="" equal to an empty string
    # Save the final vote count to the text file
    txt_file.write(election_results) #write election results to text file 
    # Determine the percentage of votes for each candidate by looping through the counts. We need to divide the candidates vote count by the total vote count, and then multiply by 100. Votes are the values of each candidate_name in the candidates_votes dictionary.Convert votes and total_votes to floating point decimal numbers because the votes in the dictionary and the total_values are integers.
    # 1. Iterate through the candidate list with for loops which will retrieve the candidates name
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate. Use a for loop variable to retrieve from the candidate_votes = {}
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

    #  To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
#  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate

        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            # And, set the winning_candidate equal to the candidate's name(which is the variable).
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    #Print the winning candidates'results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
# Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)