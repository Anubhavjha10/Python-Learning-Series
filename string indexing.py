#indexing = accessing of a sequence using [] (indexing operators)
#                       [start : end :step]

creditcard_number = "1234 5678 9874 5632"

print(creditcard_number[0]) #print a number using this location (start)
print(creditcard_number[0:9]) #print the number between 0 - 9 using [start : end]
print(creditcard_number[::3]) # print the number with the gap of 3 the first two coloums is empty to assume python that we start from 0 index to end of the number . (star : end : step)

#step meaning an gap