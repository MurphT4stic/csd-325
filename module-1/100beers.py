#Tabari Harvey, 01/08/2025, Module 1.3 Assignment

def countdown_bottles (count): #The start of the code
    while count > 0:  
        if  count > 1: #if the count is larger than one from user input, it will continue with the lyrics until zero beers.
            print(f"{count} bottles of beer on the wall, {count} bottles of beer.")
        else: 
            print(f"{count} bottle of beer on the wall, {count} bottle of beer.")

        count -= 1 #The int input from user will be subtracted to continue the song

        if count > 0: 
            print(f"Take one down, pass it around, {count} bottles of beer on the wall.\n")

        else:
            print(f"Take one down, pass it around, no more bottles of beer on the wall.\n")

def main(): 

    try: #the user will see this question and then the lyrics will continue 
        bottles = int(input("How many bottles of beer are on the wall? "))
        if bottles > 1: 
            countdown_bottles(bottles) 

        else: 
            print("Please enter a number greater than 1.")

    except ValueError: #if the user does not input a number this will pop up
        print("Invalid input. Please enter a valid number.")

    print("No more bottles of beer on the wall.") 

if __name__=='__main__':
    main() #this is to close out the code keeping it seperate incase anything else is included.

