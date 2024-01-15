a = " Would you like brekkie?"

print("Good morning, Karl" + a )

#---------------------------------------------------------------------------------------
a = 5

b = 12

print("Good morning Karl, For breakfast, would you like {}?".format("Fruit"))

print("We have {} apples, bananas and a total of {} pieces available".format(a, b, a+b))

#----------------------------------------------------------------------------------------
a = "Good"
b= "Karl"
c= "morning"
print("Message is: {first} {third} {second}".format(first=a, second=c, third=b))

#----------------------------------------------------------------------------------------
Number = 12345
Divisor = 333
Result = Number/Divisor
print("Result of {} divided by {} is {}".format(Number, Divisor, Result))
print("Limiting to a float with 4 decimal places would give {r:1.4f}".format(r=Result))

#----------------------------------------------------------------------------------------
Number = 12345
Divisor = 333
Result = Number/Divisor
print(f"result of {Number} divided by {Divisor} is {Result}")