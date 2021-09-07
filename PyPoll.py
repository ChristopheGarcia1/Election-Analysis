# Goals through the module
# 1. The total Number of Votes cast
# 2. A complete list of candidates who recieved votes.
# 3. The percentage of votes each candidate won
# 4. The total number of each candidate won 
# 5. The wimmer of the election based on the popular vote.

#importing csv and os module 
import csv
import os

#assign file to variable to load the path 
file_to_load = os.path.join("Resources", "election_results.csv")
#create a filename variable to a direct or indirect path to the file.
file_to_save =  os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter 
total_votes = 0 
# initialize a candidates list
candidate_options =[]
# declare the empty dictionary
Candidate_votes ={}

#open election results and read the file 
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)
    
    #read and print header rows
    headers =next(file_reader)

    #print each row of the csv file.
    for row in file_reader:

        total_votes += 1

        #print the candidate name from each row.
        candidate_name = row[2]

        # if candidate does not match candidate already in the list
        if candidate_name not in candidate_options:
        #add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #start each candidate at 0 votes
            Candidate_votes[candidate_name] = 0
        
        #count each vote per row
        Candidate_votes[candidate_name] += 1
    for candidate_name in Candidate_votes:
        votes = Candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        vote_percentage = round(vote_percentage, 1)
        print(f"{candidate_name}: recieved {vote_percentage}% of the vote")
    
    
# print the dictionary
#print(Candidate_votes)

#print candidate list
#print(candidate_options) 

#print total_votes
#print(total_votes)

# Print the file object
#print(election_data)
# Close the file.
election_data.close()
# ---------------------------------------------------------------
# using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
#write some data into the file.
    txt_file.write("Counties in the election\n")
    txt_file.write("---------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson\n")

#close the text file
txt_file.close()