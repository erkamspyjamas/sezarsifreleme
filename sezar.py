def sezarsifreleme(message,key):
    encrypted_message = ""
    alphabet = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','q','r','s','ş','t','u','ü','v','w','x','y','z']

    for i in message:
        if i not in alphabet:
            encrypted_message += i
        else:
            encrypted_message += alphabet[(alphabet.index(i)+key) % len(alphabet)]
    print("The encrypted message is : ", encrypted_message)

sezarsifreleme("mübarek", 2)


"""
if do you need decrypt a message, run this function.
But, you need to know key to decrypt.
"""
def decryptsezar(message,key):
    decrypted_message = ""
    alphabet = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','q','r','s','ş','t','u','ü','v','w','x','y','z']
    for i in message:
        if i not in alphabet:
            decrypted_message += i
        else:
            decrypted_message += alphabet[(alphabet.index(i)-key) % len(alphabet)]
    print("The decrypted message is : ", decrypted_message)

decryptsezar("owçcşgm",2)


