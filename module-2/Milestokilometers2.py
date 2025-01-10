#Miles is defined by miles_to_kilometers function
def miles_to_kilometers(miles):
    return miles * 1.60934 #miles times the amount of kilometers that make a mile

#User has to try and input a number of miles
try: 
    miles = float(input("Please enter the number of miles you have driven:"))

    #Miles is less than zero 
    if miles < 0:
        print("Please enter a positve number of miles.") #User will recieve message if they enter a negative number

    else: #User recieves message on miles being equal to number of kilometers after return calculation
        print(f"{miles} miles is equal to {miles_to_kilometers(miles):.2f} kilometers.")

#if User does not enter a number value the print message will appear
except ValueError:
    print("Invalid input. Please enter a number.") 