total_sales = int(input())

cost_of_one_hovercraft = 2000000
cost_of_monthly_insurance = 1000000
total_no_of_hovercraft = 10
selling_price_of_one_hovercraft = 3000000

monthly_cost = (cost_of_one_hovercraft * total_no_of_hovercraft) + cost_of_monthly_insurance

current_monthly_sales = (selling_price_of_one_hovercraft *
 total_sales )

if monthly_cost == current_monthly_sales :
    print('Broke Even')
elif monthly_cost > current_monthly_sales :
    print('Loss')
else:
    print('Profit')