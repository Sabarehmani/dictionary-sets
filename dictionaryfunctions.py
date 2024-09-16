student = {
    "name" : "saba rehmani",
    "subjects" : {
        "phy" : 65,
        "chem" : 23,
        "maths" : 89,
     
    }
}
print(len(student))
print(len(list(student.keys())))

student = {
    "name" : "saba rehmani",
    "subjects" : {
        "phy" : 65,
        "chem" : 23,
        "maths" : 89,
     
    }
}

print(student.values())

student = {
    "name" : "saba rehmani",
    "subjects" : {
        "phy" : 65,
        "chem" : 23,
        "maths" : 89,
     
    }
}

print(student.items())

student = {
    "name" : "saba rehmani",
    "subjects" : {
        "phy" : 65,
        "chem" : 23,
        "maths" : 89,
     
    }
}

print(student["name"])
print(student.get("name"))

student = {
    "name" : "saba rehmani",
    "subjects" : {
        "phy" : 65,
        "chem" : 23,
        "maths" : 89,
     
    }
}

student.update({"city" : "Karachi"})
print(student)