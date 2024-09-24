#takes a name as input
name = input("\nWhat is your name? " );
#prints name
print("Hi, " + name + "\n")
#takes a breakfast as input
breakfast = input("What is your favorite breakfast? ")
#prints name and type of breakfast
print(name + ", your favorite breakfast is: " + breakfast + "\n")

# declare vars
x = 3;
y = 5;
z = x * y;
p = x - y;
w = z - p;
# makes result of z a string
zString = str(z);
#makes result of p a string
pString = str(p)
wString = str(w)
# if else statements
if x > y:
    print("x is greater than y\n")
else:
    print("y is greater than x\n")    
# if else statements
if (x + y) > 5:
    print("Greater than 5!\n")
else: 
    print("Less than 5!")

print (x * y)
print(p)
print("\nThe product of x and y is " + zString)
print("The difference of " + zString + " and " + pString + " is " + wString + "\n")
