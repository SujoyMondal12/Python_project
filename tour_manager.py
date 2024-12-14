import csv

# File names
participants_file = "participants.csv"
payments_file = "payments.csv"
schedule_file = "schedule.csv"

def main_menu():
    while True:
        print("\n--- Chemistry Department Annual Tour Manager ---")
        print("1. Register Participant")
        print("2. View Registered Participants")
        print("3. Edit Participant Details")
        print("4. Delete Participant")
        print("5. Payment Tracking")
        print("6. Manage Tour Schedule")
        print("7. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register_participant()
        elif choice == "2":
            view_participants()
        elif choice == "3":
            edit_participant()
        elif choice == "4":
            delete_participant()
        elif choice == "5":
            payment_tracking()
        elif choice == "6":
            manage_schedule()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

def register_participant():
    print("\n--- Register Participant ---")
    name = input("Enter name: ")
    student_id = input("Enter student ID: ")
    contact = input("Enter contact number: ")
    with open(participants_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, student_id, contact])
    print(f"Participant {name} registered successfully!")

def view_participants():
    print("\n--- Registered Participants ---")
    try:
        with open(participants_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print("Name:", row[0], "| ID:", row[1], "| Contact:", row[2])
    except FileNotFoundError:
        print("No participants registered yet.")

def edit_participant():
    print("\n--- Edit Participant Details ---")
    student_id = input("Enter the Student ID of the participant to edit: ")
    participants = []
    updated = False

    try:
        # Read participants from file
        with open(participants_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                participants.append(row)
        
        # Search for participant
        for i, participant in enumerate(participants):
            if participant[1] == student_id:
                print(f"Found Participant: Name: {participant[0]}, ID: {participant[1]}, Contact: {participant[2]}")
                # Get new details
                name = input("Enter new name (leave blank to keep unchanged): ")
                contact = input("Enter new contact number (leave blank to keep unchanged): ")
                if name.strip():
                    participants[i][0] = name
                if contact.strip():
                    participants[i][2] = contact
                updated = True
                print("Participant details updated successfully!")
                break
        
        if not updated:
            print("Participant with the given Student ID not found.")
        else:
            # Write updated participants back to file
            with open(participants_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(participants)
    except FileNotFoundError:
        print("No participants registered yet.")


def delete_participant():
    print("\n--- Delete Participant ---")
    student_id = input("Enter the Student ID of the participant to delete: ")
    participants = []
    deleted = False

    try:
        # Read participants from file
        with open(participants_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                participants.append(row)
        
        # Search for participant to delete
        for i, participant in enumerate(participants):
            if participant[1] == student_id:
                print(f"Participant Found: Name: {participant[0]}, ID: {participant[1]}, Contact: {participant[2]}")
                confirm = input("Are you sure you want to delete this participant? (yes/no): ").strip().lower()
                if confirm == "yes":
                    participants.pop(i)
                    deleted = True
                    print("Participant deleted successfully!")
                break
        
        if not deleted:
            print("Participant with the given Student ID not found.")
        else:
            # Write updated participants back to file
            with open(participants_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(participants)
    except FileNotFoundError:
        print("No participants registered yet.")
        
def payment_tracking():
    print("\n--- Payment Tracking ---")
    name = input("Enter participant's name: ")
    amount = input("Enter amount paid: ")
    with open(payments_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount])
    print(f"Payment of {amount} recorded for {name}.")

def manage_schedule():
    print("\n--- Manage Tour Schedule ---")
    print("1. Add Activity")
    print("2. View Schedule")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_activity()
    elif choice == "2":
        view_schedule()
    else:
        print("Invalid choice!")

def add_activity():
    print("\n--- Add Activity ---")
    time = input("Enter time: ")
    destination = input("Enter destination: ")
    notes = input("Enter additional notes: ")
    with open(schedule_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([time, destination, notes])
    print("Activity added successfully!")

def view_schedule():
    print("\n--- Tour Schedule ---")
    try:
        with open(schedule_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print("Time:", row[0], "| Destination:", row[1], "| Notes:", row[2])
    except FileNotFoundError:
        print("No schedule created yet.")

# Run the program
if __name__ == "__main__":
    main_menu()