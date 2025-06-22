universite = [ 
    { 
        "student_name": "Alex",
        "student_age":                  "                22" ,
        "student_course":        "           Civil Engineer",
        "student_lecture_note":         "                   56"
    },
    {
        "student_name": "Pedro",
        "student_age":                  "               25" ,
        "student_course":       "           Machine Engineer",
        "student_lecture_note":         "                 60"
    },
    {
        "student_name": "Martha",
        "student_age":                  "              21" ,
        "student_course":      "           Computer Science",
        "student_lecture_note":         "                 70"
    },
    {
        "student_name": "Emily",
        "student_age":                  "               23" ,
        "student_course":       "           Computer Programing",
        "student_lecture_note":         "              68"
    },
    {
        "student_name": "Isabell",
        "student_age":                      "             19" ,
        "student_course":        "           Software Engineer",
        "student_lecture_note":         "                45"
    },
    {
        "student_name": "Ali",
        "student_age":              "                 22" ,
        "student_course":         "           Art",
        "student_lecture_note":               "                              40"
    },
    {
        "student_name": "Felix",
        "student_age":              "               22" ,
        "student_course":         "           History",
        "student_lecture_note":          "                          65"
    },
    {
        "student_name": "Leo",
        "student_age":              "                 19" ,
        "student_course":          "           Geography",
        "student_lecture_note":      "                        30"
    },
    { 
        "student_name": "Elizabeth",
        "student_age":                "           26" ,
        "student_course":             "           Biology",
        "student_lecture_note":        "                          90"
    },
    {
        "student_name": "Valdez",
        "student_age":               "              27" ,
        "student_course":            "           Architecture",
        "student_lecture_note":       "                     80"
    },
    {
        "student_name": "Violet",
        "student_age":              "              25" ,
        "student_course":           "           Physic",
        "student_lecture_note":                  "                           70"
    },
    { 
        "student_name": "Natalie",
        "student_age":               "             18" ,
        "student_course":              "           Genetics and Bioengineering",
        "student_lecture_note":                       "      92"
    },
    {
        "student_name": "Katarina",
        "student_age":                  "            28" ,
        "student_course":             "           Law",
        "student_lecture_note":       "                              95"
    },
    {
        "student_name": "Luca",
        "student_age":           "                29" ,
        "student_course":             "           Geological Engineering",
        "student_lecture_note":       "           70"
    },
    {
        "student_name": "Hazel",
        "student_age":             "               30" ,
        "student_course":            "           Chemistry",
        "student_lecture_note":           "                        69"
    }
]

print("")
print("Student_name     Student_age       Student_course           Student_lecture_note")
print("")

for university in universite:
    print(university["student_name"], university["student_age"], university["student_course"], university["student_lecture_note"])
print("")

Yas_ortalaması = [22, 25, 21, 23, 19, 22, 22, 19, 26, 27, 25, 18, 28, 29, 30]

print("Yaş Ortalaması: ", sum(Yas_ortalaması)/len(Yas_ortalaması))
print("")

Not_ortalaması = [56, 60, 70, 68, 45, 40, 65, 30, 90, 80, 70, 92, 95, 70, 69]

print("Not Ortalaması: ", sum(Not_ortalaması)/len(Not_ortalaması))