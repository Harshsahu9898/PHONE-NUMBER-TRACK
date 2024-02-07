# Phone Number Geocoding with Python

This Python script demonstrates how to use the `phonenumbers` library to parse and geocode phone numbers to determine their associated locations. Geocoding is the process of converting a description of a location into geographic coordinates. 

## Requirements

- Python 3.x
- `phonenumbers` library (install via `pip install phonenumbers`)

## Usage

1. Install the required libraries if you haven't already:

    ```
    pip install phonenumbers
    ```

2. Run the Python script `phone_geocoder.py`.

    ```
    python phone_geocoder.py
    ```

3. The script will output the location information for the provided phone numbers.

## Notes

- The `phonenumbers` library provides functionality to parse and format phone numbers in various formats.
- The `geocoder` module attempts to determine the geographic location associated with a phone number. However, this might not always be accurate, especially for mobile or VoIP numbers.
- Ensure that the phone numbers are provided in international format (e.g., "+1234567890").
- The script is currently set to print the location information in English. You can modify the language parameter ("en") if you prefer a different language.

