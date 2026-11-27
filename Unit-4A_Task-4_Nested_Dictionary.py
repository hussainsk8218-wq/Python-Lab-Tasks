students={1:{"name":"Hussain","marks":85},2:{"name":"Rehan","marks":90},3:{"name":"Karthik","marks":78}}
for roll,details in students.items():
    print("Roll Number:",roll)
    print("Name:",details["name"])
    print("Marks:",details["marks"])
    print()
