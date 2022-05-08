

def decrypt(phrase: str, key: list):
    accum = 0
    decrypted_letters = []
    for i in key:
        if i == "," or i == "." or i == "" or i == " ":
            key.remove(i)
    for i in key:
        if phrase[accum] == " ":
            decrypted_letters.append(" ")
            accum += 1
        else:
            decrypted_letters.append(chr(ord(phrase[accum])-int(i)))
            accum += 1
    decrypted_message=("".join(decrypted_letters))
    return decrypted_message

# Test phrase: "The quick brown fox jumps over the lazy dog"
t_phrase="jV4 299Kx zKdJV FOf RSLRb InfA IlN RTFQ D0z"
otp=[22, -18, -49, 64, -63, -60, -48, -24, 13, 64, 24, -39, -11, -45, -24, 64, -32, -32, -18, 64, -24, -34, -33, -30, -17, 64, -38, -8, 1, -49, 64, -43, 4, -23, 64, -26, -13, -52, -40, 64, -32, -63, 19]

decrypted_message = decrypt(t_phrase, otp)
p = "sGH9h QISirMOjp D7Lnwn"
k = [43, -30, -36, -51, -7, 64, 1, -41, -28, 3, 13, -38, -36, -5, -2, 64, -19, -50, -32, 2, 4, 77]
#print(decrypt(p, k))