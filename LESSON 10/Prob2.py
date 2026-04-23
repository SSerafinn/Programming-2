roster = [
    {"name": "Maria", "gwa": 1.50, "year": 2},
    {"name": "Juan",  "gwa": 2.25, "year": 3},
    {"name": "Ana",   "gwa": 1.75, "year": 2},
    {"name": "Carlo", "gwa": 3.00, "year": 3},
]

#List Comprehension
year3_student = [s["gwa"] for s in roster if s["year"] == 3]

#for student in roster:
#    if student["year"] == 3:
#        year3_student.append(student)

#Sort by grades using Lambda
year3_sorted = sorted(year3_student, key = lambda s: s["gwa"])

print(year3_sorted)
