class Calculator:
    def Add(self, x, y):
        return x + y
    
    def Subtract(self, x, y):
        return x - y
    
    def Multiply(self, x, y):
        return x + y
    
    def Divide(self, x, y):
        return x / y 
    

calculator = Calculator() 

sum = calculator.Add(25, 78) 
diffrence = calculator.Subtract(10,5)
product = calculator.Multiply(5,8) 
dividend = calculator. Divide(12, 4) 

print(sum) 
print(diffrence) 
print(product)
print(dividend) 


    