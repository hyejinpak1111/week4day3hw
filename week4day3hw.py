# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, 
# continue reducing in this way until a single-digit number is produced. 
# The input will be a non-negative integer.

def digital_root(n): # O(n)
    while n > 9:
        n = sum(int(digit) for digit in str(n)) # O(1)
    return n

# You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. 
# It must return the display text as shown in the examples

def likes(names): # O(log(n))
    n = len(names)

    if not names:
        return 'no one likes this'
    if n == 1: # O(1)
        return f'{names[0]} likes this'
    if n == 2: # O(1)
        return f'{names[0]} and {naems[1]} like this'
    if n == 3: # O(1)
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    
    return f'{names[0]}, {names[1]} and {n - 2} others like this'


# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, 
# neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

def disemvowel(string_): # O(n)
    vowels ='aeiouAEIOU'

    new_string = [] # O(n)
    for char in string_:
        if char not in vowels:
            new_string.append(char)
    return ''.join(new_string)