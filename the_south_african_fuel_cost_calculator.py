##FUEL COST CALCULATOR
# Let's assume they want to travel 100km
kilometres = float(input("Enter number of kilometres you want to travel: "))
petrol_price = float(input("Enter current travel cost: R")) 
litres_needed = kilometres / 10
travel_cost =  litres_needed * petrol_price
print(f"Your total travel cost is: {travel_cost}")  
print(f"Your final total travel cost is: {round(travel_cost, 2)} rounded") 


