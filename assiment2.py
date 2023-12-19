def modify_string(s):
    modified_string = ""
    
    for i in range(len(s)):
        char = s[i]
        ascii_value = ord(char)

        if i % 2 == 0 and ascii_value % 2 == 0:
            next_ascii = ascii_value(i + 1) + (ascii_value % 7)
            if next_ascii <= 127:
                next_char = chr(next_ascii)
            else:
                next_char = chr(83)
            modified_string += next_char
        elif i % 2 == 1 and ascii_value % 2 == 1:
            prev_ascii = ascii_value(i - 1) - (ascii_value % 5)
            if prev_ascii >= 0:
                prev_char = chr(prev_ascii)
            else:
                prev_char = chr(83)
            modified_string += prev_char
        else:
            modified_string += char

    return modified_string
    