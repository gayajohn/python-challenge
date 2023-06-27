
Here are the references used in the main.py script for the PyBank project:

1) https://www.geeksforgeeks.org/appending-to-list-in-python-dictionary/

   To learn more about appending lists

3) https://www.tutorialspoint.com/python/python_variable_types.htm

   To learn about the various variable types available in Python

---------------------------------------------------------------------------------------------
The following code was created with the help of the next 3 references:

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


3) https://stackoverflow.com/questions/8024248/telling-python-to-save-a-txt-file-to-a-certain-directory-on-windows-and-mac

   To learn how to save the output text into a specific directory

5) https://www.geeksforgeeks.org/saving-text-json-and-csv-to-a-file-in-python/

   To learn how to export the output in .txt format

7) https://stackoverflow.com/questions/13794873/how-to-export-all-print-to-a-txt-file-in-python

   To learn how to export the output in .txt format
---------------------------------------------------------------------------------------------


