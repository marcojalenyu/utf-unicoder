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
    # If the input is empty, it's not a valid hexadecimal number
    if input_str == "":
        return False
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
    # Remove leading zeros (unless all 0)
    if all(char == '0' for char in utf32_str):
        utf32_hex = '0'
    else:
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
    # Convert to uppercase to normalize input
    utf16_hex = utf16_str.replace(' ', '').upper()  
    # Remove leading zeros
    utf16_hex = utf16_hex.lstrip('0')
    # Range is 0x0000 to 0xFFFF
    if (int(utf16_hex, 16) <= 0xFFFF):
        return [f"U+{utf16_hex.upper()}"]
    # If not, check if high surrogate and low surrogate are within range
    elif (0xD800 <= int(utf16_hex[0:4], 16) <= 0xDBFF) and (0xDC00 <= int(utf16_hex[4:8], 16) <= 0xDFFF):
        # Deduct 0xD800 from the high surrogate and 0xDC00 from the low surrogate
        high_val = int(utf16_hex[0:4], 16) - 0xD800
        low_val = int(utf16_hex[4:8], 16) - 0xDC00
        # Combine the high and low surrogates
        combined = (high_val << 10 | low_val) + 0x10000
        return [f"U+{hex(combined)[2:].upper()}"]
    return []

""""
    This function takes a UTF-8 string and returns the Unicode code point.

    Args:   
        utf8_str: A string of hexadecimal values separated by spaces.
    
    Returns:
        A list of Unicode code points in the format "U+XXXXXXXX".
"""
def utf8_to_unicode(utf8_str):
    # Initialize the list of Unicode points
    unicode_points = []
    utf8_bin = bin(int(utf8_str, 16))[2:].zfill(len(utf8_str) * 4)
    # If utf8_bin is only 1 nibble long, extend it to 8 bits
    if len(utf8_bin) == 4:
        utf8_bin = utf8_bin.zfill(8)

    # Get the length of the binary string
    utf8_bin_len = len(utf8_bin)

    # If value is 0xxxxxxx, means it is a 1-byte code point
    if utf8_bin[0] == '0' and utf8_bin_len == 8:
        return [f"U+{hex(int(utf8_bin, 2))[2:].upper()}"]
    
    # If value is 110xxxxx 10xxxxxx, it is a 2-byte code point
    elif utf8_bin[0:3] == '110' and utf8_bin[8:10] == '10' and utf8_bin_len == 16:
        # Remove 110 and 10 from the binary string and append to the list
        unicode_points.append(utf8_bin[3:8])
        unicode_points.append(utf8_bin[10:16])
        # Convert to hexadecimal and return
        return [f"U+{hex(int(''.join(unicode_points), 2))[2:].upper()}"]
    
    # If value is 1110xxxx 10xxxxxx 10xxxxxx, it is a 3-byte code point
    elif utf8_bin[0:4] == '1110' and utf8_bin[8:10] == '10' and utf8_bin[16:18] == '10' and utf8_bin_len == 24:
        # Remove 1110, 10, and 10 from the binary string and append to the list
        unicode_points.append(utf8_bin[4:8])
        unicode_points.append(utf8_bin[10:16])
        unicode_points.append(utf8_bin[18:24])
        # Convert to hexadecimal and return
        return [f"U+{hex(int(''.join(unicode_points), 2))[2:].upper()}"]
    
    # If value is 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx, it is a 4-byte code point
    elif utf8_bin[0:5] == '11110' and utf8_bin[8:10] == '10' and utf8_bin[16:18] == '10' and utf8_bin[24:26] == '10' and utf8_bin_len == 32:
        # Remove 11110, 10, 10, and 10 from the binary string and append to the list
        unicode_points.append(utf8_bin[5:8])
        unicode_points.append(utf8_bin[10:16])
        unicode_points.append(utf8_bin[18:24])
        unicode_points.append(utf8_bin[26:32])
        # Convert to hexadecimal and return
        return [f"U+{hex(int(''.join(unicode_points), 2))[2:].upper()}"]
    
    # If the input is not a valid UTF-8 string, return an empty list
    return unicode_points

def check_and_revert_utf8(input_str):
    # Remove all spaces from the input string and convert to uppercase
    input_str = input_str.replace(' ', '').upper()
    # Checks if the input is a valid hexadecimal number
    isHex = is_valid_hex(input_str)

    # If the input is a valid hexadecimal number, convert it to Unicode
    if isHex:
        unicode_points = utf8_to_unicode(input_str)
        # If the Unicode points list is empty, the input is invalid
        if(len(unicode_points) == 0):
            return "Invalid UTF: Out of range.\n"
        else:
            return ", ".join(unicode_points) + "\n"
    else:
        return "Invalid UTF: Either out of range or contains invalid digits.\n"

def check_and_revert_utf16(input_str):
    # Remove all spaces from the input string and convert to uppercase
    input_str = input_str.replace(' ', '').upper()
    # Checks if the input is a valid hexadecimal number
    isHex = is_valid_hex(input_str)

    # If the input is a valid hexadecimal number, convert it to Unicode
    if isHex:
        unicode_points = utf16_to_unicode(input_str)
        # If the Unicode points list is empty, the input is invalid
        if(len(unicode_points) == 0):
            return "Invalid UTF: Out of range.\n"
        else:
            return ", ".join(unicode_points) + "\n"
    else:
        return "Invalid UTF: Either out of range or contains invalid digits.\n"
    
def check_and_revert_utf32(input_str):
    # Remove all spaces from the input string and convert to uppercase
    input_str = input_str.replace(' ', '').upper()
    # Checks if the input is a valid hexadecimal number
    isHex = is_valid_hex(input_str)

    # If the input is a valid hexadecimal number, convert it to Unicode
    if isHex:
        unicode_points = utf32_to_unicode(input_str)
        # If the Unicode points list is empty, the input is invalid
        if(len(unicode_points) == 0):
            return "Invalid UTF: Out of range.\n"
        else:
            return ", ".join(unicode_points) + "\n"
    else:
        return "Invalid UTF: Either out of range or contains invalid digits.\n"

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
