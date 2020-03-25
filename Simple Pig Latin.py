# Move the first letter of each word to the end of it, then add "ay" to the end 
# of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    words = text.split(' ')
    translated = [(word[1:] + word[0] + 'ay'
                  ) if word.isalpha() else word for word in words]
    return ' '.join(translated)
