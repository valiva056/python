#Take a paragraph check the count of words, if count is more than 100, print valid ; else invalid
para="Paragraphs can contain many different kinds of information. A paragraph could contain a series of brief examples or a single long illustration of a general point. It might describe a place, character, or process; narrate a series of events; compare or contrast two or more things; classify items into categories; or describe causes and effects. Regardless of the kind of information they contain, all paragraphs share certain characteristics. One of the most important of these is a topic sentence."
word=para.split()
print(word)
if len(word)>100:
        print("valid")
else:
        print("invalid")   

#ake a input with both upper and lower cases characters count the no.of uppercases and lower cases without using any methods
string="valiVA"
lowercase_count=0
uppercase_count=0
for char in string:
        code=ord(char)
        if 97<=code<=122:
                lowercase_count+=1
        elif 65<=code<=90:
                uppercase_count+=1
print("lowercase letters",lowercase_count)
print("uppercase letters",uppercase_count)                        
