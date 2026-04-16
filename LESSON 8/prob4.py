#Case Checker

#Given of subjects with inconsistent casing and extra spaces, use a list comprehension
#to clear this cases (remove whitespaces using .strip and change to title case)


raw_subjects = ["      mATH", "Sci ENC E", " eng lish", "pE", "Pr oGramminG "]
  
                 # [expression                   for item  in iterable     if condition]
clean_subjects = [clean.replace(" ", "").title() for clean in raw_subjects ]

print(clean_subjects)
#expected output : [Math, Science, English, Pe, Programming]