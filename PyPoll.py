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

#open election results and read the file 
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)
    
    #read and print header rows
    headers =next(file_reader)
    print(headers)

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