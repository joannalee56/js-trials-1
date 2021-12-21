"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)

output_all_items([1, 'hello', True])

def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

print(get_all_evens([7, 8, 10, 1, 2, 2]))

def get_odd_indices(items):
    result = []

    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i])
    
    return result

print(get_odd_indices([1, 'hello', True, 500]))


def print_as_numbered_list(items):
    number = 1
    for item in items:
        print(f" {number}. {item}")
        number +=1
        
print_as_numbered_list([1, 'hello', True])

def get_range(start, stop):
    num = []

    for i in range(start, stop):
        num.append(i)
    return num

print(get_range(0, 5))

def censor_vowels(word):
    chars = []
    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else: 
            chars.append(letter)
    return "".join(chars)

print(censor_vowels('hello world'))

def snake_to_camel(string):
    camelcase = []

    for word in string.split("_"):
        camelcase.append(word[0].upper()+word[1:])

    return "".join(camelcase)

print(snake_to_camel('hello_world'))

def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(words):
            longest = len(word)
    
    return longest
    
print(longest_word_length(['jellyfish', 'zebra']))

def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result)-1]:
            result.append(char)
    
    return "".join(result)

print(truncate('hi***!!!! wooow'))

def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
    return parens == 0

print(has_balanced_parens('(Oh no!)('))
print(has_balanced_parens('()'))
print(has_balanced_parens('((This) (is) (good))'))

def compress(string):
    compressed = []
    currentchar = ""
    charcount = 0

    for char in string:
        if char != currentchar:
            compressed.append(currentchar)
            if charcount > 1:
                compressed.append(str(charcount))
            currentchar = char
            charcount = 0
        charcount += 1

    compressed.append(currentchar)
    if charcount > 1:
        compressed.append(str(charcount))
        
    return "".join(compressed)
    
print(compress('Hello, world! Cows go moooo...'))