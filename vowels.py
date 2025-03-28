#string method
#upper()
name="valiva"
print(name.upper())
#lower()
print(name.lower())
#strip()
name="  valiva  "
print(name.strip())
#lstrip()
print(name.lstrip())
#rstrip()
print(name.rstrip())
#replace
string="my name is valiva" 
print(name.replace("v","V"))
print(name.replace("name",("NAME")))
#startwith()
string="valiva"
print(string.startswith("V"))
#endswith()
print(string.endswith("A"))
#find()
string="my name is valiva"
print(string.find("m"))
#count()
string="java,python,html,js,Php"
print(string.count("ph"))
#capitalize()
string="my name "
print(string.capitalize())
#title()
string="converts the lowercase to uppercase"
print(string.title())

#take a string it contains both upper and lower case,print the of vowels and consonants present in the string
name="valiva"
vowels = "aeiouAEIOU"
vowels_count = 0
consonants_count = 0
for char in name:
       if char.isalpha():
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
print("Vowels:", vowels_count)
print("Consonants:", consonants_count)
