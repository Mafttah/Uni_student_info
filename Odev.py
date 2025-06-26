import colorama
from colorama import Fore

student_list = [
    {
        "student_name": "Oliver",
        "student_surname": "Williams",
        "student_age": "19",
        "student_city": "San Francisco",
        "student_university": "Stanford University",
        "student_course": "Art",
        "student_notes": "45, 80, 65",
        "student_hobbies": "Football, Hockey, Skating"
    },
    {
        "student_name": "Olivia",
        "student_surname": "Brown",
        "student_age": "21",
        "student_city": "Oxford",
        "student_university": "Oxford University",
        "student_course": "Geography",
        "student_notes": "90, 71, 83",
        "student_hobbies": "Tennis, Skiing, Padel"
    },
    {
        "student_name": "Richard",
        "student_surname": "Miller",
        "student_age": "28",
        "student_city": "Edinburgh",
        "student_university": "Edinburgh University",
        "student_course": "History",
        "student_notes": "80, 65, 72",
        "student_hobbies": "Football, Basketball, Golf"
    },
    {
        "student_name": "Sarah",
        "student_surname": "Rogriguez",
        "student_age": "22",
        "student_city": "Zurich",
        "student_university": "ETH Zurich University",
        "student_course": "Chemistry",
        "student_notes": "73, 86, 56",
        "student_hobbies": "Baseball, Cricket, Surfing"
    },
    {
        "student_name": "George",
        "student_surname": "Smith",
        "student_age": "27",
        "student_city": "Cambridge",
        "student_university": "Cambridge University",
        "student_course": "AI",
        "student_notes": "34, 54, 90",
        "student_hobbies": "Football, Basketball, Tennis"
    },
    {
        "student_name": "Tracy",
        "student_surname": "Taylor",
        "student_age": "20",
        "student_city": "Tokyo",
        "student_university": "Tokyo University",
        "student_course": "Finance", 
        "student_notes": "80, 46, 74",
        "student_hobbies": "Tennis, Art, Swimming"
    }
]

students = []

while True:
    print(Fore.WHITE)
    student_number = input("Number of students to be enrolled: ")
    if student_number == "" :
        print(Fore.RED, "You have to write number.")
        print(Fore.RED, "Go Back")
        print("")
        student_number = f"{student_number: }"
        continue
    if not student_number.strip().isdigit():
        print(Fore.RED,"You must enter a number for information.")
        print(Fore.WHITE,"Go Back")
        print("")
        continue
    break
print("")

#for student_number in student_list:
#    print(f"{student_number}. Student_information: ")
# print(f"{'Student_name':<13}/ {'Student_surname':<17}/ {'Student_age':<13}/ {'Student_city':<14}/ {'Student_university':<21}/ {'Student_course':<15}/ {'Student_notes':<17}/ {'Student_hobbies':<18}") 

# print(f"{'------------':<13} {'----------------':<17} {'-------------':<15} {'-------------':<16} {'------------------':<22} {'-------------':<16} {'---------------':<17} {'---------------':<18}")


# for students_number in student_list:
#    print(f"{(students_number["student_name"]).strip():^14} {(students_number["student_surname"]).strip():^15} {(students_number["student_age"]).strip():^14} {(students_number["student_city"]).strip():^18} {(students_number["student_university"]).strip():<22} {(students_number["student_course"]).strip():^14} {(students_number["student_notes"]).strip():^19} {(students_number["student_hobbies"]).strip():<25}")

#for students_number in student_list:
while True: 
    print(Fore.WHITE)
    name = input("1. Name: ")
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
    student_age = input("Age: ")
    if student_age and int(student_age) - 19:
        print(Fore.RED, "You cannot leave the student_age information blank !")
        print(Fore.WHITE, "Go Back")
        student_age = int(student_age)
        student_age = f"{'19'}"
        continue
    if not student_age:
            print(Fore.RED, "You must enter number to enter student_age.") 
            print(Fore.WHITE, "Go Back")
            print("") 
            continue
    break
