long_statment = '''
    Print a paragraph with out \\n everywhere

    See another line
'''

create_dynamic_value_strings = "Mike"
print(f"My name is {create_dynamic_value_strings} which is {len(create_dynamic_value_strings)} chars long")

contains_string_check = "This contains some words"
print("words" in contains_string_check)
print("Mike" not in contains_string_check)

# must run in terminal as code runner runs in
# read only and switch boolean to True
is_using_commandline = False
if is_using_commandline:
    command_line_input = input("enter text: ")
    print(command_line_input)

see_type = "what am I?"
print(type(see_type))
if isinstance(see_type, str):
    print("It is a string")
else:
    print("Is not a string")

# ternary operator
message = "It is a string" if isinstance(see_type, str) else "Is not a string"
print(message)

is_break = False
for x in range(3):
    print(x)
    if is_break:
        print("for else block does not execute as break, breaks out of the loop")
        break
else:
    print("Done in for else block")
