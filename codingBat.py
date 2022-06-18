# # Warm ups


# Monkey Trouble
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False

def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False

monkey_trouble = lambda a_smile, b_smile : True if a_smile == b_smile else False

# The Sum or double
def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b

def sum_double(a, b):
    return ((a+b) *2) if a == b else (a+b)

sum_double = lambda a, b : ((a+b) * 2) if a == b else (a+b)

# Difference
    # you can add "abs" after return to always get absolute value
def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2
# Alternate
# you can add "abs" after return to always get absolute value
def diff21(n):
    if n <= 21:
        return abs(21 - n)
    else:
        return abs((21 - n) * 2)
# Alternate
def diff21(n):
    return (21 - n) if n <= 21 else ((n - 21) * 2)
# Alternate
diff21 = lambda n : (21 - n) if n <= 21 else ((n - 21) * 2)


# Parrot Talking
def parrot_trouble(talking, hour):
    if (talking and (hour < 7 or hour > 20)): 
        return True
    else:
        return False
# Alternate
def parrot_trouble(talking, hour):
    return True if (talking and (hour < 7 or hour > 20)) else False
# ALternate
parrot_trouble = lambda talking, hour : True if talking and (hour < 7 or hour > 20) else False

# Make 10
def makes10(a, b):
    if (a + b) == 10 or (a == 10) or (b == 10):
        return True
    else:
        return False
# Alternate
def makes10(a,b):
    return True if (a + b) == 10 or (a == 10) or (b == 10) else False
# Alternate
makes10 = lambda a,b : True if (a + b) == 10 or (a == 10) or (b == 10) else False

# Near Hundred
def near_hundred(n):
    if (n >= 90 and n <= 110) or (n >= 190 and n <= 210):
        return True
    else:
        return False
# Alternate
def near_hundred(n):
    return True if (n >= 90 and n <= 110) or (n >= 190 and n <= 210) else False
# Alternate
near_hundred = lambda n : True if (n >= 90 and n <= 110) or (n >= 190 and n <= 210) else False





# # Lists 1

# First Last 6 
def first_last6(nums):
    if nums[0] == int(6) or nums[len(nums)-1] == int(6):
        return True
    else:
        return False

# Sum 2
def sum2(nums):
    sum = ((nums[0]) + (nums[1]))
    if(nums >= [1]):
        return sum
    else:
        return [0]

#Middle way
def middle_way(a, b):
    li = []
    li.append(a[1])
    li.append(b[1])
    return li

# Make Ends
def make_ends(nums):
    li = []
    li.append(nums[0])
    li.append(nums[-1])
    return li

# Optional way to get to the end
#   endOfList = nums[lens(nums)-1]

# Has 23
def has23(nums):
    firstNum = nums[0]
    secondNum = nums[1]
  
    if((firstNum == 2 or firstNum == 3) or (secondNum == 2 or secondNum == 3)):
        return True
    else:
        return False
# Alternate
def has23(nums):
    return True if((nums[0] == 2 or nums[0] == 3) or (nums[1] == 2 or nums[1] == 3)) else False
# Alternate
has23 = lambda nums : True if((nums[0] == 2 or nums[0] == 3) or (nums[1] == 2 or nums[1] == 3)) else False





# # Logic 1


# Cigar_Party
def cigar_party(cigars, is_weekend):
    if is_weekend:
        return (cigars >= 40)
    else:
        return (cigars >= 40 and cigars <= 60)
# Alternate
def cigar_party(cigars, is_weekend):
    if is_weekend:
        return (cigars >= 40)
    return (cigars >= 40 and cigars <= 60)
# Alternate 2
def cigar_party(cigars, is_weekend):
    if(not is_weekend and (cigars >= 40 and cigars <= 60)):
        return True
    elif( is_weekend and (cigars >= 40)):
        return True
    else:
        return False

# Fashion Date

def date_fashion(you, date):
    if (you <= 2 or date <= 2):
        return 0
    elif (you >= 8 or date >= 8):
        return 2
    else:
        return 1

# Squirrel Play

def squirrel_play(temp, is_summer):
    if((temp >= 60 and temp <= 100) and is_summer):
        return True
    if((temp >= 60 and temp <= 90) and not is_summer):
        return True
    return False

# Caught Speeding

def caught_speeding(speed, is_birthday):
    if (speed <= 60 or (speed <=65 and is_birthday)):
        return 0
    elif (speed >= 61 and speed <= 80 or (speed >=66 and speed <= 85 and is_birthday)):
        return 1
    else:
        return 2

# Sort Sum

def sorta_sum(a, b):
    if 10 <= (a + b) < 20:
        return 20
    else:
        return a + b

# Alarm Clock

def alarm_clock(day, vacation):
    if not vacation:
        if 1 <= day <= 5:
            return "7:00"
        return "10:00"
    
    if 1 <= day <= 5:
        return "10:00"
    return "off"

# Love 6

def love6(a, b):
    if (a == 6 or b == 6 or (a + b) == 6 or (abs(a - b) == 6)):
        return True
    else:
        return False
# Alternate
def love6(a, b):
    if (a == 6 or b == 6 or (a + b) == 6 or (abs(a - b) == 6)):
        return True
    return False
