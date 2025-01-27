import csv
import matplotlib.pyplot as plt

#The file path to the excel 
filename = 'C:\\Users\\tabar\Downloads\\sitka_weather_2018_simple.csv'

dates, highs, lows = [], [], [] 
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Dates and temperatures from this
    for row in reader:
        try:
            current_date = row[2]
            high = int(row[5])
            low = int(row[6]) 
        except ValueError:
            print(f"Missing data for {current_date}")
        else: 
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
#Plot highs for graph
def plot_highs():
    plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c= 'red', label='Highs')
    plt.title("Daily High Temperatures, 2018", fontsize=20)
    plt.xlabel("Date", fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16) 
    plt.legend()
    plt.show()

#Plot lows for grap
def plot_lows():
    plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, lows, c='blue', label='Lows')
    plt.title("Daily Low Temperatures, 2018", fontsize=20)
    plt.xlabel("Date", fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.legend()
    plt.show()

#Welcome message with choices
def main():
    print("""Welcome to the Sitka Weather View.
          
          Choose the following options:
          1. View High Temperatures
          2. View Low Temperatures
          3. Exit
          """)
    
    #User inputs three different choices 
    while True: 
        choice = input("Enter your choice: (1, 2, or 3): ").strip()

        if choice =='1':
            plot_highs()
        elif choice =='2':
            plot_lows()
        elif choice =='3':
            print("This is the end of the Weather View.")
            break
        else: 
            print("Invalid choice. Please enter 1,2, or 3.")

if __name__=="__main__":
    main()