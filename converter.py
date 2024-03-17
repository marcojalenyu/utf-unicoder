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
    pass

def convert_to_utf32(unicode):
    utf32_string = ""

    # zero extension
    for i in range(0, 8 - len(unicode)):
        utf32_string += '0'
    
    utf32_string += unicode
    return utf32_string


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
        print("UTF-16:", utf16)
        print("UTF-32:", ' '.join(utf32[i:i+2] for i in range(0, len(utf32), 2)))
    else: # invalid input
        print("Sorry! Invalid Input.")


if __name__ == "__main__":
    main()