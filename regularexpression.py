import re

line = "Python is better than JS"

# matchObj = re.match( r'(.*) better (.*?) .*', line, re.M|re.I)

# if matchObj:
#    print (f"matchObj.group() : {matchObj.group()}")
#    print (f"matchObj.group(1) : {matchObj.group(1)}")
#    print (f"matchObj.group(2) : {matchObj.group(2)}")
# else:
#    print ("No match!!")

line = ("Devs are smarter than accountants")

# matchObj = re.match( r'dogs', line, re.M|re.I)
# if matchObj:
#    print ("matchObj.group() : ", matchObj.group())
# else:
#    print ("No match!!")

# searchObj = re.search( r'devs', line, re.M|re.I)
# if searchObj:
#    print ("search --> searchObj.group() : ", searchObj.group())
# else:
#    print ("Nothing found!!")

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
# num = re.sub(r'#.*$', "", phone)
# print ("Phone Num : ", num)

# Remove anything other than digits
# num = re.sub(r'\D', "", phone)    
# print ("Phone Num : ", num)

#email validator
# try:
#     email = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", "paco.ocampor@gmail.com")
#     print(email)
#     print(email.group())
# except re.error as error:
#     print(error)

# from email.utils import parseaddr
# print(parseaddr("paco,oil,com"))
# print(parseaddr("esto no es un mail"))

my_age = "Paco is 40 years old and Joes is 28 years old and Diego is 1028 years old"
age = re.findall(r'\d{3,3}', my_age)
print(age)
