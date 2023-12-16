import re
import cv2
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# 1. Load the image using OpenCV
business_card = 'C:/Users/obeyk/Documents/GitHub/OCR-ContactSync/business_card.png'

image = cv2.imread(business_card)

# 2. Preprocess the image (resize, convert to grayscale, etc.)

# Resize the image
resized_image = cv2.resize(image, (800, 600))  # Adjust the dimensions as needed

# Convert the resized image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Use Tesseract OCR to extract text
extracted_text = pytesseract.image_to_string(image)

# Print
#print(list(extracted_text))
#print(len(extracted_text))

# Define regular expressions for phone number and email
phone_regex = r'\b(?:\d{3}[-.]?)?\d{3}[-.]?\d{4}\b'
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Find phone numbers in the extracted text
phone_numbers = re.findall(phone_regex, extracted_text)

# Find email addresses in the extracted text
emails = re.findall(email_regex, extracted_text)

print(phone_numbers)
print(emails)
