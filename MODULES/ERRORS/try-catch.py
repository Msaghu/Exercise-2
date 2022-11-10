#Handling errors by passing in a catch block
num1 = input("Enter the first number: ")
num2 = input("Enter another number: ")

if num1 != "60":
    raise Exception ("hey num1 needs to be a number")

#def add(num1, num2):
#    try:
#        newNum = int(num1) + int(num2)
#        try:
#           return newNum + "HEllo there"
#        except:
#            return "Nested Failure"
#    except ValueError:
#        return"Hey you need to enter a number"
#    except:
#        return " Hey you "

 
#print(add(num1, num2))