while True:
    print(Fore.WHITE)
    city_word1 = input("City First Word: ").strip()
    city_word2 = input("City Second Word: ").strip()
    student_city = f"{city_word1} {city_word2}"
    if city_word1 == "":
        if city_word2 == "":
            print(Fore.RED, "City must be exactly 2 words and contain only letters.")
        print(Fore.WHITE, "Go Back")
        continue
    if not city_word1.isalpha() and city_word2.isalpha():
        print(Fore.RED, "You must enter 2 words to enter student_city.") 
        print(Fore.RED, "You cannot leave the student_city information blank !")
        print(Fore.WHITE, "Go Back")
        print("")
        continue
    break 
while True:
    print(Fore.WHITE)
    uni_word1 = input("University First Word: ").strip()
    uni_word2 = input("University Second Word: ").strip() 
    student_university = f"{uni_word1} {uni_word2}"            
    if uni_word1 == "":
        if uni_word2 == "":
            print(Fore.RED, "City must be exactly 2 words and contain only letters.")
            print(Fore.RED, "You cannot leave the student_university information blank !")
            print(Fore.WHITE, "Go Back")
        continue
    if not uni_word1.isalpha() and uni_word2.isalpha():
        print(Fore.RED, "You cannot leave the student_university information blank !")
        print(Fore.WHITE, "Go Back")
        print("") 
        continue
    break
while True:
    print(Fore.WHITE)
    student_course = input("Course: ")
    if student_course == "":
        print(Fore.RED, "You cannot leave the student_course information blank !")
        print(Fore.WHITE, "Go Back") 
        continue       
    if not student_course.strip().isalpha():
        print(Fore.RED, "You must enter a word/words to enter student_course.") 
        print(Fore.WHITE, "Go Back")
        
        print("") 
        continue
    break
while True:
    print(Fore.WHITE)
    student_notes = input("Notes (3 tane, virgülle ayır): ").split(",")
    if student_notes == "":
        if len(student_notes) <3:
            print(Fore.RED, "You cannot leave the student_notes information blank !")
        print(Fore.WHITE, "Go Back")
        continue
    if not student_notes:
            print(Fore.RED, "You must enter a numbers to enter student_notes.") 
            print(Fore.WHITE, "Go Back")
            print("") 
            continue
    break
while True:
    print(Fore.WHITE)
    student_hobbies = input("Hobbies (3 tane, virgülle ayır): ").split(",") 
    if student_hobbies == "":
        if len(student_hobbies) <3:
            print(Fore.RED, "You cannot leave the student_hobbies blank !")
        print(Fore.WHITE, "Go Back")
        continue
    if not student_hobbies:
        print(Fore.RED, "You must enter a words to enter student_hobbies.") 
        print(Fore.WHITE, "Go Back")
        print("")
        continue
    break
print("")

# while True: 
#     print(Fore.WHITE)
#     name = input("2. Name: ")
#     if name == "": 
#         print(Fore.RED, "You cannot leave the Name information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not name.strip().isalpha():
#         print(Fore.RED, "You must enter a word to enter name.") 
#         print(Fore.WHITE, "Go Back")
#         continue
#     break
# while True:
#     print(Fore.WHITE)
#     surname = input("2. Surname: ")
#     if surname == "":   
#         print(Fore.RED, "You cannot leave the Surname information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not surname.strip().isalpha():
#         print(Fore.RED, "You must enter a word to enter Surname.") 
#         print(Fore.WHITE, "Go Back")
#         print("") 
#         continue
#     break
# while True:
#     print(Fore.WHITE)       
#     student_age = input("Age: ")
#     if student_age.isdigit() and int(student_age) == 21:
#         print(Fore.RED, "You cannot leave the student_age information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_age.strip().isdigit():
#             print(Fore.RED, "You must enter number to enter student_age.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_city = input("City (2 words): ").strip()
#     if student_city == "":
#         if len(student_city.split()) == 2 and all(c.isalpha() for c in student_city.replace(" ", "")):
#              continue
#         print(Fore.RED, "You cannot leave the student_university information blank !")
#         print(Fore.WHITE, "Go Back")
#     if not student_city.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_city.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)            
#     student_university = input("University (2 words): ").strip()
#     if student_university == "":
#         if len(student_university.split()) == 2 and all(c.isalpha() for c in student_university.replace(" ", "")):
#              continue
#         print(Fore.RED, "You cannot leave the student_university information blank !")
#         print(Fore.WHITE, "Go Back")
#     if not student_university.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_university.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_course = input("Course: ")
#     if student_course == "":
#         print(Fore.RED, "You cannot leave the student_course information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_course.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_course.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_notes = input("Notes (3 tane, virgülle ayır): ").split(",") 
#     if student_notes == "":
#         print(Fore.RED, "You cannot leave the student_notes information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_notes.strip().isdigit():
#             print(Fore.RED, "You must enter a numbers to enter student_notes.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_hobbies = input("Hobbies (3 tane, virgülle ayır): ").split(",")
#     if student_hobbies == "":
#         print(Fore.RED, "You cannot leave the student_hobbies blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_hobbies:
#         print(Fore.RED, "You must enter a word to enter student_hobbies.") 
#         print(Fore.WHITE, "Go Back")
#         print("")
#         continue
#     break
# print("")

