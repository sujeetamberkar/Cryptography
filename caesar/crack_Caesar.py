ALPHABET="".join(chr(x) for x in range(128))
key=3
def caesar_encryption(plain_text,key):
    cipher_text='' #To store cipher Text
    plain_text=plain_text.upper() #To make case insensitive
    for c in plain_text:
        index=ALPHABET.find(c) #Find the index in ALPHABET
        index=(index+key)%len(ALPHABET)
        cipher_text=cipher_text+ALPHABET[index]
    return cipher_text

def caesar_decryption(cipher_text,key):
    plain_text=''
    for c in cipher_text:
        index=ALPHABET.find(c) #Find the index in ALPHABET
        index=(index-key)% len(ALPHABET)
        plain_text=plain_text+ALPHABET[index]
    return plain_text


def bruteCeacer (cipher_text):
    for key in range(len(ALPHABET)):
        plain_text=caesar_decryption(cipher_text,key)
        check=languageDetectorAlgorithm(plain_text)
        if check is True:
            print('Key: '+ str(key)+ '\n\t'+plain_text)
def languageDetectorAlgorithm(inputText):
    EnglishWords=[]
    match=0
    totalWords=len(inputText.split(' '))
    Checkwordsinput=[]
    dictionary = open('english_words.txt', 'r')
    for word in dictionary.read().split('\n'):
        EnglishWords.append(word)
    for word in inputText.split(' '):
        word=word.upper()
        if word in EnglishWords:
            match=match+1
    if (float(match)/totalWords)*100 >=50:
        return True
    else:
        return False

def frequencyAnalysis(text):
    text=text.upper()
    letterFrequencies={}

    for letter in ALPHABET:
        letterFrequencies[letter]=0

    for letter in text:
        letterFrequencies[letter] += 1
    return letterFrequencies

def crackCaesar(cipher_text):
    freq=frequencyAnalysis(cipher_text)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    possibleKeys=[]
    key=ALPHABET.find(freq[0][0])-ALPHABET.find(' ')
    possibleKeys.append(key)
    key=ALPHABET.find(freq[1][0])-ALPHABET.find('E')
    if key not in possibleKeys:
        possibleKeys.append(key)
    key=ALPHABET.find(freq[1][0])-ALPHABET.find('A')
    if key not in possibleKeys:
        possibleKeys.append(key)
    
    for key in possibleKeys:
        plain_text=caesar_decryption(cipher_text,key)
        check=languageDetectorAlgorithm(plain_text)
        if check is True:
            print('Key: '+ str(key)+ '\n\t'+plain_text)

if __name__ == '__main__':
    text="This is a demo text"
    encrptedText=caesar_encryption(text,8)
    bruteCeacer(encrptedText)
