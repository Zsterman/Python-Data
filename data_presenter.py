# question 2 + 3 - Open the CupcakeInvoices.csv.
# Loop through all the data and print each row.

open_file = open('CupcakeInvoices.csv')
for line in open_file:
    print(line)
open_file.close()

# question 4 - Loop through all the data and print the type of cupcakes purchased.

cupcakes = open('CupcakeInvoices.csv','r')

total_Chocolate = 0
total_Vanilla = 0
total_Strawberry = 0

for line in cupcakes:
    line = line.rstrip('\n').split(',')
    for value in line:
        if value == 'Chocolate':
            total_Chocolate +=1
        elif value == 'Vanilla':
            total_Vanilla +=1
        elif value == "Strawberry": 
            total_Strawberry +=1          


print(total_Chocolate,total_Vanilla,total_Strawberry)

# question 5 - Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).

cupcakes = open('CupcakeInvoices.csv','r')
prices = []

for line in cupcakes:
    line = line.rstrip('\n').split(',')
    totalPrice = int(line[3])*float(line[4])
    prices.append(totalPrice)

    

    print(prices)
    

# question 6 - Loop through all the data, and print out the total for all invoices combined.

total= sum(prices)
print('Sum of list elements is', total)





# question 7 - Close your open file.

open_file.close()



# Challenge: Do some research and see if you can limit your floats to never exceed to characters after the decimal point.





# Going Further - Explore the graphing tools covered in today’s lecture. See if you can implement one of them to display the total income of chocolate cupcakes vs vanilla cupcakes vs strawberry cupcakes.
