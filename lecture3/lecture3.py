print ("Hello World")

variable = 4
var2 = "string"
varcasting = int(3/4)

print (variable)
print (variable + 5)
print (3/4)
print (varcasting)

print (var2 + "  " + str(variable))

boolean = True
# print(boolean)

def isBoolean(value):
    if value:
        print("true")
    elif not value:
        print("false")
    else:
        print ("Shits broken doo")

isBoolean(boolean)

isBoolean(not boolean)
# if boolean:    print ("true")
# else:
#     print ("False")

dicofnumbers = {} #dictionary

listofNums = [1,2,"string",5,6,7] #list

print (listofNums)

for value in listofNums:
        print(value, end=" ")
        
for i in range(len(listofNums)):
    print(listofNums[i])