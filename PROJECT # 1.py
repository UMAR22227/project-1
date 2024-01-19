# Student data for Class 9
class_9_students = [
    {"Roll Number": "1276", "Name": "Ali", "Father Name": "Khalid", "Result": "Pass"},
    {"Roll Number": "1277", "Name": "Sara", "Father Name": "Rizwan", "Result": "Fail"},
    {"Roll Number": "1278", "Name": "Ahmed", "Father Name": "Imran", "Result": "Pass"},
    {"Roll Number": "1279", "Name": "Aisha", "Father Name": "Nadeem", "Result": "Pass"},
    {"Roll Number": "1280", "Name": "Bilal", "Father Name": "Yasin", "Result": "Fail"},
    {"Roll Number": "1281", "Name": "Fatima", "Father Name": "Iqbal", "Result": "Pass"},
    {"Roll Number": "1282", "Name": "Kamran", "Father Name": "Tariq", "Result": "Fail"},
    {"Roll Number": "1283", "Name": "Mehak", "Father Name": "Akram", "Result": "Pass"},
    {"Roll Number": "1284", "Name": "Omar", "Father Name": "Asif", "Result": "Fail"},
    {"Roll Number": "1285", "Name": "Zainab", "Father Name": "Saeed", "Result": "Pass"}
]

# Student data for Class 10
class_10_students = [
    {"Roll Number": "5271", "Name": "Amir", "Father Name": "Rashid", "Result": "Pass"},
    {"Roll Number": "5272", "Name": "Hira", "Father Name": "Yousuf", "Result": "Fail"},
    {"Roll Number": "5273", "Name": "Usman", "Father Name": "Tahir", "Result": "Pass"},
    {"Roll Number": "5274", "Name": "Sadia", "Father Name": "Faisal", "Result": "Pass"},
    {"Roll Number": "5275", "Name": "Nabeel", "Father Name": "Javed", "Result": "Fail"},
    {"Roll Number": "5276", "Name": "Rabia", "Father Name": "Rauf", "Result": "Pass"},
    {"Roll Number": "5277", "Name": "Farhan", "Father Name": "Salman", "Result": "Fail"},
    {"Roll Number": "5278", "Name": "Ayesha", "Father Name": "Ahmed", "Result": "Pass"},
    {"Roll Number": "5279", "Name": "Aliya", "Father Name": "Riaz", "Result": "Fail"},
    {"Roll Number": "5280", "Name": "Saad", "Father Name": "Irfan", "Result": "Pass"}
]

# Function to display all students in a specific class
def display_students(class_students):
    if not class_students:
        print("No students in this class.")
    else:
        print("\nAll Students in the Class:")
        for student in class_students:
            print(f"Roll Number: {student['Roll Number']}, Name: {student['Name']}, Father Name: {student['Father Name']}, Result: {student['Result']}")
        print()

# Main program
while True:
    print("\nStudent Database Management System")
    print("1. Display Students in Class 9")
    print("2. Display Students in Class 10")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        display_students(class_9_students)

    elif choice == "2":
        display_students(class_10_students)

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")