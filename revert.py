def utf32_to_unicode(utf32_string):
    utf32_hex = utf32_string.replace(' ', '')
    # Remove leading zeros
    utf32_hex = utf32_hex.lstrip('0')
    return [f"U+{utf32_hex[i:i+8].upper()}" for i in range(0, len(utf32_hex), 8)]

def utf16_to_unicode(utf16_string):
    utf16_hex = utf16_string.replace(' ', '').upper()  # Convert to uppercase to normalize input
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



def decode_utf8(utf8_bytes):
    utf8_hex = utf8_bytes.replace(' ', '')
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

def bytes_to_unicode(bytes_str):
    # Converts a byte string to Unicode code points
    unicode_points = []
    for char in bytes_str:
        unicode_points.append(f"U+{ord(char):04X}")
    return unicode_points

def main():
    print("Choose encoding type of input string:")
    print("1. UTF-8")
    print("2. UTF-16")
    print("3. UTF-32")
    choice = input("Enter choice (1/2/3): ")

    input_string = input("Enter encoded string: ")

    if choice == '1':
        # Assuming the UTF-8 string is input as a regular string
        unicode_points = decode_utf8(input_string)
        # unicode_points = bytes_to_unicode(decoded_str)
    elif choice == '2':
        unicode_points = utf16_to_unicode(input_string)
    elif choice == '3':
        unicode_points = utf32_to_unicode(input_string)
    else:
        print("Invalid choice.")

    print("Unicode points:")
    print(", ".join(unicode_points))

    main()

if __name__ == "__main__":
    main()
