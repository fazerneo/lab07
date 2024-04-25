import csv

# Created a menu
def menu():
    print()
    print("User Menu")
    print("1. Add staff details. Select 1")
    print("2. View staff details. Select 2")
    print("3. Exit Program. Select 3")
    User_input = int(input("Please enter the number corresponding to the action you want to perform: "))

    return User_input

# Initialize a while loop
while True:
    
    # Call menu and store the user input
    user_input = menu()
    
    if user_input == 1:
        ''' _________Option 1. Add Staff Details_________ '''
        # Open file in append mode so as to not overwrite data
        #create a writer object, take user input and store them in a list, then writerow to file
        with open("staff_details.csv", "a+", newline="", encoding="utf-8-sig") as csvfile:
            writer = csv.writer(csvfile)
            print()
            Staff_ID = input("Please enter the Staff ID: ")
            Staff_Name = input("Please enter the Staff Name: ")
            Phone = input("Please enter the Staff Phone Number: ")
            Home_Address = input("Please enter the staff's address: ")
            
            record = [Staff_ID, Staff_Name, Phone, Home_Address]
            writer.writerow(record)
            
            print("Record added successfully")

    elif user_input == 2:
        ''' _________Option 2. View Staff Details_________ '''
        # Open file in read mode, create a reader object
        # Iterate through reader object and print the data using indexing
        with open("staff_details.csv", newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.reader(csvfile)
            print()
            for col in reader:
                print(col[0],",", col[1],",", col[2],",", col[3])

    elif user_input == 3:
        ''' _________Option 3. Exit Program_________ '''
        print()
        print("Thank You for using the program")
        break
    