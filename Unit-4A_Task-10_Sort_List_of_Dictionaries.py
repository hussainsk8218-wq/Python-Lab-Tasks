students=[{"name":"Hussain","marks":85},{"name":"Rehan","marks":92},{"name":"H","marks":78}]
ascending=sorted(students,key=lambda s:s["marks"])
descending=sorted(students,key=lambda s:s["marks"],reverse=True)
print("Ascending order:")
for student in ascending: print(student)
print("Descending order:")
for student in descending: print(student)
