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