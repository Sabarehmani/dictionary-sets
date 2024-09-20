dictionary = {
    "cat" : "a small animal",
    "table" : ("a piece of furniture" , "lists of facts and  figures")
    }

print(dictionary)

subjects = {
    "python", "java", "c++", "python", "javascript", "java",
    "python", "java", "c++", "c"
}

print(len(subjects))

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

print(marks)