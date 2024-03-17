def is_valid_unicode(unicode):
    valid_chars = set('0123456789ABCDEF')
    min = 0x0000
    max = 0x10FFFF

    # check if value has valid characters
    if all(char.upper() in valid_chars for char in unicode):
        decimal_value = int(unicode, 16)

        if (decimal_value >= min) and (decimal_value <= max):
            return True
    return False

def convert_to_utf8(unicode):
    pass

def convert_to_utf16(unicode):
    subtracted_val = int(unicode, 16) - 0x10000
    binary_val = bin(subtracted_val)[2:].zfill(20) 

    # split to 10 bits each
    left = binary_val[0:10]
    right = binary_val[10:20]

    # add left with D800 and right with DC00
    final_left = hex(0xD800 + int(left, 2))
    final_right = hex(0xDC00 + int(right, 2))
    utf16_string = (final_left[2:] + final_right[2:]).upper()

    return utf16_string

def convert_to_utf32(unicode):
    return unicode.zfill(8)


def main():
    print("---------Unicode Converter---------")
    input_unicode = input("Input (Unicode): U+")

    if is_valid_unicode(input_unicode):
        input_unicode = input_unicode.upper()
        # convert
        utf8 = convert_to_utf8(input_unicode)
        utf16 = convert_to_utf16(input_unicode)
        utf32 = convert_to_utf32(input_unicode)

        # print outputs
        print("Outputs:")
        print("UTF-8:", utf8)
        print("UTF-16:", ' '.join(utf16[i:i+2] for i in range(0, len(utf16), 2)))
        print("UTF-32:", ' '.join(utf32[i:i+2] for i in range(0, len(utf32), 2)))
    else: # invalid input
        print("Sorry! Invalid Input.")


if __name__ == "__main__":
    main()