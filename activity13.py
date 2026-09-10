#Interger thing

name = input("Input thy name ----->  ")
age = int(input("Input thy age -----> "))

print("Greetings! Monarch", name, "It though seems that the is a:")
if age >= 1 and age <=5:
	print("Infant")
elif age >= 6 and age <=12:
	print("Kid")
elif age >= 13 and age <=19:
	print("Teenager")
elif age >= 20 and age <=29:
	print("Early Adult")
elif age >= 30 and age <=48:
	print("Adult")
elif age >= 49 and age <=59:
	print("Advance Adult")
elif age >= 60 and age <=150:
	print("Senior")
elif age >= 151:
	print("Immortal Being born from the depths below")

else:
	print("Invalid")
