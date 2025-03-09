from Substitution import Substitution as sub
from UserInput import UserInput as ui
from Shift import Shift


class Controller:

    @staticmethod
    def run():
        #see if we want to encrypt or decrypt
        f_answers = "e", "encrypted"
        s_answers = "d", "decrypted"
        prompt = "Would you like to encrypt (E) or decrypt (D)? "
        encrypted = ui.input_option_boolean(f_answers, s_answers, prompt)


        #see what type of encryption is used
        options = ["sh", "sub"]
        answers = [["sh", "shift"],
                   ["sub", "substitution"]]
        prompt = "Is the encryption a shift (sh) or substitution(sub)? "
        type = ui.input_option(answers, options, prompt)

        #get message to be encrypeted/decrypted
        if encrypted:
            message = input("Enter message to be encrypted: ")
        else:
            message = input("Enter message to be decrypted: ")


        if type == "sh":
            Shift.run(message, encrypted)
        elif type == "sub":
            sub.run(message, encrypted)