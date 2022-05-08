import string
import secrets

def one_time_pad_generator(phrase: str):
    '''(str) -> str
    Takes a phrase and returns a random key for the phrase.
    '''
    alphabet = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(alphabet) for i in range(len(phrase)))
    #key = ''.join(secrets.choice(alphabet) for i in range(len(phrase)^len(phrase))) # this didn't work. If you uncomment this, you'll get an error.
    return key