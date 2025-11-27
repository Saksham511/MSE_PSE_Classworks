# math functions
# Author: Saksham Shrestha
# description:
import math     # import math libraries

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

def main():
    num=int(input("Enter the number:"))     #input of the number
    fibonnaci_series(num)
    print("The factorial of",num,"is",math.factorial(num))

if __name__ == "__main__":      # run only when called directly
    main()