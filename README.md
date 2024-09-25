To perform the financial analysis, first the budget_data csv is loaded. Then a variable for total months and the total net profit/loss are created and set equal to zero. An empty net change list is created, along with an array for holding the greatest profit increase, and an array for holding the greatest profit decrease. The code opens up the csv and skips the 1st row because it contains the headers, then goes to the 2nd row and adds 1 to the total months variable. The profit/loss value in the 2nd row is placed into the total net profit/loss variable, as well as into a variable to track the previous row's profit/loss. Then it skips to the 3rd row, and begins to loop through each row. For each row it adds 1 to the total months variable, and adds the profit/loss to the total net. The net change is calculated by taking the current row's profit/loss and subtracting the previous row's profit/loss, and that's added to the net change list. The code then checks if the net change is the greatest net change or the lowest net change calculated so far using a couple of if conditions, and if it is then the arrays for holding the greatest profit increase or decrease will be updated with the net change and the current row's month. The current row's profit/loss now becomes the previous row's profit/loss, and it goes on to the next row. After it loops through each row, it calculates the average net change. The results are printed to the terminal and written in a text file that is uploaded into the analysis folder. 