# while True: 
#     print(Fore.WHITE)
#     name = input("3. Name: ")
#     if name == "": 
#         print(Fore.RED, "You cannot leave the Name information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not name.strip().isalpha():
#         print(Fore.RED, "You must enter a word to enter name.") 
#         print(Fore.WHITE, "Go Back")
#         continue
#     break
# while True:
#     print(Fore.WHITE)
#     surname = input("3. Surname: ")
#     if surname == "":   
#         print(Fore.RED, "You cannot leave the Surname information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not surname.strip().isalpha():
#         print(Fore.RED, "You must enter a word to enter Surname.") 
#         print(Fore.WHITE, "Go Back")
#         print("") 
#         continue
#     break
# while True:
#     print(Fore.WHITE)       
#     student_age = input("Age: ")
#     if student_age.isdigit() and int(student_age) == 28:
#         print(Fore.RED, "You cannot leave the student_age information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_age.strip().isdigit():
#             print(Fore.RED, "You must enter number to enter student_age.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_city = input("City (2 words): ").strip()
#     if student_city == "":
#         if len(student_city.split()) == 2 and all(c.isalpha() for c in student_city.replace(" ", "")):
#              continue
#         print(Fore.RED, "You cannot leave the student_university information blank !")
#         print(Fore.WHITE, "Go Back")
#     if not student_city.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_city.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)            
#     student_university = input("University (2 words): ").strip()
#     if student_university == "":
#         if len(student_university.split()) == 2 and all(c.isalpha() for c in student_university.replace(" ", "")):
#              continue
#         print(Fore.RED, "You cannot leave the student_university information blank !")
#         print(Fore.WHITE, "Go Back")
#     if not student_university.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_university.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_course = input("Course: ")
#     if student_course == "":
#         print(Fore.RED, "You cannot leave the student_course information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_course.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_course.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_notes = input("Notes (3 tane, virgülle ayır): ").split(",")
#     if student_notes == "":
#         print(Fore.RED, "You cannot leave the student_notes information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_notes.strip().isdigit():
#             print(Fore.RED, "You must enter a numbers to enter student_notes.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_hobbies = input("Hobbies (3 tane, virgülle ayır): ").split(",")
#     if student_hobbies == "":
#         print(Fore.RED, "You cannot leave the student_hobbies blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_hobbies:
#         print(Fore.RED, "You must enter a word/words to enter student_hobbies.") 
#         print(Fore.WHITE, "Go Back")
#         print("")
#         continue
#     break
# print("")

