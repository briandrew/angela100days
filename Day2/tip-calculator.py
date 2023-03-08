# Create a tip calculator per the following examples.assert

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

print("Tip Calculator")
bill = float(input("Please enter the bill total before tip: $"))
tip = int(input("What percentage tip do you want to give - 10, 15, or 20: "))
people = int(input("How many people are splitting the bill?: "))
total_bill = bill + (bill * (tip / 100))
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
total_bill = "{:.2f}".format(total_bill)

print(f"The total with tip is ${total_bill}.")
print(f"The total per person is ${final_amount}")






