char_1 = input("Enter Character: ")

#alpha_num = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345'

if not char_1.isalpha() and not char_1.isdigit():
    print("Character is a special character.")

#if char_1 not in alpha_num:
#    print("Character is a special character.")