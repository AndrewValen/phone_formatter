"""
Andrew Valenzuela
CSC 101 
09/28/2025
Using the % and // operators to format a 10-digit phone number
"""
#asking users for their phone number
phone_number = int(input("Please enter your 10-digit phone number: "))

#gathering last 4 digits first 
line_number = phone_number % 1000
phone_number //= 10000 

prefix = phone_number % 1000
phone_number //= 1000

#first 3 digit separation
area_code = phone_number

#introduced an f string for variable manipulation
#introduced 04d to safeguard phone numbers that are shorter than 10-digits
#04d is a format spec. The 0 pads with zeros and the 4 returns a width of 4 characters
#d tells Python to treat the value as an int 
print(f"Formatted Phone Number: ({area_code}) {prefix}-{line_number:04d}")
