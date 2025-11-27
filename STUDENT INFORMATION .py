# COC Student Information System

# --- LOGIN SYSTEM ---
username = "Student"
password = "12345678"

print("---> LOGIN <---")
user = input("Enter username: ")
pw = input("Enter password: ")

if user != username or pw != password:
    print("Login failed! Exiting program...")
    exit()

print("\nLogin successful!\n")

# --- STUDENT DATABASE ---
students = {}

# --- FUNCTIONS ---

def add_student():
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    section = input("Enter Section: ")
    course = input("Enter Student Course: ")
    age = input("Enter Student Age: ")
    address = input("Enter Address: ")
    contact = input("Enter Contact Number: ")

    students[student_id] = {
        "Name": name,
        "Section": section,
        "Course": course,
        "Age": age,
        "Address": address,
        "Contact": contact
    }

    print("Student added successfully!")


def edit_student():
    print("\n--- Edit Student ---")
    student_id = input("Enter Student ID to edit: ")

    if student_id not in students:
        print("Student not found!")
        return

    print("To maintain the current value, leave blank.")

    name = input(f"Name ({students[student_id]['Name']}): ")
    section = input(f"Section ({students[student_id]['Section']}): ")
    course = input(f"Course ({students[student_id]['Course']}): ")
    age = input(f"Age ({students[student_id]['Age']}): ")
    address = input(f"Address ({students[student_id]['Address']}): ")
    contact = input(f"Contact ({students[student_id]['Contact']}): ") 

    students[student_id] = {
        "Name": name,
        "Section": section,
        "Course": course,
        "Age": age,
        "Address": address,
        "Contact": contact
    }

    print("Student details updated!")


def delete_student():
    print("\n--- Delete Student ---")
    student_id = input("Enter Student ID to delete: ")

    if student_id not in students:
        print("Student not found!")
        return

    del students[student_id]
    print("Student deleted successfully!")


def show_students():
    print("\n--- All Students ---")
    if not students:
        print("No records found.")
        return

    for sid, info in students.items():
        print(f"\nStudent ID: {sid}")
        for key, value in info.items():
            print(f"{key}: {value}")
    print()


# --- DASHBOARD ---
while True:
    print("\n---> DASHBOARD <---")
    print("[1] Add Student")
    print("[2] Edit Student")
    print("[3] Delete Student")
    print("[4] View All Students")
    print("[5] Logout")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        edit_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        show_students()
    elif choice == "5":
        print("You have been logged out.")
        break
    else:
        print("Invalid option, try again.")