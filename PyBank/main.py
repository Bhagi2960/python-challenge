
import csv
import os
import statistics

#file path to input data
data = os.path.join( "PyBank", "Resources", "budget_data.csv")

with open(data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip header in data 
    csv_header = next(csvreader)

    net_profit_loss= 0
    months = 0
    month_changes = []
    profitloss_changes = []
    
    avg_change = 0
    current_month_profitloss = 0

    maxchange = 0
    minchange = 0
    highest_month = ''
    lowest_month = ''

    
    #read through each row of data after header
    for row in csvreader:

        months += 1
        current_month_profitloss = int(row[1])
        net_profit_loss += current_month_profitloss


        if months == 1:
        # make the previous months profit equal to current month for the first row    
            prev_month_profit = current_month_profitloss
        else:
            change_in_profit_loss = current_month_profitloss - prev_month_profit
            #add each month to the months list
            month_changes.append(row[0])
            #add change in progit loss for each period
            profitloss_changes.append(change_in_profit_loss)
            #set the previous months profit loss to current month's profit loss
            prev_month_profit = current_month_profitloss
    
    # Calculate the sum and average of the profit loss over the entire period
sum_profit_loss = sum(profitloss_changes)
number_months = months - 1
avg_change = round((sum_profit_loss)/number_months,2)



        

#Calculating greatest increase in profits
maxchange = max(profitloss_changes)
minchange = min(profitloss_changes)
maxmonth = profitloss_changes.index(maxchange)
minmonth = profitloss_changes.index(minchange)

#Get the month and year value from months list

highest_month = month_changes[maxmonth]
lowest_month = month_changes[minmonth]



output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: $ {net_profit_loss}
Average Change: ${round(avg_change,2)}
Greatest Increase in Profits: {highest_month} (${maxchange})
Greatest Decrease in Profits: {lowest_month} (${minchange})
'''

# print(months)
print(output)



#Export a text file with the results:
#specify the path to write to:

output_path = os.path.join("PyBank", "Analysis", "pybank_output.txt")

#open the file using write mode
with open(output_path, 'w') as outfile:


    outfile.write(f"Financial Analysis\n")
    outfile.write(f"----------------------------\n")
    outfile.write(f"Total Months:  {months}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${round(avg_change,2)}\n")
    outfile.write(f"Greatest Increase in Profits:  {highest_month} (${maxchange})\n")
    outfile.write(f"Greatest Decrease in Losses:  {lowest_month} (${minchange})\n")


