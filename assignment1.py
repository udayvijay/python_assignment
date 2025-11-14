# Name: uday vijay
# Roll No: 2501060136
# Cours: BCA
# Semster: 1st
# Subjet: Problem Solving with Python
# Assignment: Unit-1  Project
# Title: Student Profile 
# Date: 14 Nov 2025

print("WELCOM TO STUDENT PROFILE CONSOLE APP")

studname = input("Enter your full name: ")
rollnumber = input("Type roll number: ")
program = input("What program (ex. BCA): ")
univ = input("Give university name: ")

city = input("Which city you live in? ")
age = int(input("Your age? "))
hobby = input("Your hobby: ")

num_a = int(input("put first number: "))
num_b = int(input("put second number: "))

# Operators area
print("Arithmetic Opertars:")
print(str(num_a) + " + " + str(num_b) + " = " + str(num_a + num_b))
print(str(num_a) + " - " + str(num_b) + " = " + str(num_a - num_b))
print(str(num_a) + " * " + str(num_b) + " = " + str(num_a * num_b))
print(str(num_a) + " / " + str(num_b) + " = " + str(num_a / num_b))
print(str(num_a) + " % " + str(num_b) + " = " + str(num_a % num_b))
print(str(num_a) + " ** " + str(num_b) + " = " + str(num_a ** num_b))

# Assignments
temp = num_a
print("Assigment Oprtars:")
temp += 10
print("temp += 10", temp)
temp -= 2
print("temp -= 2", temp)
temp *= 3
print("temp *= 3", temp)

# Comparison
print("Comparsion Oprtars:")
print(str(num_a) + " == " + str(num_b), num_a == num_b)
print(str(num_a) + " > " + str(num_b), num_a > num_b)

# Logical
print("Logical Ops:")
print((num_a > 5) and (num_b > 5))
print((num_a < 0) or (num_b < 0))

# Identity
print("Ident Ops:")
print("numa is numb:", num_a is num_b)
print("numa is not numb:", num_a is not num_b)

# Membership
sampl_str = "Python Program"
print("Membership Ops:")
print("'P' in", sampl_str, 'P' in sampl_str)
print("'x' not in", sampl_str, 'x' not in sampl_str)

print("------ PYTHON STRING METHOD DEMO -------")
print("Big letters name:", studname.upper())           
print("Small city:", city.lower())                     
print("Nice Hobby:", hobby.title())                     
print("City with a->@:", city.replace("a", "@"))       

# Escape sequence demo
print("Newline si here\nSecond line seen!")         
print("Quote in string: \"python is nice\"")        

print("-------------STUDNT PROFILE SYSTEM---------------")
print("Name: " + studname)
print("Roll No: " + rollnumber)
print("Cours: " + program)
print("Univ: " + univ)
print("Cty: " + city)
print("Age: " + str(age))
print("Hobby: " + hobby)
print("------------------------------------------")
print("welcom to Python Programin!")
print("------------------------------------------")

saveit = input("save profile? (y/n): ")
if saveit.lower() == "y":
    fle = open("studnt_profile.txt", "w")
    fle.write("----- STUDNT PROFILE -----\n")
    fle.write("Name: " + studname + "\n")
    fle.write("Roll No: " + rollnumber + "\n")
    fle.write("Cours: " + program + "\n")
    fle.write("Univ: " + univ + "\n")
    fle.write("City: " + city + "\n")
    fle.write("Age: " + str(age) + "\n")
    fle.write("Hobby: " + hobby + "\n")
    fle.write("--------------------------\n")
    fle.close()
    print("Profile saved in studnt_profile.txt")
else:
    print("Profile not saved")