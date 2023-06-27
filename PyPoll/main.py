#importing libraries needed for this script
import os
import csv

# path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

# reading the CSV file
with open(election_csv, 'r') as csvfile:
    
    #splitting the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #variable to store total no. of votes
    total_votes = 0

    #list to store candidates
    candidates=[]

    #storing headers in header variable
    header = next(csvreader)

    #variable to store column index for Candidates
    candcol = header.index("Candidate")
    
    #looping through the rows in csv reader
    for row in csvreader:

        #counter variable
        total_votes +=1 

        #appending candidate names to list of candidates
        candidates.append(row[candcol])

    #creating a list containing only unique candidate names
    unique_candidates = set(candidates)

    #sorting candidates alphabetically within the list
    unique_candidates = sorted(unique_candidates)

    #creating lists to store vote numbers and percentage of votes received
    vote_num = []
    vote_percent = []

    #looping through no. of unique candidates and appending values to vote_num[] and vote_percent[] lists
    for cand in unique_candidates:
        vote_num.append(0)
        vote_percent.append(0)

    #variable to represent index in the following loop
    x = 0

    #nested loop that looks for each unique candidate among the list of all the candidates, tallies the votes and assigns it to the appropriate list index
    for cand in unique_candidates:
        for votes in candidates:
            if cand == votes:
                vote_num[x] += 1
        
        x=x+1
    
    #loop that goes through all unique candidates and assigns percentage values in the vote_percent[] list
    for y in range(len(unique_candidates)):
        vote_percent[y] = "{:.3%}".format(vote_num[y]/total_votes) #formatted to be displayed as a percentage with 3 decimal places


#creating a dictionary that puts together candidates, the votes they recieved and what percentage of votes they received
dict = {"Candidates": unique_candidates, "Votes": vote_num, "Percentage" : vote_percent  }

#print output

print("Election Results")
print("")
print("-------------------------")
print("")
print(f"Total Votes: {total_votes}")
print("")
print("-------------------------")
print("")

#looping through all the lists in the dictionary
for y in range(len(unique_candidates)):
    print(f"{dict['Candidates'][y]}: {dict['Percentage'][y]} ({dict['Votes'][y]})")
    print("")

print("-------------------------")
print("")

#finding the candidate with the most votes
print(f"Winner: {unique_candidates[vote_num.index(max(vote_num))]}") 
print("")        
print("-------------------------")

#creating a .txt file to store the output

#setting the path for where the .txt file is saved
filepath = os.path.join("analysis", "Output.txt")
f= open(filepath, "w")

#printing the same output into the .txt file

print("Election Results", file = f)
print("", file = f)
print("-------------------------", file = f)
print("", file = f)
print(f"Total Votes: {total_votes}", file = f)
print("", file = f)
print("-------------------------", file = f)
print("", file = f) 

#looping through all the lists in the dictionary
for y in range(len(unique_candidates)):
    print(f"{dict['Candidates'][y]}: {dict['Percentage'][y]} ({dict['Votes'][y]})", file = f)
    print("", file = f)

print("-------------------------", file = f)
print("", file = f)

#finding the candidate with the most votes
print(f"Winner: {unique_candidates[vote_num.index(max(vote_num))]}", file = f)  
print("", file = f)       
print("-------------------------", file = f)

#closing the .txt file
f.close()





