dict={"Nandita":90,"Kritika":81,"Priyanka":89,"Riya":76}
name=input("Enter the students's name: ")
if name in dict:
    print(f"{name}'s marks: {dict[name]}")
else:
    print("Student not found.")