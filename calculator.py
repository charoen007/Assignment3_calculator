def calculator(first_var,secound_var, function_type):
    if function_type == 'a':        # if input is 'a' do add function
        return first_var + secound_var
    elif function_type == 's':      # if input is 's' do subtract function
        return first_var - secound_var
    elif function_type == 'm':      # if input is 'm' do multiply function
        return first_var * secound_var
    elif function_type == 'd':      # if input is 'd' do divide function
        return first_var / secound_var
    else:
        return "out of function"
#end------------------------------

#display results  calculator(2,5,'?')
num1 = float(input("Please input Num1: "))  # Convert input to float
num2 = float(input("Please input Num2: "))  # Convert input to float

print("add      :",calculator(num1,num2, 'a'))
print("subtract :",calculator(num1,num2, 's'))
print("multiply :",calculator(num1,num2, 'm'))
print("divide   :",calculator(num1,num2, 'd'))