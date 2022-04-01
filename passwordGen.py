"""
Description:
Program solve generating password. 
Security level requirements:
 o password length of ten characters
 o contain minimum three characters from different character groups.
Character groups are uppercase, lowercase, digits and special characters.
Credits:
Orginaly written by MATBAL in Feb 2021, remastered Mar 2022 (edited in Vi).
"""

import random


def checkGroup(new_char, group):
    """
    Purpose: 
    Check if character is in the group. 
    Parameters:
    'new_char' is object with character data type.
    'group'is an object with string data type. 
    Principle:
    Compare character by character in group string.
    Returns:
    True if character is in the group string.
    False if character is not in the group string.
    """

    for char in group:
        if new_char == char:
            return True
    return False
        
def checkMinGroups(groups_index_num):
    """
    Purpose:
    Check if the index indicates three different groups. 
    Parameters:
    'groups_index_num' has an integer data type.
    Principle:
    Create a groups index string based on groups index number.
    Eventually add zeros at the beginning to have four character length string.
    Count zeros in the index string.
    Zero indicates that password's characters has not representation in characters group.
    As we have four groups of characters, more than one zero means False return.
    Returns:
    True if were indicated minimum three different groups, False in other cases.
    """

    groups_index = ""
    zero_count = 0
   
    #Create a groups index string.Add zeros eventually.
    if groups_index_num < 100:
        groups_index = "00" + str(groups_index_num)
    elif groups_index_num < 1000:
        groups_index = "0" + str(groups_index_num)
    else :
        groups_index = str(groups_index_num)
    
    #Count zeros in groups index
    for i in groups_index:
        if i == "0":
            zero_count = zero_count+1 
            
    if zero_count >1:
        return False

    return True 


print
print("Generating a new strong password...")

#Definition of variables
#Character groups 
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_characters = "+-*/,.?!@#$%^&_= "
#Password string
password = ""
#All characters
character_base = lower_case + upper_case + digits + special_characters 
base_length = len(character_base)
#Groups index number
groups_index_num = 0;
#Print variables; offset,quotation
p_offset = "        "
p_quotation = '"' 
p_asterix = '*'

while checkMinGroups(groups_index_num)!= True :

   #Generate ten characters 
   for i in range(10):
        new_random_number = random.randint(0,base_length-1)
        new_char = character_base[new_random_number]
        password = password + new_char
   
        #Calculating the groups index number
        groups_index_num = groups_index_num + 1*int(checkGroup(new_char, lower_case))
        groups_index_num = groups_index_num + 10*int(checkGroup(new_char, upper_case))
        groups_index_num = groups_index_num + 100*int(checkGroup(new_char, digits))
        groups_index_num = groups_index_num + 1000*int(checkGroup(new_char, special_characters))

#Print section
print
print
print(p_offset + p_offset + p_asterix +"New password is : " + p_quotation + password + p_quotation + p_offset + p_offset )
print
print
print
print(p_offset + p_offset + p_offset + p_offset + p_asterix + "surrounded by doublequotes" )
print
print

