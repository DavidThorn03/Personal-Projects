from UserInput import UserInput as ui
import random
import string


class Substitution:

    chars = list(" " + string.ascii_letters + string.digits + string.punctuation) # characters used in encryption

    @staticmethod
    def random_encrypt(plain_text): # encrypt without key
        key = Substitution.chars.copy() # get used characters
        random.shuffle(key) # randomise key

        encryption_text = ""

        for letter in plain_text: # swap letters from plain text with corresponding key letters
            index = Substitution.chars.index(letter)
            encryption_text += key[index]

        print(f"Original message : {plain_text}")
        print(f"Encrypted message : {encryption_text}")

        decrypted_text = ""

        for letter in encryption_text: # swap letters from encryption text with corresponding key letters
            index = key.index(letter)
            decrypted_text += Substitution.chars[index]

        print(f"Decoded message : {decrypted_text}")

    @staticmethod
    def key_encrypt(plain_text):
        key = Substitution.get_key()
        encryption_text = ""

        for letter in plain_text:
            index = Substitution.chars.index(letter)
            encryption_text += key[index]

        print(f"Original message : {plain_text}")
        print(f"Encrypted message : {encryption_text}")

    @staticmethod
    def key_decrypt(encryption_text):
        key = Substitution.get_key()
        decryption_text = ""

        for letter in encryption_text:
            index = key.index(letter)
            decryption_text += Substitution.chars[index]

        print(f"Original message : {encryption_text}")
        print(f"Decrypted message : {decryption_text}")


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
    def run(message, encrypted):
        key_created = ui.input_yn("Is the key in the keys.txt file (Yes or No)? ")

        if key_created:
            if encrypted:
                Substitution.key_encrypt(message)
            else:
                Substitution.key_decrypt(message)
        else:
            Substitution.random_encrypt(message)
