from UserInput import UserInput as ui
import random
import string


class Encryption:

    chars = list(" " + string.ascii_letters + string.digits + string.punctuation) # characters used in encryption

    @staticmethod
    def random_encrypt(): # encrypt without key
        key = Encryption.chars.copy() # get used characters
        random.shuffle(key) # randomise key

        plain_text = input("Enter a message to be encrypted: ")
        cipher_text = ""

        for letter in plain_text: # swap letters from plain text with corresponding key letters
            index = Encryption.chars.index(letter)
            cipher_text += key[index]

        print(f"Original message : {plain_text}")
        print(f"Encrypted message : {cipher_text}")

        decoded_text = ""

        for letter in cipher_text: # swap letters from cipher text with corresponding key letters
            index = key.index(letter)
            decoded_text += Encryption.chars[index]

        print(f"Decoded message : {decoded_text}")

    @staticmethod
    def key_encrypt():
        key = Encryption.get_key()
        plain_text = input("Enter a message to be encrypted: ")
        cipher_text = ""

        for letter in plain_text:
            index = Encryption.chars.index(letter)
            cipher_text += key[index]

        print(f"Original message : {plain_text}")
        print(f"Encrypted message : {cipher_text}")

    @staticmethod
    def key_decrypt():
        key = Encryption.get_key()
        cipher_text = input("Enter a message to be decrypted: ")
        decoded_text = ""

        for letter in cipher_text:
            index = key.index(letter)
            decoded_text += Encryption.chars[index]

        print(f"Original message : {cipher_text}")
        print(f"Decrypted message : {decoded_text}")


    @staticmethod
    def get_key():
        key_num = ui.input_number("Which key is needed? ")
        f = open("keys.txt", "r")
        for i in range(key_num):
            key = f.readline()

        return list(key)

    @staticmethod
    def make_keys(num_keys):
        f = open("keys.txt", "w")
        f.write('')
        for x in range(num_keys):
            chars = list(" " + string.ascii_letters + string.digits + string.punctuation)
            random.shuffle(chars)
            chars = ''.join(chars)
            f.write(chars)
            f.write("\n")
        f.close()

    @staticmethod
    def run():
        key_created = ui.input_yn("Is the key in the keys.txt file (Yes or No)? ")

        if key_created:
            f_answers = "e", "encrypted"
            s_answers = "d", "decrypted"
            prompt = "Would you like to encrypt (E) or decrypt (D) the cipher? "
            encrypted = ui.input_option_boolean(f_answers, s_answers, prompt)
            if encrypted == True:
                Encryption.key_encrypt()
            else:
                Encryption.key_decrypt()
        else:
            Encryption.random_encrypt()