# Alternate
def love6(a, b):
    return (a == 6 or b == 6 or (a + b) == 6 or (abs(a - b) == 6))
# Alternate
love6 = lambda a, b : (a == 6 or b == 6 or (a + b) == 6 or (abs(a - b) == 6))

# Outside mode

def in1to10(n, outside_mode):
    if not outside_mode:
        return n in range(1, 11)
    return n <= 1 or n >= 10
        
# Near Ten

def near_ten(num):
    if 0 <= (num % 10) <= 2 or 8 <= (num % 10) <= 10:
        return True
    else:
        return False
# Alternate
def near_ten(num):
    return 0 <= (num % 10) <= 2 or 8 <= (num % 10 <= 10
# Alternate
near_ten = lambda num : 0 <= (num % 10) <= 2 or 8 <= (num % 10) <= 10





# # Logic 2

# Make Bricks
def make_bricks(small, big, goal):
    if (goal > big*5 + small):
        return False
    if (goal % 5 > small):
        return False
    return True
# Alternate
def make_bricks(small, big, goal):
    if (goal > big*5 + small) or (goal % 5 > small):
        return False
    return True

# Lone Sum
def lone_sum(a, b, c):
    if (a == b) and (a == c):
        return 0
    elif (a == b):
        return c
    elif (a == c):
        return b
    elif (b == c):
        return a
    else:
        return a + b + c

# Lucky Sum
def lucky_sum(a, b, c):
    if (a == 13):
        return 0
    elif (b == 13):
        return a
    elif (c == 13):
        return a + b
    else:
        return a + b + c

# No Teen Sum
def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    else:
        return n
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

# Round Sum
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)
  
def round10(num):
    if num % 10 >= 5:
        return num + 10 - (num % 10)
    return num - (num % 10)

# Close Far
def close_far(a, b, c):
    close = abs(a - b) <= 1 and abs(b - c) >= 2 and abs(a - c) >= 2
    far = abs(a - c) <=1 and abs(a - b) >= 2 and abs(b - c) >= 2
    return far or close

# Make Chocolate
def make_chocolate(small, big, goal):
    maxBig = goal / 5
    if big >= maxBig:
        if small >= (goal - maxBig * 5):
            return goal - maxBig * 5
    if big < maxBig:
        if small >= (goal - big * 5):
            return goal - big * 5
    return -1
  




# # List -2

# Sum 13

def sum13(nums):
    if len(nums) == 0:
        return 0
 
    for i in range(0, len(nums)):
        if nums[i] == 13:
            nums[i] = 0
        if i+1 < len(nums): 
            nums[i+1] = 0
    return sum(nums)
# Alternative 
def sum13(nums):
    badNums = []
    if (13 not in nums):
        return sum(nums)
    if (len(nums) <= 2 and 13 in nums):
        return 0
    if (len(nums) <= 3 and nums.count(13) >= 2):
        return 0
    for i in range(len(nums)):
        if (nums[i-1] == 13):
            badNums.append(nums[i-1])
            if(i !=0):
                badNums.append(nums[i])
    return abs(sum(badNums) - sum(nums))





# # Strings 1

# Hello Name

def hello_name(name):
    return "Hello " + name + "!"

# Make abba

def make_abba(a, b):
    return a + b + b + a

# Make Tags

def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

# Make out word

def make_out_word(out, word):
    return out[:2] + word + out[2:] # the colon breaks out the "out" and splits it up however directed

# Extra end

def extra_end(str):
    return str[-2:] *3

# First two

def first_two(str):
    if str == 0:
        return "yields the empty string"
    if str == [0]:
        return []
    return str[:2]

# First Half

def first_half(str):
    return str[:len(str) / 2]

# Without end

def without_end(str):
    return str[1:-1]

# Combo strings

def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    elif len(b) > len(a):
        return a + b + a
# Alternate
def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    return a + b + a

# Non Start

def non_start(a, b):
    return a[1:] + b[1:]

# Left 2

def left2(str):
    return str[2:] + str[:2]





# # Strings 2

# Double Char

def double_char(str):
    new = ""
    for char in str:
        new += char * 2
    return new


# Count Hi

def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == "hi":
            count += 1
    return count
# Alternate
def count_hi(str):
    sum = 0
  ## Loop to length-1 and access index i and i+1
  ## in the loop.
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
            sum = sum + 1
    return sum

# Cat and Dog

def cat_dog(str):
    cat_count = 0
    dog_count = 0
    for i in range(len(str)-2):
        if str[i:i+3] == "cat":
            cat_count = cat_count + 1
        if str[i:i+3] == "dog":
            dog_count = dog_count + 1
    return cat_count == dog_count


# Code count

def count_code(str):
    code = 0
    for i in range(len(str)-3):
        if str[i:i+2] == "co" and str[i+3] == "e":
            code = code + 1
    return code

# End Other

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if a.endswith(b) or b.endswith(a):
        return True
    else:
        return False
# Alternate
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return (b.endswith(a) or a.endswith(b))

# XYZ there

def xyz_there(str):
    for i in range(len(str)):
        if str[i] != "." and str[i+1:i+4] == "xyz":
            return True
    if str[0:3] == "xyz":
        return True
    return False



