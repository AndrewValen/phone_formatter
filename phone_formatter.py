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
