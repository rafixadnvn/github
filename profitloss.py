actual_cost = float(input("Enter the actual cost of the meal: "))
selling_cost = float(input("Enter the selling cost of the meal: ") )
if(selling_cost> actual_cost):
    profit = selling_cost - actual_cost
    print("The seller has made a profit of ",profit)



else:
 print("no profit")
