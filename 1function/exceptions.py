try:
    file = open("lists.py")
    age = int(input("Age: "))
    math = 10 / age
except (ValueError, ZeroDivisionError):
    print("This is not a valid age")
else:
    print("prints if there are no exceptions")
finally:
    file.close()


#Default release resources
#If object has __enter__ and __exit__ methods you can auto release with "with"

try:
    file = open("lists.py")
except FileNotFoundError:
    print("file not found")
finally:
    file.close()

try:
    with open("lists.py") as file:
        print("Do something with file")
except FileNotFoundError:
    print("file not found")


#Normally better to just return None instead of making higher level fuctions handle exceptions
#It is much faster
#timeit is cool built in function to test performance difference of code

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age
