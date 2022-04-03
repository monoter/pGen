"""
Description:
Program solve generating password. 
Security level requirements:
 o password length of ten characters
 o contain minimum three characters from different character groups.
Character groups are uppercase, lowercase, digits and special characters.
Credits:
Orginaly written by MATBAL in Feb 2021, remastered Mar/Apr 2022 (edited mostly in Vi).
"""

#random module 
import random

#stdout intro
print("\nGenerating strong password...")

#Definition of variables

#Character groups 
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = lower_case.upper()
digits = "0123456789"
spec_chars = "+-*/,.?!@#$%^&_= "

#Password string
password = ""
#All characters
character_base = lower_case + upper_case + digits + spec_chars

#Groups flags
groups_flags=[
[False,lower_case],
[False,upper_case],
[False,digits],
[False,spec_chars],
]


#Print variables; offset,quotation, etc.
p_offset = 2*"\t"
p_quotation = '"' 
p_asterix = '*'
p_newline = '\n'

# Loop untill new password has characters from minimum three groups
while [groups_flags[0][0], groups_flags[1][0], groups_flags[2][0], groups_flags[3][0]].count(True) < 3 :

   #Generate ten characters 
   for i in range(10):
        new_random_number = random.randint(0,len(character_base)-1)
        new_char = str(character_base)[new_random_number]
        password += new_char

	#Groups flags setting
	for n in range(len(groups_flags)):
		if new_char in groups_flags[n][1] :
			 groups_flags[n][0] = True

#Print section
print(2*p_newline + 2*p_offset + p_asterix +"New password is : " + p_quotation + password + p_quotation)
print(3*p_newline + 4*p_offset + p_asterix + "surrounded by doublequotes" + 2*p_newline )


