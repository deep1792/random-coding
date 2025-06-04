
#print(ord('a'))   - to print the ASCII value
#print(chr(97))    - to print the character value of the ASCII


#function definition
import random
def generate_password(length=8) :

#special characters

	list1 = ['@','#','!','$','%','^','&','*']
	upper_case = chr(random.randint(65,90))
	lower_case = chr(random.randint(97,122))
	special_characters = random.choice(list1)
	numeric = random.randint(100000,999999)  #defining 6 letter word rom min to max
	final_password = upper_case + lower_case + special_characters + str(numeric) #as digit is in numeric and combinig with string will create an error, so convert digit to  string
	list1 = random.sample(final_password,length)
	final_password = ("").join(list1)
	return final_password

#function call

final_result = generate_password(8)
print(final_result)



