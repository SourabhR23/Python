#!/usr/bin/env python
# coding: utf-8

# ## `Calculator`

# In[ ]:


class Calculator:
    
    def add(self, num1, num2):
        '''
        Function defined for addition between two numbers 
        '''
        return (num1 + num2)

    def subtract(self, num1, num2):
        '''
        Function defined for subtraction between two numbers 
        '''
        return (num1 - num2)
    
    def multiply(self, num1, num2):
        '''
        Function defined for multiplition between two numbers 
        '''
        return (num1 * num2)
    
    def divide(self, num1, num2):
        '''
        Function defined for division between two numbers 
        '''
        return (num1 / num2)

    
if __name__ == "__main__":

    Calc = Calculator()

    while True:

        try:
            print('''
                    Select Operation
                    1. Addition
                    2. Subtraction
                    3. Multiplication
                    4. Division
                    5. Close Calculator
                    ''')
            
            choice =int(input("\nEnter choice(1/2/3/4/5): "))
            
            if choice == "":
                print("Empty input is invalid. Please select number.")
                
            if choice == 5:
                print("*Thank You for using Calculator*")
                break
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print("\nAddition is: ", Calc.add(num1, num2))
                
            elif choice == 2:
                print("\nSubtraction is: ", Calc.subtract(num1, num2))
                  
            elif choice == 3:
                print("\nMultiplication is: ", Calc.multiply(num1, num2))
                  
            elif choice == 4:
                print("\nDivision is: ", Calc.divide(num1, num2))
            
            else:
                print("\nInvalid input. \nPlease try again!")
        
        except ValueError:
            print("\nString as input is not valid. Please select number.")
            continue
        except ZeroDivisionError:
            print("\nCan not divide by Zero!")
            continue


# In[ ]:





# In[ ]:




