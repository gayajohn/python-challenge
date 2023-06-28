Here are the references used in the main.py script for the PyPoll project:

1) https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python

   To learn how to find unique values in a list

   line reference: unique_candidates = set(candidates)

-------------------------------------------------------------------------------------------

3) https://stackoverflow.com/questions/14032521/python-data-structure-sort-list-alphabetically

4) https://learnpython.com/blog/sort-alphabetically-in-python/ 
   
   To learn how to sort lists alphabetically

   line reference: unique_candidates = sorted(unique_candidates)

-------------------------------------------------------------------------------------------

5) https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value-in-python

6) https://www.geeksforgeeks.org/how-to-convert-fraction-to-percent-in-python/

   To learn how to format variables as percentages with 3 decimal places

   line reference: vote_percent[y] = "{:.3%}".format(vote_num[y]/total_votes) #formatted to be displayed as a percentage with 3 decimal places

-------------------------------------------------------------------------------------------

7) https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list/

   To learn how to find the largest number in a list

   line reference: print(f"Winner: {unique_candidates[vote_num.index(max(vote_num))]}")

-------------------------------------------------------------------------------------------

The following code was created with the help of the next 3 references:

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

8) https://stackoverflow.com/questions/8024248/telling-python-to-save-a-txt-file-to-a-certain-directory-on-windows-and-mac

To learn how to save the output text into a specific directory

9) https://www.geeksforgeeks.org/saving-text-json-and-csv-to-a-file-in-python/

To learn how to export the output in .txt format

10) https://stackoverflow.com/questions/13794873/how-to-export-all-print-to-a-txt-file-in-python

To learn how to export the output in .txt format

-------------------------------------------------------------------------------------------

Note that I also used Jupyter IDE to test and debug my code.
