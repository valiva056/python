#default parameter
def student_info(s_name,batch_name="37r",inst_name="1000 coder"):
    print(s_name+batch_name+inst_name)
student_info("valiva")
student_info("lavanya")
student_info("mahi")

#keyword parameter
def sample(b,a):
    print(a,b)
sample(a=4,b=2)

#positional arguments
def greet(name, greeting):
    print(f"{greeting}, {name}!")
greet("Aisha", "Hello")
greet("Ravi", "Good morning")


#combined posiitional arguments and keyword parameter
def sample(a,b,/,*,c,d):
    print(a+b+c+d)
sample(2,4,c=5,d=7)
 
#arbitrary arguments 
def sample(**kid):
    print("his last name is" + kid["lname"])
sample(fname="mark",lname="valiva") 

#return function
def sample():
    print("hello world")
    return ("execution completed")
    print(sample())

#lambda function
f_class=lambda x:"hello"+x
print(f_class("valiva"))    

#Research about combining positional and keyword parameters
Keyword-Only Arguments:
The * symbol in a function's parameter list indicates that all parameters after it must be passed as keyword arguments.
This means you must use their names to pass them, and you cannot pass them positionally.
Positional-Only Arguments
The / symbol in a function's parameter list indicates that all parameters before it must be passed as positional arguments.
This means you cannot use their names to pass them as keyword arguments.
#Research on pass by value and pass by reference
Pass by Value vs. Pass by Reference (Simple Explanation)
When passing variables to a function, there are two ways a language can handle it:
Pass by Value – The function gets a copy of the variable. Changes inside the function do not affect the original variable.
Pass by Reference – The function gets a reference to the original variable. Changes inside the function affect the original variable

