import colorama
from colorama import Fore


students = []
Max_students = 10

while True:
    print(Fore.WHITE)
    student_number = input("Number of students to be enrolled: ")
    if student_number == "" :
        print(Fore.RED, "You have to write number.")
        print(Fore.WHITE, "Go Back")
        print("")
        student_number = int(student_number)
        continue
    if not student_number.strip().isdigit():
        print(Fore.RED,"You must enter a number for information.")
        print(Fore.WHITE,"Go Back")
        continue
    if student_number == 0:
        print("Minimum one student")
        continue
    break
print("")

print(Fore.GREEN + f"\nToplam {student_number} öğrenci kaydedilecektir.\n")
print("")


while True: 
    print(Fore.WHITE)
    name = input("1. Name: ")
    name = input("2. Name: ")
    name = input("3. Name: ")
    name = input("4. Name: ")
    name = input("5. Name: ")
    name = input("6. Name: ")
    if name == "": 
        print(Fore.RED, "You cannot leave the name information blank !")
        print(Fore.WHITE, "Go Back")
        continue
    if not name.isalpha():
        print(Fore.RED, "You must enter a word to enter name.") 
        print(Fore.WHITE, "Go Back")
        continue
    break
while True:
    print(Fore.WHITE)
    surname = input("1. Surname: ")
    surname = input("2. Surname: ")
    surname = input("3. Surname: ")
    surname = input("4. Surname: ")
    surname = input("5. Surname: ")
    surname = input("6. Surname: ")
    if surname == "":   
        print(Fore.RED, "You cannot leave the Surname information blank !")
        print(Fore.WHITE, "Go Back")
        continue
    if not surname.isalpha():
        print(Fore.RED, "You must enter a word to enter Surname.") 
        print(Fore.WHITE, "Go Back")
        print("") 
        continue
    break
while True:
    print(Fore.WHITE)       
    student_age = input("1. Age: ")
    student_age = input("2. Age: ")
    student_age = input("3. Age: ")
    student_age = input("4. Age: ")
    student_age = input("5. Age: ")
    student_age = input("6. Age: ")
    if student_age == "":
        print(Fore.RED, "You cannot leave the student_age information blank !")
        print(Fore.WHITE, "Go Back")
        continue
    if not student_age:
            print(Fore.RED, "You must enter number to enter student_age.") 
            print(Fore.WHITE, "Go Back")
            print("") 
            continue
    break


students.append({
        "Name": name,
        "Surname": surname,
        "Age": student_age,
})

print(Fore.RED + f"{'Name':<10} {'Surname':<12} {'Age':<15}")

for list in students:
    print(Fore.WHITE + f"{list['Name']:<10} {list['Surname']:<12} {list['Age']:<15}")

