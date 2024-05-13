import datetime


members = []
sponsors = []

while True:
    print("\nFriends of Seaview Pier")
    print("1. Become a Member")
    print("2. List Members")
    print("3. Sponsor a Wooden Plank")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        # Task 1 - becoming a member of Friends of Seaview Pier
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        volunteer = input("Do you want to volunteer? (yes/no): ").lower() == 'yes'
        volunteer_area = input("Choose volunteer area (gate/gift shop/painting): ").lower() if volunteer else None
        join_date = datetime.date.today().strftime("%Y-%m-%d")
        fee_paid = input("Have you paid the $75 fee? (yes/no): ").lower() == 'yes'

        member = {
            'first_name': first_name,
            'last_name': last_name,
            'volunteer_area': volunteer_area,
            'join_date': join_date,
            'fee_paid': fee_paid
        }

        members.append(member)

        if volunteer_area:
            print(f"You have joined as a volunteer in the {volunteer_area} area.")
        else:
            print("You have joined as a member.")

    elif choice == '2':
        # Task 2 - using the membership data
        category = input("Enter the category (volunteers/gate/gift shop/painting/expired/unpaid): ").lower()
        if category == 'volunteers':
            volunteers = [f"{member['first_name']} {member['last_name']}" for member in members if member['volunteer_area'] is not None]
            print("\n".join(volunteers))
        elif category in ['gate', 'gift shop', 'painting']:
            volunteers_by_area = [f"{member['first_name']} {member['last_name']}" for member in members if member['volunteer_area'] == category]
            print("\n".join(volunteers_by_area))
        elif category == 'expired':
            current_year = datetime.date.today().year
            expired_members = [f"{member['first_name']} {member['last_name']}" for member in members if member['join_date'][:4] != str(current_year)]
            print("\n".join(expired_members))
        elif category == 'unpaid':
            unpaid_members = [f"{member['first_name']} {member['last_name']}" for member in members if not member['fee_paid']]
            print("\n".join(unpaid_members))

    elif choice == '3':
        # Task 3 - sponsoring a wooden plank
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        message = input("Enter the message for the brass plaque: ")

        sponsor = {
            'first_name': first_name,
            'last_name': last_name,
            'message': message
        }

        print("\nConfirmation:")
        print(f"Name: {sponsor['first_name']} {sponsor['last_name']}")
        print(f"Message: {sponsor['message']}")

        confirmation = input("Is the information correct? (yes/no): ").lower()
        if confirmation == 'yes':
            sponsors.append(sponsor)
            print("Thank you for sponsoring a wooden plank! You have been charged $200.")
        else:
            print("Data not saved. Please re-enter the information.")

    elif choice == '4':
        # Exit
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
