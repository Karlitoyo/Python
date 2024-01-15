print("Good Morning, Karl", end = " ")

print("Brekkie?")

print("Good morning, Karl\nWould you like brekkie?")

#---------------------------------------------------------------------------------
a = "Good morning, Karl\nWould you like brekkie?"

print(len(a))

#---------------------------------------------------------------------------------
my_string = "Almost finished now folks"
my_upper = my_string.upper()
my_lower = my_string.lower()
print(f"Original: (my_string)")
print(f"Upper: {my_upper}")
print(f"Lower: {my_lower}")

#---------------------------------------------------------------------------------
text_with_spaces = "         Karl Timmins              "
text_without_spaces = text_with_spaces.strip()
print(text_without_spaces)

#---------------------------------------------------------------------------------
text_with_brackets = "(Karl)"
text_without_brackets = text_with_brackets.strip('(')
text_without_brackets = text_without_brackets.strip(')')
print(text_without_brackets)