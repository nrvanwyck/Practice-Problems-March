# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

def rot13(message):
    coded = []
    for char in message:
        if (ord(char) > 64) and (ord(char) < 78):
            coded.append(chr(ord(char)+13))
        elif (ord(char) >= 78) and (ord(char) < 91):
            coded.append(chr(ord(char)-13))
        elif (ord(char) > 96) and (ord(char) < 110):
            coded.append(chr(ord(char)+13))
        elif (ord(char) >= 110) and (ord(char) < 123):
            coded.append(chr(ord(char)-13))
        else:
            coded.append(char)
    return ''.join(coded)