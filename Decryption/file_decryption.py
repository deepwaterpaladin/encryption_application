from phrase_decryption import *

def clean(str: str):
    '''(str) -> str
    Takes a string and returns a string without the apostrophies, brackets, or line breaks.
    '''
    str1= str.replace("'", "")
    str2= str1.replace("[", "")
    str3= str2.replace("]", "")
    str4= str3.replace("\n", "")
    return str4

def file_decrypt(outfile):
    file=open(outfile, "r+")
    content=file.readlines()
    numOfLines=len(content)
    key= content[-1]
    cleanstr=clean(key)
    myKey = [int(s) for s in cleanstr.split(',')]
    message=[str(s) for s in content[:-3]]
    suh = len(myKey)/len(message)
    sss= []
    for k in range(0,len(message)-1):
        for i in range(int(suh)):
            sss.append(myKey[i])
            myKey.remove(myKey[i])
    newLst=sss, myKey
    list(newLst)
    return (len(sss), len(message), len(myKey), len(newLst[0])), len(newLst[1])