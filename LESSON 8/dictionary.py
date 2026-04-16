students = [
    {"name":'Lovely', "gwa": 1.25, "year": 4},
    {"name":'Justin', "gwa": 3.00, "year": 2},
    {"name":'Biegh', "gwa": 2.50, "year": 2}, 
    {"name":'John', "gwa": 3.00, "year": 3},
]

year2_students = [student["name"] for student in students if student["year"] == 2]
honors = [student["name"] for student in students if student["gwa"] <= 2.50]

remarks = ["passed" if student["gwa"] <= 2.50 else "failed" for student in students]

print(year2_students)
print(honors)
print(remarks)