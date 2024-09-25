To perform the financial analysis, first the budget_data csv is loaded. Then a variable for total months and the total net profit/loss are created and set equal to zero. An empty net change list is created, along with an array for holding the greatest profit increase, and an array for holding the greatest profit decrease. The code opens up the csv and skips the 1st row because it contains the headers, then goes to the 2nd row and adds 1 to the total months variable. The profit/loss value in the 2nd row is placed into the total net profit/loss variable, as well as into a variable to track the previous row's profit/loss. Then it skips to the 3rd row, and begins to loop through each row. For each row it adds 1 to the total months variable, and adds the profit/loss to the total net. The net change is calculated by taking the current row's profit/loss and subtracting the previous row's profit/loss, and that's added to the net change list. The code then checks if the net change is the greatest net change or the lowest net change calculated so far using a couple of if conditions, and if it is then the arrays for holding the greatest profit increase or decrease will be updated with the net change and the current row's month. The current row's profit/loss now becomes the previous row's profit/loss, and it goes on to the next row. After it loops through each row, it calculates the average net change. The results are printed to the terminal and written in a text file that is uploaded into the analysis folder. 


To get the results of an election, the election_data csv is loaded. A variable for total votes is created and set equal to 0. A dictionary is then created that has the voter data, where it holds an empty candidate list and an empty votes list. Another list is created to hold the winning candidate and their number of votes. The csv is opened, and the 1st row is skipped because it contains the headers. A for loop is used to go through each row, where the total votes variable is increased by 1. The candidate's name is collected from the 3rd column and placed into a variable. Using an if condition, the code check's if the candidate is already contained in the candidate list. If it's not then it's added to the list and a 1 is added to the votes list. If the candidate is already contained within the candidate's list, then it will find it's index and use that to determine the index in the votes list that needs to increase by 1. After it loops through all the rows, it prints the total number of votes to the terminal and writes the election results to a file which is uploaded to the analysis folder. Using a for loop that goes through the candidate list, the number of the candidate's vote is pulled from the votes list and stored into a variable. The percentage of votes for that candidate is calculated. An if condition is used to check if the number of candidate's votes is the greatest collected so far. If it is, then the winning list is updated with the candidate's name & their # of votes. The candidate, their voting percentage, & the number of votes is printed to the terminal and written to the text file. The winning candidate is also printed and written to the file.
