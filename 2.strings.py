# 28:24

print("Giraffe\nAcademy")
print("Giraffe\"Academy") # print double quote literally
print("Girafee\Academy")

phrase = "Giraffe Academy"
print(phrase)

# concat
print(phrase + " is Cool")

# string function

print(phrase.upper())
print("hello world".islower())
print(len(phrase))


# access character
print(phrase[6])
print(phrase[len(phrase) - 1])
print(phrase[-1])

# find location of a particular character
print(phrase.index("A"))

# Replace
print(phrase.replace("Giraffe", "Elephant"));  # Elephant Academy