# while True: 
#     print(Fore.WHITE)
#     name = input("4. Name: ")
#     if name == "": 
#         print(Fore.RED, "You cannot leave the Name information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not name.strip().isalpha():
#         print(Fore.RED, "You must enter a word to enter name.") 
#         print(Fore.WHITE, "Go Back")
#         continue
#     break
# while True:
#     print(Fore.WHITE)
#     surname = input("4. Surname: ")
#     if surname == "":   
#         print(Fore.RED, "You cannot leave the Surname information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not surname.strip().isalpha():
#         print(Fore.RED, "You must enter a word to enter Surname.") 
#         print(Fore.WHITE, "Go Back")
#         print("") 
#         continue
#     break
# while True:
#     print(Fore.WHITE)       
#     student_age = input("Age: ")
#     if student_age.isdigit() and int(student_age) == 22:
#         print(Fore.RED, "You cannot leave the student_age information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_age.strip().isdigit():
#             print(Fore.RED, "You must enter number to enter student_age.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_city = input("City (2 words): ").strip()
#     if student_city == "":
#         if len(student_city.split()) == 2 and all(c.isalpha() for c in student_city.replace(" ", "")):
#              continue
#         print(Fore.RED, "You cannot leave the student_university information blank !")
#         print(Fore.WHITE, "Go Back")
#     if not student_city.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_city.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)            
#     student_university = input("University (2 words): ").strip()
#     if student_university == "":
#         if len(student_university.split()) == 2 and all(c.isalpha() for c in student_university.replace(" ", "")):
#              continue
#         print(Fore.RED, "You cannot leave the student_university information blank !")
#         print(Fore.WHITE, "Go Back")
#     if not student_university.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_university.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_course = input("Course: ")
#     if student_course == "":
#         print(Fore.RED, "You cannot leave the student_course information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_course.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_course.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_notes = input("Notes (3 tane, virgülle ayır): ").split(",")
#     if student_notes == "":
#         print(Fore.RED, "You cannot leave the student_notes information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_notes.strip().isdigit():
#             print(Fore.RED, "You must enter a numbers to enter student_notes.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_hobbies = input("Hobbies (3 tane, virgülle ayır): ").split(",")
#     if student_hobbies == "":
#         print(Fore.RED, "You cannot leave the student_hobbies blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_hobbies:
#         print(Fore.RED, "You must enter a word/words to enter student_hobbies.") 
#         print(Fore.WHITE, "Go Back")
#         print("")
#         continue
#     break
# print("")

# while True: 
#     print(Fore.WHITE)
#     name = input("5. Name: ")
#     if name == "": 
#         print(Fore.RED, "You cannot leave the Name information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not name.strip().isalpha():
#         print(Fore.RED, "You must enter a word to enter name.") 
#         print(Fore.WHITE, "Go Back")
#         continue
#     break
# while True:
#     print(Fore.WHITE)
#     surname = input("5. Surname: ")
#     if surname == "":   
#         print(Fore.RED, "You cannot leave the Surname information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not surname.strip().isalpha():
#         print(Fore.RED, "You must enter a word to enter Surname.") 
#         print(Fore.WHITE, "Go Back")
#         print("") 
#         continue
#     break
# while True:
#     print(Fore.WHITE)       
#     student_age = input("Age: ")
#     if student_age.isdigit() and int(student_age) == 27:
#         print(Fore.RED, "You cannot leave the student_age information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_age.strip().isdigit():
#             print(Fore.RED, "You must enter number to enter student_age.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_city = input("City (2 words): ").strip()
#     if student_city == "":
#         if len(student_city.split()) == 2 and all(c.isalpha() for c in student_city.replace(" ", "")):
#              continue
#         print(Fore.RED, "You cannot leave the student_university information blank !")
#         print(Fore.WHITE, "Go Back")
#     if not student_city.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_city.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)            
#     student_university = input("University (2 words): ").strip()
#     if student_university == "":
#         if len(student_university.split()) == 2 and all(c.isalpha() for c in student_university.replace(" ", "")):
#              continue
#         print(Fore.RED, "You cannot leave the student_university information blank !")
#         print(Fore.WHITE, "Go Back")
#     if not student_university.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_university.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_course = input("Course: ")
#     if student_course == "":
#         print(Fore.RED, "You cannot leave the student_course information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_course.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_course.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_notes = input("Notes (3 tane, virgülle ayır): ").split(",")
#     if student_notes == "":
#         print(Fore.RED, "You cannot leave the student_notes information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_notes.strip().isdigit():
#             print(Fore.RED, "You must enter a numbers to enter student_notes.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_hobbies = input("Hobbies (3 tane, virgülle ayır): ").split(",")
#     if student_hobbies == "":
#         print(Fore.RED, "You cannot leave the student_hobbies blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_hobbies:
#         print(Fore.RED, "You must enter a word/words to enter student_hobbies.") 
#         print(Fore.WHITE, "Go Back")
#         print("")
#         continue
#     break
# print("")

