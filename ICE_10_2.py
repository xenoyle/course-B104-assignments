 # Programmer:         Connor Floyd
 # Course:             CSCI/ISAT B104
 # Assignment:         ICE 10.2


# step 1 **
# l = "}"
# l_unicode = ord(l)


# step 2 **
# word = "Pineapple"
# for l in word:
#     print(f"The unicode for character {l} is {ord(l)}")


# step 3 **
# word = "Pineapple"
# word_unicode = ""
# for l in word:
#     word_unicode += "." + str(ord(l))


# step 4 **
# word = "Pineapple"
# word_encrypted = ""
# for l in word:
#     word_encrypted += "." + str(ord(l)+2)
    
    
# step 5 **
# word = "Pineapple"
# word_encrypted = ""
# for l in word:
#     word_encrypted += chr(ord(l)+2)


# step 6 **
# word = "Pineapple"
# word_encrypted = ""
# word_decrypted = ""
# for l in word:
#     word_encrypted += chr(ord(l)+2)
# for n in word_encrypted:
#     word_decrypted += chr(ord(n)-2)


# step 7 **
# word = input("Passphrase: ")
# word_encrypted = ""
# word_decrypted = ""
# for l in word:
#     word_encrypted += chr(ord(l)+2)
# for n in word_encrypted:
#     word_decrypted += chr(ord(n)-2)


# step 8 **
# word = input("Passphrase: ")
# shift = eval(input("Shift: "))
# word_encrypted = ""
# word_decrypted = ""
# for l in word:
#     word_encrypted += chr(ord(l)+shift)
# for n in word_encrypted:
#     word_decrypted += chr(ord(n)-shift)


## Final Version ****
# create functions
def encrypt_phrase(word,shift):
    word_encrypted = ""
    for n in word:
        word_encrypted += chr(ord(n)+shift)
    return word_encrypted

def decrypt_phrase(word,shift):
    word_decrypted = ""
    for n in word:
        word_decrypted += chr(ord(n)-shift)
    return word_decrypted

word = input("Passphrase: ")
shift = eval(input("Shift: "))
encrypt = encrypt_phrase(word,shift)
decrypt = decrypt_phrase(encrypt,shift)
print(f"\nThe encryption is {encrypt}")
print(f"\nThe decryption is {decrypt}")


