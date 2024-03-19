"""
    This function checks if the input is an 1-8 digit hexadecimal number.

    Args:
        input_str: A string of hexadecimal values.
    
    Returns:
        True if the input is a valid hexadecimal number, False otherwise.
"""
def is_valid_hex(input_str):
    # Define valid hexadecimal characters
    hex_chars = "0123456789ABCDEF"
    # If length is greater than 8 (excluding spaces), it's not a valid hexadecimal number
    if len(input_str) > 8:
        return False
    # If the string contains non-hexadecimal characters, it's not a valid hexadecimal number
    return all(char in hex_chars for char in input_str)

"""
    This function takes a UTF-32 string and returns the Unicode code point.

    Args:
        utf32_str: A string of hexadecimal values separated by spaces.

    Returns:
        A list of Unicode code points in the format "U+XXXXXXXX".
"""
def utf32_to_unicode(utf32_str):
    # Remove leading zeros
    utf32_hex = utf32_str.lstrip('0')
    # Check if UTF-32 is out of range
    if int(utf32_hex, 16) > 0x10FFFF:
        return []
    # Return as is if it's within range
    return [f"U+{utf32_hex[i:i+8].upper()}" for i in range(0, len(utf32_hex), 8)]

"""
    This function takes a UTF-16 string and returns the Unicode code point.

    Args:
        utf16_str: A string of hexadecimal values separated by spaces.
    
    Returns:
        A list of Unicode code points in the format "U+XXXXXXXX".
"""
def utf16_to_unicode(utf16_str):
    utf16_hex = utf16_str.replace(' ', '').upper()  # Convert to uppercase to normalize input
    unicode_points = []
    i = 0
    while i < len(utf16_hex):
        # Extract 4 characters (if available), padding with leading zeros if less than 4 characters
        hex_val = utf16_hex[i:i+4].zfill(4)
        high_val = int(hex_val, 16)
        if 0xD800 <= high_val <= 0xDBFF:
            # This is a high surrogate; look ahead for the low surrogate
            low_val_hex = utf16_hex[i+4:i+8].zfill(4)  # Pad low value hex if it's less than 4 nibbles
            low_val = int(low_val_hex, 16)
            combined = ((high_val - 0xD800) << 10 | (low_val - 0xDC00)) + 0x10000
            unicode_points.append(f"U+{hex(combined)[2:].upper()}")
            i += 8  # Move past the surrogate pair
        else:
            # No need for surrogate handling; direct representation
            unicode_points.append(f"U+{hex_val.upper()}")
            i += 4  # Move to the next set of characters
    return unicode_points

""""
    This function takes a UTF-8 string and returns the Unicode code point.

    Args:   
        utf8_str: A string of hexadecimal values separated by spaces.
    
    Returns:
        A list of Unicode code points in the format "U+XXXXXXXX".
"""
def utf8_to_unicode(utf8_str):
    utf8_hex = utf8_str.replace(' ', '')
    n = len(utf8_hex)
    unicode_points = []
    # Convert to binary
    binary_str = bin(int(utf8_hex, 16))[2:].zfill(n * 4)
    # Debug
    # print(binary_str)    
    # If value is over 1FFFFF, it's not valid UTF-8
    if n > 8 or binary_str[0:5] == '11111':
        return []
    # If value is 0xxxxxxx, it's a single byte character
    elif binary_str[0] == '0':
        # Remove the '0b' prefix
        return [f"U+{hex(int(binary_str, 2))[2:].upper()}"]
    # If value is 110xxxxx 10xxxxxx, it's a two byte character
    elif binary_str[0:3] == '110' and binary_str[8:10] == '10':
        # Remove 110 and 10 from the binary string
        unicode_points.append(binary_str[3:8])
        unicode_points.append(binary_str[10:16])
        # Convert to hexadecimal and return
        return [f"U+{hex(int(''.join(unicode_points), 2))[2:].upper()}"]
    # If value is 0800 to FFFF, it's a three byte character
    elif binary_str[0:4] == '1110' and binary_str[8:10] == '10':
        unicode_points.append(binary_str[4:8])
        unicode_points.append(binary_str[10:16])
        unicode_points.append(binary_str[18:24])
        return [f"U+{hex(int(''.join(unicode_points), 2))[2:].upper()}"]
    # If value is 10000 to 1FFFFF, it's a four byte character
    elif binary_str[0:5] == '11110' and binary_str[8:10] == '10':
        byte1 = binary_str[5:8]
        byte2 = binary_str[10:16]
        byte3 = binary_str[18:24]
        byte4 = binary_str[26:32]
        unicode_points.append(byte1)
        unicode_points.append(byte2)
        unicode_points.append(byte3)
        unicode_points.append(byte4)
        return [f"U+{hex(int(''.join(unicode_points), 2))[2:].upper()}"]
    print("Invalid UTF-8 string.")
    unicode_points = []
    return unicode_points

"""
    Main function to run the program.
"""
def main():    
    # Print the menu
    print("Choose encoding type of input string:")
    print("1. UTF-8 to Unicode")
    print("2. UTF-16 to Unicode")
    print("3. UTF-32 to Unicode")
    print("4. Exit")

    # Get UTF conversion choice
    choice = input("Enter choice (1/2/3/4): ")
    # Exit if the user chooses 4 or an invalid choice
    if choice == '4':
        exit()
    elif choice not in ['1', '2', '3']:
        print("Invalid choice.\n")
        main()
    
    # Get the input string
    input_string = input("Enter encoded string: ")
    # Remove all spaces from the input string and convert to uppercase
    input_string = input_string.replace(' ', '').upper()
    # Checks if the input is a valid hexadecimal number
    isHex = is_valid_hex(input_string)

    # If the input is a valid hexadecimal number, convert it to Unicode
    if isHex:
        # Convert the input string to Unicode based on the user's choice
        if choice == '1':
            unicode_points = utf8_to_unicode(input_string)
        elif choice == '2':
            unicode_points = utf16_to_unicode(input_string)
        elif choice == '3':
            unicode_points = utf32_to_unicode(input_string)
        
        # If the Unicode points list is empty, the input is invalid
        if(len(unicode_points) == 0):
            print("Invalid UTF: Out of range.\n")
        else:
            print("Unicode points:")
            print(", ".join(unicode_points) + "\n")
    else:
        print("Invalid UTF: Either out of range or contains invalid digits.\n")

    # Loops back to the main menu
    main()

if __name__ == "__main__":
    main()