# while True: 
#     print(Fore.WHITE)
#     name = input("6. Name: ")
#     if name == "": 
#         print(Fore.RED, "You cannot leave the Name information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not name.strip().isalpha():
#         print(Fore.RED, "You must enter a word to enter name.") 
#         print(Fore.WHITE, "Go Back")
#         continue
#     break
# while True:
#     print(Fore.WHITE)
#     surname = input("6. Surname: ")
#     if surname == "":   
#         print(Fore.RED, "You cannot leave the Surname information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not surname.strip().isalpha():
#         print(Fore.RED, "You must enter a word to enter Surname.") 
#         print(Fore.WHITE, "Go Back")
#         print("") 
#         continue
#     break
# while True:
#     print(Fore.WHITE)       
#     student_age = input("Age: ")
#     if student_age.isdigit() and int(student_age) == 28:
#         print(Fore.RED, "You cannot leave the student_age information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_age.strip().isdigit():
#             print(Fore.RED, "You must enter number to enter student_age.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_city = input("City (2 words): ").strip()
#     if student_city == "":
#         if len(student_city.split()) == 2 and all(c.isalpha() for c in student_city.replace(" ", "")):
#              continue
#         print(Fore.RED, "You cannot leave the student_university information blank !")
#         print(Fore.WHITE, "Go Back")
#     if not student_city.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_city.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)            
#     student_university = input("University (2 words): ").strip()
#     if student_university == "":
#         if len(student_university.split()) == 2 and all(c.isalpha() for c in student_university.replace(" ", "")):
#              continue
#         print(Fore.RED, "You cannot leave the student_university information blank !")
#         print(Fore.WHITE, "Go Back")
#     if not student_university.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_university.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_course = input("Course: ")
#     if student_course == "":
#         print(Fore.RED, "You cannot leave the student_course information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_course.strip().isalpha():
#             print(Fore.RED, "You must enter a word/words to enter student_course.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_notes = input("Notes (3 tane, virgülle ayır): ").split(",")
#     if student_notes == "":
#         print(Fore.RED, "You cannot leave the student_notes information blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_notes.strip().isdigit():
#             print(Fore.RED, "You must enter a numbers to enter student_notes.") 
#             print(Fore.WHITE, "Go Back")
#             print("") 
#             continue
#     break
# while True:
#     print(Fore.WHITE)
#     student_hobbies = input("Hobbies: (3 tane, virgülle ayır): ").split(",")
#     if student_hobbies == "":
#         print(Fore.RED, "You cannot leave the student_hobbies blank !")
#         print(Fore.WHITE, "Go Back")
#         continue
#     if not student_hobbies:
#         print(Fore.RED, "You must enter a word/words to enter student_hobbies.") 
#         print(Fore.WHITE, "Go Back")
#         print("")
#         continue
#     break


#print(Fore.WHITE + f"{'------':<10} {'-------':<15} {'-------':<12} {'----------':<15} {'----------------':<12} {'------------':<12} {'--------------':<12} {'----------':<15}") 

#for students in student_list:
#    print(f"{(students["student_name"]).strip():<10} {(students["student_surname"]).strip():<10} {(students["student_age"]).strip():<20} {(students["student_city"]).strip():<15} {(students["student_university"]).strip():<20} {(students["student_course"]).strip():<30} {(students["student_notes"]).strip():<15} {(students["student_hobbies"]).strip():<15}")

students.append({
        "Name": name,
        "Surname": surname,
        "Age": student_age,
        "City": student_city,
        "University": student_university,
        "Course": student_course,
        "Hobbies": ", ".join(student_hobbies)
        })

print(Fore.RED + f"{'Name':<10} {'Surname':<12} {'Age':<15} {'City':<20} {'University':<25} {'Course':<12} {'Notes':<10} {'Hobbies':<15}")

for list in students:
    print(Fore.WHITE + f"{list['Name']:<10} {list['Surname']:<12} {list['Age']:<15} {list['City']:<20} {list['University']:<25} {list['Course']:<12} {'Notes':<10} {list['Hobbies']:<15}")