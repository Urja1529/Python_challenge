import os
import csv
from datetime import datetime
dates=[]
total_profit=0
profit=[]
changes=[]
previous_profit=0
max_increase=0
max_decrease=0
#giving path file ,reading them and skipping Header line
path=os.path.join('..','Resources','budget_data.csv')
with open(path,'r') as data_file:
    reader=csv.reader(data_file,)
    header=next(reader)
    print(reader)
     #Counting Total Months and Total Profit and loss
    for row in reader:
        date_str=row[0]
        date_obj=datetime.strptime(date_str,"%b-%y")   
        dates.append(date_obj.strftime('%m-%y'))
        profit.append(int(row[1]))
        value=int(row[1])
        #Counting Changes in profit/loss
        change=value-previous_profit
        if previous_profit !=0:
            changes.append(change)
            #Calculating Greatest increase and decrease
            if change > max_increase:
                max_increase=change
                max_date=row[0]
            if change<max_decrease:
                max_decrease=change
                min_date=row[0]    
        previous_profit=value   
       
    avg_change=sum(changes)/len(changes)
num_months=len(set(dates))
total_profit=sum(profit)

#avg=total_profit1/len(profit1)
print("Financial Analysis")

print("------------------------------")

print(f"Total Number of Month in CSV File is: {num_months}")
print(f"Total : {total_profit}")
print(f"Average: {avg_change}")
print(f"Greatest Increase in price :{max_date} ${max_increase}")
print(f"Greatest Decrease in price :{min_date} ${max_decrease}")

with open('output.txt', 'w') as f:
    f.write(f"Total Number of Month in CSV File is: {num_months}")
    f.write(f"Total : {total_profit}")
    f.write(f"Average: {avg_change}")
    f.write(f"Greatest Increase in price :{max_date} ${max_increase}")
    f.write(f"Greatest Decrease in price :{min_date} ${max_decrease}")

