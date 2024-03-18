def utf32_to_unicode(utf32_string):
    utf32_hex = utf32_string.replace(' ', '')
    return [f"U+{utf32_hex[i:i+8]}" for i in range(0, len(utf32_hex), 8)]

def utf16_to_unicode(utf16_string):
    utf16_hex = utf16_string.replace(' ', '')
    unicode_points = []
    i = 0
    while i < len(utf16_hex):
        hex_val = utf16_hex[i:i+4]
        if len(hex_val) < 4:
            break
        high_val = int(hex_val, 16)
        if 0xD800 <= high_val <= 0xDBFF:
            low_val = int(utf16_hex[i+4:i+8], 16)
            combined = ((high_val - 0xD800) << 10 | (low_val - 0xDC00)) + 0x10000
            unicode_points.append(f"U+{hex(combined)[2:].upper()}")
            i += 8
            continue
        unicode_points.append(f"U+{hex(high_val)[2:].upper()}")
        i += 4
    return unicode_points

def decode_utf8(utf8_bytes):
    pass

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
        decoded_str = decode_utf8(input_string.encode('utf-8'))
        unicode_points = bytes_to_unicode(decoded_str)
    elif choice == '2':
        unicode_points = utf16_to_unicode(input_string)
    elif choice == '3':
        unicode_points = utf32_to_unicode(input_string)
    else:
        print("Invalid choice.")
        return

    print("Unicode points:")
    print(", ".join(unicode_points))

if __name__ == "__main__":
    main()
