# math functions
# Author: Saksham Shrestha
# description:

def fibonnaci_series(n):    #function to calculate fibonnaci series
    if n<=0:
        print("Please enter a positive integer")
    elif n==1:
        print(0)
    else:
        a,b = 0,1
        for i in range(n):
            print(a)
            a,b = b,a+b
def factorial(n):       # function to calculate factorial
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)        #recursive function


def main():
    num=int(input("Enter the number:"))     #input of the number
    fibonnaci_series(num)
    f= factorial(num)
    print("The factorial of",num,"is",f)

if __name__ == "__main__":      # run only when called directly
    main()