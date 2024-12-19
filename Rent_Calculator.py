Rent = int(input('Enter your hostle/flat rent : '))#taking input of hostle
Food = int(input('Enter the amount of food ordered : '))#taking input of food
Electricty_spend = int(input('Enter the total of electricity spend : '))#taking input of bill
Electrict_Charge_per_unit = int(input('Enter the charge per unit : '))#taking input of per unit
Persons = int(input('Enter the number of persons living in room/flat : '))#taking input of persons

Total_Electricity_bill = Electricty_spend * Electrict_Charge_per_unit

calculation = (Rent + Food + Total_Electricity_bill) // Persons
print('Total charge per person to pay = ',calculation)

