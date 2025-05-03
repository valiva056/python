string="this is simple paragraph with alphabets space and numbers like 1,2,3"
for ch in string:
    ascii_val=ord(ch)
    if((65<=ascii_val<=90) or (97<=ascii_val<=122) or ascii_val==32):
        print("valid")
    else:
        print("invalid")