students = []
Max_students = 10

def student_number():
    while True:
        number = input("Number of students to be enrolled: ").strip()
        if number.isdigit():
            number = int(number)
            if 0 < number <= Max_students:
                return number
            print("Please enter between 1 and 10.")
        else:
            print("Please enter a valid number.")

def student_name():
    while True:
        name = input("Name: ").strip()
        if name.isalpha() and len(name) <= 7:
            return name
        print("Name must be letters only and shorter than 7 letters.")

def student_surname():
    while True:
        surname = input("Surname: ").strip()
        if surname.isalpha() and len(surname) > 5:
            return surname
        print("Surname must be letters only and longer than 5 letters.")

def student_age():
    while True:
        age = input("Your age: ").strip()
        if age.isdigit():
            age = int(age)
            if 19 <= age <= 22:
                return f"{age} (University student)"
            elif age > 22:
                return f"{age} (Looking for a job)"
            elif age == 18:
                level = "12. Grade"
            elif age == 17:
                level = "11. Grade"
            elif age == 16:
                level = "10. Grade"
            elif age == 15:
                level = "9. Grade"
            elif age == 14:
                level = "8. Grade"
            elif age == 13:
                level = "7. Grade"
            elif age == 12:
                level = "6. Grade"
            elif age == 11:
                level = "5. Grade"
            elif age == 10:
                level = "4. Grade"
            else:
                print("Too young to register.")
                continue

            print("You can't go to university.")
            return f"{age} (Middle/High School - {level})"
        else:
            print("Please enter a valid numeric age.")

def parse_age_number(age):
    try:
        return int(age.split()[0])
    except ValueError:
        return 0

def student_city():
    while True:
        city = input("City: ").strip()
        parts = city.split()
        if 1 <= len(parts) <= 3 and all(part.isalpha() for part in parts):
            return city
        print("City must be 1 to 3 words and only letters.")

def student_uni(age):
    if parse_age_number(age) < 18:
        return "N/A"
    while True:
        uni = input("University (2 words): ").strip()
        parts = uni.split()
        if len(parts) == 2 and all(part.isalpha() for part in parts):
            return uni
        print("University must be exactly two words and letters only.")

def student_course(age):
    if parse_age_number(age) < 18:
        return "N/A"
    while True:
        course = input("Course: ").strip()
        if course and course.replace(" ", "").isalpha():
            return course
        print("Course must contain only letters.")

def student_notes(age):
    if parse_age_number(age) < 18:
        return "N/A"
    while True:
        notes = input("Enter at least 3 grades (comma-separated): ").strip()
        parts = notes.split(",")
        grades = []

        for note in parts:
            note = note.strip()
            if note.isdigit():
                grades.append(int(note))

        if len(grades) < 3:
            print("Enter at least 3 valid numeric grades.")
        else:
            average = round(sum(grades) / len(grades))
            return grades, average    
        
def student_hobbies(age):
    if parse_age_number(age) < 18:
        return "N/A"
    while True:
        hobbies= input("Hobbies: at least 3 hobbies (comma-separated): ").strip()

        if len(hobbies) < 3:
            print("Enter at least 3 hobbies.")
        else:
            return hobbies


# Main process
num_students = student_number()

for i in range(num_students):
    print(f"\nStudent {i+1} Entry\n")
    name = student_name()
    surname = student_surname()
    age = student_age()
    city = student_city()
    university = student_uni(age)
    course = student_course(age)
    notes = student_notes(age)
    hobbies = student_hobbies(age)

    student = {
        "Name": name,
        "Surname": surname,
        "Age": age,
        "City": city,
        "University": university,
        "Course": course,
        "Notes": notes,
        "Hobbies": hobbies
    }
    students.append(student)

# Report
print(f"{'Name':<10} {'Surname':<12} {'Age':<35} {'City':<12} {'University':<25} {'Course':<12} {'Notes':<20} {'Hobbies'}")

for student in students:
    print(f"{student['Name']:<10} {student['Surname']:<12} {student['Age']:<35} {student['City']:<12} {student['University']:<25} {student['Course']:<12} {str(student['Notes']):<20} {student['Hobbies']}")




