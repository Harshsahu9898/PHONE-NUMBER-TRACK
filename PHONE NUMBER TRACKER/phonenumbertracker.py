import phonenumbers
from phonenumbers import geocoder
phone_number1 =  phonenumbers.parse("+919692013830")
phone_number2 =  phonenumbers.parse("+916200682942")

print("\n Phone numbers location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));