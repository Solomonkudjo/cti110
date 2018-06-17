#CTI-110
#P2T1 - Sales Prediction
#Kudjo Solomon
#June 15, 2018


#Get the protected total sales
total_sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of the total sales.
profit = total_sales * 0.23

#Display the profit.
print('The profit is $', format(profit, ',.2f'))
