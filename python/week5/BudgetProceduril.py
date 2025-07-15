funds = 2500 



budgets = {} 



expenses = {} 



def AddBudget(name, amount): 
    global funds 
    if name is budgets:
        raise ValueError("Budget For item already Exists")
    if amount > funds: 
        raise ValueError("No can do, You are to broke")
    budgets[name] = amount 
    funds -= amount 
    expenses[name] = 0 
    return funds 

print(funds)
AddBudget("rent", 120) 
AddBudget("rent", 500)
print(budgets)
print(expenses) 
print(funds)