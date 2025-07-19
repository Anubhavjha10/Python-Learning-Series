#formate specifier = {:flags} formate a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive values
# := place sign to leftmost position
# : insert a space before positive numbers
# :, = comma seperator

#Examples
#1
num = 3.1412
print(f"num is {num:.2f}")
#2
num2 = 895.23569
print(f"num2 is {num2:10}")
#3
num3 = 45.325
print(f"num3 is {num3:010}")
#4
num4 = 95.239
print(f"num4 is {num4:< 10}")
#5
num5 = 456.321
print(f"num5 is {num5:> 10}")
#6
num6 = 9.29
print(f"num6 is {num6:^ 10}")
#7
num7 = 5949.2
print(f"num7 is {num7:+}")
#8
num8 = 785.32
print(f"num8 is {num8:= 10}")
#9
num9 = 95.239
print(f"num9 is {num9: 10}")
#10
num10 = 9999.99
print(f"num10 is {num10:,}")
