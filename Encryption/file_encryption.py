from phrase_encryption import *

def file_encryption(infile):
    '''(file of strings) -> list of strings, list of ints
    
    '''
    file=open(infile, "r+")
    content=file.readlines()
    encrypted_letters_from_file = []
    key_lst_from_file=[]
    for line in content:    
        encrypted_letters_from_file.append(encrypt_phrase(line)[0])
        key_lst_from_file.append(encrypt_phrase(line)[1])
        print(len(line))
    file.close()
    return encrypted_letters_from_file, key_lst_from_file



def fileWriteV2(file_to_be_encrypted, encrypted_file):
    '''(file of strings, empty file) -> file of strings.
    Takes a file of strings and returns an encrypted file. The last line of the file will be th encryption key. Last line of the encrypted text is index[-3].
    '''
    encryptLst = []
    keyLst=[]
    i = 0
    file=open(file_to_be_encrypted, "r+")
    out = open(encrypted_file, "w+")
    content=file.readlines()
    for line in content:    
        encryptLst.append(encrypt_phrase(line)[0])
        keyLst.append(encrypt_phrase(line)[1])
        i+=1
    file.close()
    k=0
    for word in encryptLst:
        out.write(word)
        out.write("\n")
    out.write("\n")
    out.write("Encryption Key:")
    out.write("\n")
    #for i in keyLst: this would be the key as a string separated by *
        #mess=("*".join(i)) 
    x=keyLst
    out.write(str(x))
    out.close()
    print(f"File encrypted! \n \n {i} lines encrypted.")
    return out # if this stops working, try deleting this line and rerunning the program.