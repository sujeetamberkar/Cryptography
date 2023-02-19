import math
import statistics as st
NUM_ASCII_CHARS = 26 # 26 for alphabets and 128 for ascii
BASE_CHAR = ord('A') # ord('A') for alphabets and 0 for ascii 
ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key='key'
def guess_key_length(cipher: str):
    res = []
    for shift in range(len(cipher)):
        matches = 0
        for i in range(len(cipher)):
            if cipher[i] == cipher[(i - shift + len(cipher)) % len(cipher)]:
                matches=matches+1
        res.append(matches)
    dat_means = st.mean(res[1:])
    dat_std_dev   = math.sqrt(st.variance(res[1:]))
    peaks = []
    for i in range(len(res)):
        if res[i] >= dat_std_dev + dat_means:
            peaks.append(i)
    peak_diff = []
    for i in range(len(peaks) - 1):
        varNextPeak_CurrentPeak=peaks[i+1] - peaks[i]
        peak_diff.append(varNextPeak_CurrentPeak)

    mode_peadkDiff=st.mode(peak_diff)
    return mode_peadkDiff

def frequencyAnalysis(text):
    text=text.upper()
    letterFrequencies={}
    #print(type(letterFrequencies))
    for letter in ALPHABET:
        letterFrequencies[letter]=0

    for letter in text:
        letterFrequencies[letter] += 1
    freq = sorted(letterFrequencies.items(), key=lambda x: x[1], reverse=True)
    return freq

def vigenere_encrypt(plain_text,key):
    plain_text = plain_text.upper() #Make text case insensitive
    key = key.upper()
    cipher_text = '' #To store the cipher text
    key_index = 0 #Index of keys
    for letter in plain_text:
        if ord(letter)>=65 and ord(letter)<=90:
            index = (ALPHABET.find(letter)+ALPHABET.find(key[key_index])) % len(ALPHABET)
            cipher_text = cipher_text + ALPHABET[index]
            key_index = key_index + 1
            if key_index == len(key):
                key_index = 0
        else:
            cipher_text=cipher_text+' '
    return cipher_text 


def vigenere_decrypt(cipher_text,key):
    cipher_text = cipher_text.upper() #Make text case insensitive
    key = key.upper()
    plain_text = '' #To store the cipher text
    key_index = 0 #Index of keys
    for letter in cipher_text:
        if ord(letter)>=65 and ord(letter)<=90:
            index = (ALPHABET.find(letter)-ALPHABET.find(key[key_index])) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]
            key_index = key_index + 1
            if key_index == len(key):
                key_index = 0
        else:
            plain_text=plain_text+' '
    return plain_text 

def generateKey(cipher):
    keylenth=guess_key_length(cipher)
    divisions = ['' for i in range(keylenth)]
    for i in range(len(cipher)):
        divisions[i % keylenth] += cipher[i]
    key=''
    for i in range(keylenth):
        subFreqData=frequencyAnalysis(divisions[i])
        letterKey=chr(BASE_CHAR + ((ord(subFreqData[0][0]) - ord('E')) % NUM_ASCII_CHARS) )
        key=key+str(letterKey)
    
    print(key)
    return key


def main():
    message='This is a standard deviation'
    message=message.upper()
    cipherText=vigenere_encrypt(message,key)
    plain_text=vigenere_decrypt(cipherText,key)
    print(generateKey(cipherText))


main()
