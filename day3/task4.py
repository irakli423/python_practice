# students = [("Alejandro", ["CompSci", "Physics"]),
#             ("Justin", ["Math", "CompSci", "Stats"]),
#             ("Ed", ["CompSci", "Accounting", "Economics"]),
#             ("Margot", ["InfSys", "Accounting", "Economics", "CommLaw"]),
#             ("Peter", ["Sociology", "Economics", "Law", "Stats", "Music"])]

# for (name, subjects) in students:
#     print(name, "takes", len(subjects), "courses")

# counter = 0
# for (name, subjects) in students:
#     for s in subjects:                 # a nested loop! chaqsovili cikli
#         if s == "CompSci":
#             counter += 1

# print("The number of students taking CompSci is", counter)

# studentebi = [("giorgi", ["matematika", "geografia", "inglisuri"]), 
# ("irakli", ["biologia", "qimia", "rusuli"]), ("nika", ["fizika", "matematika"]), 
# ("lasha", ["matematika", "rusuli", "inglisuri"]), ("zura", ["fizika", "geografia", "inglisuri"])]

# for (name, subjects) in studentebi:
#     print(name, "takes", len(subjects), "course")

# counter = 0
# for (name, subjects) in studentebi:
#     for s in subjects:
#         if s == "inglisuri":
#             counter +=1

# print("the number of students taking inglisuri is", counter)

# studentebi = [("giorgi", ["fizika", "rusuli", "matematika"]), 
# ("irakli", ["inglisuri", "geografia", "biologia"]), 
# ("nika", ["matematika", "geografia", "rusuli"]), 
# ("zura", ["inglisuri", "fizika", "biologia"]),
# ("lasha", ["geografia", "qimia", "fizika"])]

# for (name, subjects) in studentebi:
#     print(name, "takes", len(subjects), "course")

# studentebi = [("giorgi",["fizika", "qimia", "biologia"]), 
# ("irakli", ["matematika", "inglisuri", "biologia"]), 
# ("nika", ["inglisuri", "matematika", "qimia"]), 
# ("zura", ["rusuli", "fizika", "qimmia"]), 
# ("lasha", ["rusuli", "inglisuri", "matematika"])]

# for (name, subject) in studentebi:
#     print(name, "take", len(subject), "course")

# studentebi = [("giorgi", ["matematika", "inglisuri", "rusuli"]), 
# ("irakli", ["inglisuri", "matematika", "fizika"]), 
# ("nika", ["geografia", "inglisuri", "matematika"]), 
# ("zura", ["fizika", "qimia", "matematika"]), 
# ("lasha", ["geografia", "rusuli", "inglisuri"])]

# for (name, subjects) in studentebi:
#     print(name, "take", len(subjects), "course")

studentebi = [("giorgi", ["geografia", "rusuli", "inglisuri"]), 
("irakli", ["inglisuri", "rusuli", "geografia"]), 
("nika", ["rusuli", "matematika", "inglisuri"]), 
("lasha", ["istoria", "inglisuri", "rusuli"]),
("zura", ["inglisuri", "qartuli", "fizika"])]

# for (name, subject) in studentebi:
#     print(name, "takes", len(subject), "course")

# counter = 0
# for (name, subject) in studentebi:
#     for s in subject:
#         if s == "inglisuri":
#             counter += 1

# print("inglisurebis raodenoba", counter)

counter = 0
for (name, subject) in studentebi:
    for s in subject:
        if s == "inglisuri":
            counter += 1
print("inglisuris raodebona", counter)