def productOfThree(x, y, z):
    return x*y*z

def favHolidays():
    return "Halloween", "Leap-Day"


#the variables inside the parantheses are called 'parameters'
#we can have multiple parameters, separated by a comma 
def sum3(x):
    return x+3

 
def main():

    print("Hello class! :)")

    x = 4
    sum3(x)

    
    #both ways of accepting output can be printed
    print(sum3(2))
    result = sum3(8)
    print(result)

    print(favHolidays())

    print(productOfThree(5.5,3,-9))

    #you always take input as a STRING
    favNum=input("Write your favorite number\n")
    print("My favorite number is "+favNum)
    
if __name__ == "__main__":
    main()
