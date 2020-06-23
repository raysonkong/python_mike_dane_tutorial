# 2:07:18
# Dictionaries

# pickup at 2:13:56

monthConversions = {
    "Jan": "January",
    "Feb": "Feburary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "Sept",
    "Oct": "October",
    "Nov": 'November',
    "Dec": "December"
}

print(monthConversions["Nov"])
print(monthConversions.get("lu", "Not a valid key"))