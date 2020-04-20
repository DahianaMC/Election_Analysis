# The data we need to retrieve from election results file:
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The total number of votes each candidate won.
# 4. A complete list of the counties that recieved votes.
# 5. The total number of votes each county contributed.
# 6. The percentage of votes each county contributed.
# 7. The winner county of the election based on votes.
# 8. The percentage of votes each candidate won.
# 9. The winner of the election based on popular vote.


# Import modules to read csv files and create path to save and read a files.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options list.
candidate_options = []

# Declare the empty dictionary for candidate votes.
candidate_votes = {}

# County Options List.
county_options = []

# Declare the empty dictionary for county votes.
county_votes = {}

# Winning County and Winning County Count Tracker
winning_county = ""
winningCounty_count = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.  Telling read the file starting from the second row (after the header)
    headers = next(file_reader)
    

    # Read each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Determine the total votes for each county
        county_name = row[1]
        # If the county does not match any existing candidate...
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # Begin tracking that county's vote count
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1

       
# Save the results to our text file (terminal).
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
            f"\nCounty Votes:\n")
           
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # Determine the percentage of votes for each county by looping through the vote counts by county.
        # Iterate through the county votes.
        for county in county_votes:
            # Retrieve vote count of a county
            votes = county_votes[county]
            # Calculate the percentage of votes in each county.
            voteCounty_percentage = float(votes) / float(total_votes) * 100
            # Print out each county's name, vote county count, and percentage of votes per county to the terminal.
            county_results = (f"{county}: {voteCounty_percentage:.1f}% ({votes:,})\n")
 
            # Print the final vote count and percentage per county to the terminal.
            print(county_results,end="")
            # Save the county results to the text file.
            txt_file.write(county_results)


            # Determine winning county using votes and print the county name
            if (votes > winningCounty_count): 
                # if true then set winningCounty_count = votes.
                winningCounty_count = votes
                # Set the winning_county equal to the county's name.
                winning_county = county

            #  Print out the winning county to the terminal.
            winning_county_summary = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n")
        print(winning_county_summary)
        # Save the winning county's results to the text file.
        txt_file.write(winning_county_summary)

        # Determine the percentage of votes for each candidate by looping through the vote counts by candidate.
        # Iterate through the candidate votes.
        for candidate in candidate_votes:
            # Retrieve vote count of a candidate
            votes = candidate_votes[candidate]
            # Calculate the percentage of votes per candidate.
            vote_percentage = float(votes) / float(total_votes) * 100
            # Print out each candidate's name, vote count, and percentage of votes to the terminal.
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate's voter count and percentage to the terminal.
            print(candidate_results, end="")
            # Save the candidate results to the text file.
            txt_file.write(candidate_results)

            
            # Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # if true then set winning_count = votes and winning_percent = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate
                
            #  Print out the winning candidate, vote count and percentage to terminal.
            winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)