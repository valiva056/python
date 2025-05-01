#perfrom basic mathematical operation using def function
#addition
n=13,34
def add(first,second):
   print(first+second)
add(13,34)
#subtraction
def sub(first,second):
  print(first-second)
sub(13,34)  
#multiplication
def mul(first,second):
  print(first*second)
mul(13,34)  
#power
def power(first,second):
  print(first**second)
power(13,34)  
#division module
def divmod(first,second):
  print(first%second)
power(13,34)
#floor division
def floordiv(first,second):
  print(first//second)
floordiv(13,34) 
#division
def div(first,second):
  print(first//second)
div(13,34) 
 
#perform basic mathematical opearation using lambda function
#addition
add_lambda=lambda a, b:a+b
result_lambda=add_lambda(2,6)
print(result_lambda)
#subtraction
sub_lambda=lambda a,b:a-b
result_lambda=sub_lambda(3,8)
print(result_lambda)
#multiplication
mul_lambda=lambda a, b:a* b
result_lambda=mul_lambda(4,8)
print(result_lambda)
#division
div_lambda=lambda a, b:a/ b
result_lambda=div_lambda(4,8)
print(result_lambda)
#floor division
floordiv_lambda=lambda a, b:a//b
result_lambda=floordiv_lambda(4,8)
print(result_lambda)
#power
power_lambda=lambda a, b:a**b
result_lambda=power_lambda(4,8)
print(result_lambda)
#division module
divmod_lambda=lambda a, b:a//b
result_lambda=divmod_lambda(4,8)
print(result_lambda)
