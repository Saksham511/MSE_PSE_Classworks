class TempConverter:
    def __init__(self,t):       # initialize the data for object
        self.t=t

    def validate(self):         # validate whether the data has correct prefix followed by temperature in number
        t=self.t
        if (t.startswith("C") or t.startswith("F")) and len(t)>1 and t[1:].isdigit():
            return True
        else:
            return False

    def Convert(self):
        t=self.t
        if t[0]=='C':           # for conversion of celcius to farenheit
            celcius=float(t[1:])
            farenheit=(celcius*9/5)+32
            print("The tempurature is:",round(farenheit,2),"degrees Farenheit")

        elif t[0]=='F':         # for conversion of farenheit to celcius
            farenheit=float(t[1:])
            celcius=(farenheit-32)*5/9
            print("The tempurature is:",round(celcius,2),"degrees Celcius")

def main():
    temp= input("Enter the temperature with prefix C for celsius and F for fahrenheit: ")
    obj1 = TempConverter(temp)
    if obj1.validate():     # validate input for prefic C or F
        obj1.Convert()      # only calculate if entered value is valid
    else:
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix only")    #displays error if validate is false

if __name__ == "__main__":
    main()
