def iterate(inputValue):
    print("You entered " + inputValue)

    try:
        float(inputValue)   #check if its a valid input 
        for i  in range(1,int(inputValue)+1):
            if ((i%3 == 0) or (i%5 == 0)):
                if i%3 == 0 and i%5 == 0:
                    print("multiple of 3 and 5") # print multiple of 3 and 5
                if i%3 == 0 and i%5 != 0:
                    print("multiple of 3")       # print multiple of 3
                if i%3 != 0 and i%5 == 0:
                    print("multiple of 5")       # print multiple of 5
            else:
                print(i)
    except ValueError:
        print("Not a valid number - Please enter a valid number > 0")
    
    
def main():

    inputValue = input("Enter the value... ");
    iterate(inputValue)
 
main()
