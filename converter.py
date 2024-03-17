def convert_to_utf8(unicode):
    pass

def convert_to_utf16(unicode):
    pass

def convert_to_utf32(unicode):
    pass


def main():
    print("---------Unicode Converter---------")
    input_unicode = input("Input (Unicode): ")
    
    # check if input is valid
    
    # convert
    utf8 = convert_to_utf8(input_unicode)
    utf16 = convert_to_utf16(input_unicode)
    utf32 = convert_to_utf32(input_unicode)

    # print outputs
    print("Outputs:")
    print("UTF-8: ", utf8)

    print("UTF-16: ", utf16)

    print("UTF-32: ", utf32)


if __name__ == "__main__":
    main()