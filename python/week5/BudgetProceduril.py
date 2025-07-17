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

def Spend(name, amount): 
    if name not in expenses:
        raise ValueError("Item not in budget") 
    expenses[name] += amount
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent

def printBudget():
    for name in budgets:
        Budgeted = budgets[name]
        spent = expenses[name]
        remainingBudgets = Budgeted - spent
        print (f'') (name:15):(name) < Budgeted, spent, remainingBudgets


print("Total funds:", funds)
AddBudget("books", 100) 
AddBudget("Rent",800) 
AddBudget("Car note", 200) 



Spend("Books", 50) 
Spend("rent", 800) 
Spend("car note", 200) 

printBudget()