from UserInput import UserInput as ui


class Caesar:
    @staticmethod
    def caesar(message, shift, encrypt):
        new_message = ""
        if not encrypt:
            shift = -shift

        for char in message:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                new_message += chr((ord(char) - base + shift) % 26 + base)
            else:
                new_message += char
        return new_message

    @staticmethod
    def ascii_caesar(message, shift, encrypt):
        new_message = ""
        if not encrypt:
            shift = -shift

        for char in message:
            new_message += chr((ord(char) + shift) % 128)

        return new_message

    @staticmethod
    def reverse_caesar(message, shift, encrypt):
        reverse = message[::-1] # this is how to reverse string in python
        return Caesar.caesar(reverse, shift, encrypt)

    def reverse_ascii_caesar(message, shift, encrypt):
        reverse = message[::-1]
        return Caesar.ascii_caesar(reverse, shift ,encrypt)

    @staticmethod
    def run():
        # see if we want to encrypt or decrypt
        f_answers = "e", "encrypted"
        s_answers = "d", "decrypted"
        prompt = "Would you like to encrypt (E) or decrypt (D) the cipher? "
        encrypted = ui.input_option_boolean(f_answers, s_answers, prompt)

        # see if cipher has been reversed
        prompt = "Is the cipher reversed (Yes or No)? "
        reversed = ui.input_yn(prompt)

        # see if all characters or just letters have been reversed
        if encrypted:
            prompt = "Are only letter characters going to be encrypted(Yes or No)? "
        else:
            prompt = "Are only letter characters encrypted(Yes or No)? "

        ascii = not ui.input_yn(prompt)

        # get shift value
        shift = ui.input_number("Enter the ciphers shift value: ")

        # get message
        if encrypted:
            prompt = "Enter the cipher to be encrypted: "
        else:
            prompt = "Enter the cipher to be decrypted: "

        message = input(prompt)

        # get result
        if reversed and ascii:
            result = Caesar.reverse_ascii_caesar(message, shift, encrypted)
        elif reversed and not ascii:
            result = Caesar.reverse_caesar(message, shift, encrypted)
        elif not reversed and ascii:
            result = Caesar.ascii_caesar(message, shift, encrypted)
        else:
            result = Caesar.caesar(message, shift, encrypted)
        # print result
        if encrypted:
            print("The encrypted message is:", result)
        else:
            print("The decrypted message is:", result)



