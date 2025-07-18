# Even or Odd
def even_or_odd(number):
    if (number % 2 == 0):
        return("Even")
    else:
        return("Odd")
    
    
# Convert a Number to a String
def number_to_string(num):
    return str(num)


# Remove String Spaces
def no_space(x):
    return x.replace(" ", "")


# Vowel Count
def get_count(vowels):
    v_count = 0
    for v in vowels:
        if (v == "a" or v == "e" or v == "i" or v == "o" or v == "u"):
            v_count += 1
        else: continue
    return v_count