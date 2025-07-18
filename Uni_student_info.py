students = []
Max_students = 10

def student_number():
    while True:
        number = input("Number of students to be enrolled: ").strip()
        if not number.isdigit():
            print("You have to write a number.")
            continue
        number = int(number)
        if number == 0:
            print("Zero cannot be entered. Please try again.")
        elif number > Max_students:
            print("A maximum of 10 students can enter.")
        else:
            return number
                

def student_name():
    while True:
        name = input("Name: ")
        if not name:
            print("You cannot leave your name blank.")
            continue
        if not name.isalpha():
            print("Name must contain only letters.")
            continue
        if len(name) >= 7:
            print("Name should be shorter than 7 letters.")
            continue
        return name


def student_surname():
    while True:
        surname = input("Surname: ")
        if not surname:
            print("You cannot leave your surname blank.")
            continue
        if not surname.isalpha():
            print("Surname must contain only letters.")
            continue
        if len(surname) <= 5:
            print("Surname should be longer than 5 letters.")
            continue
        return surname
       

def student_age():
    while True:
        age_input = input("Your age: ")
        if not age_input:
            print("Do not leave age blank.")
            continue
        if not age_input.strip().isdigit():
            print("Please enter age using numbers.")
            continue
        age = int(age_input)

        if age >= 19:
            print("You can continue.")
            return str(age)

        # 10–18 arası yaşlara göre sınıf belirle
        if age == 18:
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

        print("You can't go university.")
        return f"{age} (Middle/High School - {level})"
            
    

def student_city():
    while True:
        city = input("City: ").strip()
        if not city:
            print("City cannot be blank.")
            continue
        
        parts = city.split()

        if len(parts) < 1 or len(parts) > 3:
            print("City must be 1 to 3 words.")
            continue
        return city
    
def student_uni():
    while True:
        uni = input("Uni: ").strip()
        parts = uni.split()
        if not len(parts) == 2:
            print("Please enter exactly TWO words for the university name.")
        age = input("Age: ")
        if int(age) <=18:
            print("You can't go university.") 
            continue
        break



    
   

# Ana işlem:
num_students = student_number()

for num in range(num_students):
    print(f"\nStudent {num+1} Entry\n")
    name = student_name()
    surname = student_surname()
    age = student_age()
    city = student_city()
    uni = student_uni()

    # Tek bir sözlükte tüm bilgileri topla
    student = {
        "Name": name,
        "Surname": surname,
        "Age": age,
        "City": city,
        "Universite": uni
    }
    
    students.append(student)
    

# Rapor
print("\nStudent İnformation:\n ")
print(f"{'Name':<10} {'Surname':<12} {'Age':<5} {'City':<20} {'University':<25}\n")
for student in students:
    print(f"{student['Name']:<10} {student['Surname']:<12} {student['Age']:<5} {student['City']:<20} {student['University']:<25}")











