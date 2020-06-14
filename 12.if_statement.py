# If Statements 1:40:06

is_male = False
is_tall = False

if is_male and is_tall:  # try or
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:
    print("You are an alien")