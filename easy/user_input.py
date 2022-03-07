# Take two inputs from user
# One integer number
# other float number
# display multiply result
 
# User Input to Number
int_text = input("Give me a integer number : ")
int_num = int(int_text)
float_text = input("Give me a float number : ")
float_num = float(float_text)
result_input = int_num * float_num
print("Your Input Result Is: ", result_input)

# shortcut
int_num = int(input("Give me a integer number : "))
float_num = float(input("Give me a float number : "))
result = int_num * float_num
print("Your short Result is : ", result)