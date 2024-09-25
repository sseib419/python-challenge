# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
vote_count = {"candidate": [],
              "votes": []}

# Winning Candidate and Winning Count Tracker
winning = ['', 0]

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in vote_count["candidate"]:
            vote_count["candidate"].append(candidate)

        # Add a vote to the candidate's count
            vote_count["votes"].append(1)
        else:
            index =vote_count["candidate"].index(candidate)
            vote_count["votes"][index] += 1
            
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"The total number of votes is {total_votes}")

    # Write the total vote count to the text file
    txt_file.write(f"Election Results\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"----------------------------\n")
    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in vote_count["candidate"]:

        # Get the vote count and calculate the percentage
        index = vote_count["candidate"].index(candidate)
        # Getting the number of votes for the candidate 
        numerator = vote_count["votes"][index]
        percentage = (numerator / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if numerator > winning[1]:
            winning[1] = numerator
            winning[0] = candidate

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {percentage:.3f}% ({numerator})\n")
        txt_file.write(f"{candidate}: {percentage:.3f}% ({numerator})\n")
    
    txt_file.write(f"----------------------------\n")    
    
    # Generate and print the winning candidate summary
    print(f"Winner: {winning[0]}")


    # Save the winning candidate summary to the text file
    txt_file.write(f"Winner: {winning[0]}\n")

    txt_file.write(f"----------------------------\n") 
