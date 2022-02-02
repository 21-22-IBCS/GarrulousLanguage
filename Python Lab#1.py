def coffeeShop():
    
    receipt=""
    name= input("Welcome! What is your name?\n")
    order= input("What would you like to order?\n")
    receipt = (name +" "+order+ " "+str(10))
    return receipt

    
def palindrome(s):
    pali= False
    for i in range (len(s)):
        if s[i] == s[len(s)-i-1:len(s)-i]:
            pali = True

    return pali

def main():
    print(coffeeShop())
    x=input("enter something")
    print(palindrome(x))


if __name__ == "__main__":
    main()
