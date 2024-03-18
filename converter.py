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
    bin_unicode = bin(int(unicode, 16))
    num_of_bits = len(bin_unicode) - 2
    str_unicode = str(bin_unicode)
    str_unicode = str_unicode[2:]
    res = ""
    bytes_req = 4 if num_of_bits > 16 else 3 if num_of_bits > 11 else 2 if num_of_bits > 7 else 1

    if bytes_req == 1:
        unicode = unicode[-2:]
        return unicode.zfill(2)
    else:
        for i in range(bytes_req - 1):
            res = "10" + str_unicode[-6:] + res
            str_unicode = str_unicode[:-6] 
        
        rem = 8 - bytes_req + 1
        res = "0" + str_unicode[-rem:] + res

        for i in range(bytes_req):
            res = "1" + res
    res = hex(int(res, 2)).upper()
    return res[2:]

def convert_to_utf16(unicode):
    if int(unicode, 16) <= 0xFFFF:
        unicode = unicode[-4:]
        return unicode.zfill(4)
    else:
        subtracted_val = int(unicode, 16) - 0x10000
        binary_val = bin(subtracted_val)[2:].zfill(20) 
        left, right = binary_val[0:10], binary_val[10:20]

        final_left = hex(0xD800 + int(left, 2))[2:].upper()
        final_right = hex(0xDC00 + int(right, 2))[2:].upper()

        return final_left + final_right

def convert_to_utf32(unicode):
    unicode = unicode[-8:]
    return unicode.zfill(8)

def main():
    print("---------Unicode Converter---------")
    input_unicode = input("Input (Unicode): U+")

    try:
        if is_valid_unicode(input_unicode):
            input_unicode = input_unicode.upper()

            utf8 = convert_to_utf8(input_unicode)
            utf16 = convert_to_utf16(input_unicode)
            utf32 = convert_to_utf32(input_unicode)

            print("Outputs:")
            print("UTF-8:", ' '.join(utf8[i:i+2] for i in range(0, len(utf8), 2)))
            print("UTF-16:", ' '.join(utf16[i:i+2] for i in range(0, len(utf16), 2)))
            print("UTF-32:", ' '.join(utf32[i:i+2] for i in range(0, len(utf32), 2)))
        else:
            print("Invalid input.")
    except ValueError:
        print("Error: Invalid Unicode input. Please provide valid Unicode text.")



if __name__ == "__main__":
    main()