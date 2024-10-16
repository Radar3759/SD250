#Eg_1
def my_new_function():
    print("Printing Hello from inside the function")
my_new_function();

# add three new functions print messages re: cybersecurity
def passwords():
    print("Use strong passwords and turn on multi-factor authentication")
passwords();

def holidays():
    print("Holiday shopping season is an opportunity to take advantage of unsuspecting shoppers")
holidays();

def message():
    print("Cybersecurity is important for all users")
message();

# Eg.2 add three more functions subtract/multiply/divide
def addNumbers(a, b):
    return a + b
spam = addNumbers(2, 40)
print(spam)

def subNumbers(a, b):
    return a - b
minus = subNumbers(20, 5)
print(minus)

def multNumbers(a, b):
    return a * b
multi = multNumbers(5, 10)
print(multi)

def divNumbers(a, b):
    return a / b
div = divNumbers(60, 12)
print(div)

# Eg 3. change the passwords, add one or two selections to access the correct password
print("Enter your password")
typedPassword = input()
if typedPassword == 'swordfish':
    print('Access Granted')
elif typedPassword == 'mary':
    print('Hint: the password is a fish.')
elif typedPassword == '12345':
    print("That is a really obvious password.")
elif typedPassword == 'gold':
    print('Not that type of fish.')    
elif typedPassword == 'sticks':
    print('Not a fish for eating.')
elif typedPassword == 'rock lobster':
    print("Oh, so close!")
else:
    print('Access Denied')            
print('Done')    