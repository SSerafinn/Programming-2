#list = []
#tuple = ()
#dict = {}

student = {
    "name": "Andre Manuel",
    "id_number": "2024-01384",
    "gwa": 1.43,
    "year_level": 3,
    "is_Scholar": True
}

student["gwa"] = 1.23

print(student["gwa"])

#del student["gwa"]

#dictionary.get("key", "fallbact")
#print(student.get("grades", "No Key"))


#if "gwa" in student:
#    print("existing")
#else:
#    print("not existing")

#dictionary.key() = returns every single key in the dictionary
#dictionary.values()= returns every single key in the dictionary
#dictionary.items()=returns every single key and value pair in the dictionary

#dictionary.update(x)
#dictionary.pop(x,y)
#dictionary.setdefault(k,v)
#len(dict)


#accessing

#for key in student:
#    print(key)

#for values in student.values():
#    print(values)

for key, value in student.items():
    print(f"{key}:{value}")
    
    
