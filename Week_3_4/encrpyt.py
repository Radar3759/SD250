# this program will encrypt an input string of lowercase letters and distance value single digit
plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - \
                    (ord('z') - ordvalue + 1)
    code += chr(cipherValue)    
print(code)
