from weather import *
    
filename = "weather.dat"

choice = 0
while True:
    print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n\n\n")

    print("1. Set data filename")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Print historical report")
    print("9. Exit the program\n")
    
    choice = input("Enter menu choice: ")

    if choice == '1':
        thefilename = input("Enter data filename: ")
        file = read_data(thefilename)

    elif choice == '2':
        date = input("Enter date (YYYYMMDD): ")
        time = input("Enter time (hhmmss): ")
        temp = int(input("Enter temperature: "))
        humid = int(input("Enter humidity: "))
        rain = float(input("Enter rainfall: "))
        file[date + time] = {"t": temp, "h": humid, "r": rain}
        write_data(data = file, filename = thefilename)

    elif choice == '3':
        daily = input("Enter date (YYYYMMDD): ")
        dispDaily = report_daily(file, daily)
        print(dispDaily)

    elif choice == '4':
        dispHistorical = report_historical(file)
        print(dispHistorical)

    elif choice == '9':
        break

    else:
        print("Invalid\n")