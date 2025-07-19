name =input("What is your Full Name = ")
phone = input("What is your Phone Number = ")
#len() = length function used to calculate length of a string, for example
length = len(name)
print(f"Your name is {length} characters long including spaces")

# ".find" = it use to find an string or words or spaces in an input in ascending order whereas ".rfind" is also work same but in desending orders.
#example

result = name.find(" ")
print(f"Space in your name is in {result} position")

result1 = name.find("K" or "k")
print(f"K or k in your name is in {result1} position")

result2 = name.rfind("a")
print(f"A or a in your name is in {result2} position")

#.capitalize() = it use to capatalize the first letter of word
#Example
name = name.capitalize()
print(name)

#.upper() = it use to converts all words into uppercase
name = name.upper()
print(name)

#.lower() = it is used to convert all words into lowercase
#Example
name = name.lower()
print(name)

#.isdigit() = it is an boolean condition in which it conly return true when the input is only contain digits
name = name.isdigit()
print(name)

#.isalpha() = it returns an boolean condition it only return true when there is no space or number are in an input
name2 = "abhi"
r0 = name2.isalpha()
print(r0)
#.count() = it method use to count how many string in a function
name1 = "anubhav"
r = name1.count("a")
print(r)

#.replace() = this method is used to replace a word with another one
phone = phone.replace("-"," ")
print(phone)

#print(help(str)) = it use to understand all types of string methonds just print this command and see in terminal for all strinfs methods
print(help(str))
