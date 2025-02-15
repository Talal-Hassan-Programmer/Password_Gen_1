from funcs import Gen_Pass

length = int(input("Enter the length of the password: "))
upper = input("Use uppercase letters? (y/n): ").lower() == "y"
digits = input("Use digits? (y/n): ").lower() == "y"
special = input("Use special characters? (y/n): ").lower() == "y"

gen = Gen_Pass(length, upper, digits, special)

password = gen.generate()

print("Generated password:", password)


save = input("Save password to file? (y/n): ").lower() == "y"  
if save:
    gen.save_pass(password)
