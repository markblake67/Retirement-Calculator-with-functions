name = input("Enter name: ")  #User input value that saves user's name to a variable titled 'user'
age = input("Enter Age: ")  #User input value that saves input user's age to the variable age.

def retirementCalc(x):  #creation of the calculator that calculates how long until user can retire. 
    yearsToRetire = 66 - int(age)    #Variable that converts the age input to an integer and calculates the difference between that and the retirement age. 
    yearsToRetire = str(yearsToRetire)  #converts yearsToRetire variable string into a float
    print("You have: " + yearsToRetire + " years until you can retire.")  #prints a statement saying you have a certain amount of years until you retire. 
    
print("Hello, " + name + ".")   #Prints a string that incorporates an introduction and the users name. 
retirementCalc(age)  #calls the retirementCalc function to use. 