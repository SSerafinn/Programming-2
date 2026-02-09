input_year = int(input("Enter the year: "))

#if_leap = (input_year % 4 == 0 and input_year % 100 != 0) or input_year % 400 ==0
#if if_leap:
#    print("Year is a leap year.")

if (input_year % 4 == 0 and input_year % 100 != 0) or input_year % 400 == 0:
    print("Year is a leap year.")