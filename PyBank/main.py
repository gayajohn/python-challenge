#importing libraries needed for this script
import os
import csv

# path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

#defining a function for finding the average in a list
#note that because there is 1 less value for list of changes, relative to date and profit/loss lists, we are dividing by (length of list - 1)
def average(listofnumbers=[]):
    sum =0
    for numbers in listofnumbers:
        sum = sum + numbers
    return sum/(len(listofnumbers)-1)


# reading the CSV file
with open(budget_csv, 'r') as csvfile:
    
    #variable to store no. of months
    total_months = 0

    #variable to sum total profit/loss
    total_pl = 0

    #splitting the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #storing headers in header variable
    header = next(csvreader)

    #variables to store column index for Date and Profit/Losses
    datecol = header.index("Date")
    plcol = header.index("Profit/Losses")

    #list to store all the current profit/loss
    current=[]

    #list to store date
    dates=[]

    #looping through the rows in csv reader
    for row in csvreader:

        #counter variable
        total_months +=1 

        #summing up total profit/loss
        total_pl += int(row[plcol])
        
        #appending profit/loss to current list
        current.append(int(row[plcol]))

        #appending dates to dates list
        dates.append(row[datecol])

#running through the csv for the second time to create a list called after to store the (row+1) value of profit/loss
with open(budget_csv, 'r') as csvfile:
    
    #splitting the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #storing and skipping through header row
    header = next(csvreader)
    
    #skipping the first row 
    next(csvreader)
    
    #list to store the next profit/loss value such that change = after - current
    after=[]

    #looping through rows in csv starting from the 2nd data row
    for row in csvreader:

        #appending profit/loss to after list, starting from the second date
        after.append(int(row[plcol]))

#list to store the difference between after and current 
change=[]

#setting the first change value to 0 because there is no change on the first date
change.append(0)

#running a loop from 1 to end of the after[] list, as indeces for the change[] list
#note that the range ends in the length of after[] + 1 
for x in range(1, len(after)+1):

    #appending after[]-current[] to change[]
    change.append(after[x-1]-current[x-1])

#creating variables to store highest and lowest change values
highest = 0
lowest = 0

#looping through the change[] list to find highest and lowest values
for val in change:
    if val>highest:
        highest = val
    if val<lowest:
        lowest = val

#print output
print("Financial Analysis")
print("")
print("----------------------------")
print("")
print(f"Total Months: {total_months}")
print("")
print(f"Total: ${total_pl}")
print("")
print(f"Average Change: ${round(average(change),2)}") #using round function to round down to 2 decimal places
print("")
print(f"Greatest Increase in Profits: {dates[change.index(highest)]} (${highest})")
print("")
print(f"Greatest Decrease in Profits: {dates[change.index(lowest)]} (${lowest})")

    
#creating a .txt file to store the output

#setting the path for where the .txt file is saved
filepath = os.path.join("analysis", "Output.txt")
f= open(filepath, "w")

#printing the same output into the .txt file
print("Financial Analysis", file = f)
print("", file = f)
print("----------------------------", file = f)
print("", file = f)
print(f"Total Months: {total_months}", file = f)
print("", file = f)
print(f"Total: ${total_pl}", file = f)
print("", file = f)
print(f"Average Change: ${round(average(change),2)}", file = f) 
print("", file = f)
print(f"Greatest Increase in Profits: {dates[change.index(highest)]} (${highest})", file = f)
print("", file = f)
print(f"Greatest Decrease in Profits: {dates[change.index(lowest)]} (${lowest})", file = f)

#closing the .txt file
f.close()

