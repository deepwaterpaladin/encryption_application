from one_time_pad import *

def encrypt_phrase(phrase: str):
    '''(str) -> tuple(str, lst of strings))
    Rudimentary encryption algorithm that encrypts a phrase using the one-time pad method.
    Takes a phrase (string of characters) and returns the encrypted phrase and a list of keys to decode the phrase.
    '''
    encrypted_letters=[]
    key_lst = []
    for letter in phrase:
        if letter == " ":
            encrypted_letters.append(" ")
            key_lst.append(ord(" ")+ord(letter))
        else:
            one_time_pad = one_time_pad_generator(letter)
            encrypted_letters.append(one_time_pad)
            key_lst.append(ord(one_time_pad)-ord(letter)) 
    encrypted_phrase=("".join(encrypted_letters))
    return encrypted_phrase, key_lst


