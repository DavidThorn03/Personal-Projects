from UserInput import UserInput as ui
import string

class Shift:
    @staticmethod
    def basic_shift(message, shift, encrypt):
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
    def ascii_shift(message, shift, encrypt):
        new_message = ""
        if not encrypt:
            shift = -shift

        for char in message:
            new_message += chr((ord(char) + shift) % 128)

        return new_message

    @staticmethod
    def reverse_shift(message, shift, encrypt):
        reverse = message[::-1] # this is how to reverse string in python
        return Shift.basic_shift(reverse, shift, encrypt)

    def reverse_ascii_shift(message, shift, encrypt):
        reverse = message[::-1]
        return Shift.ascii_shift(reverse, shift, encrypt)

    @staticmethod
    def unknown_ascii_shift(message):
        new_message = ""
        for shift in range(0, 27):
            for char in message:
                new_message += chr((ord(char) + shift) % 128)

            print("Shift " + str(shift) + ": " + new_message)
            new_message = ""


    @staticmethod
    def run(message, encrypted):
        if not encrypted:
            prompt = "Is the shift known (Yes or No)?"
            shift_known = ui.input_yn(prompt)

            if not shift_known:
                prompt = "Enter the message to be decrypted: "
                message = input(prompt)
                Shift.unknown_ascii_shift(message)
                return

        # get shift value
        shift = ui.input_number("Enter the encryption shift value: ")

        # see if encryption has been reversed
        prompt = "Is the encryption reversed (Yes or No)? "
        reversed = ui.input_yn(prompt)

        # see if all characters or just letters have been reversed
        if encrypted:
            prompt = "Are only letter characters going to be encrypted(Yes or No)? "
        else:
            prompt = "Are only letter characters encrypted(Yes or No)? "

        ascii = not ui.input_yn(prompt)

        # get result
        if reversed and ascii:
            result = Shift.reverse_ascii_shift(message, shift, encrypted)
        elif reversed and not ascii:
            result = Shift.reverse_shift(message, shift, encrypted)
        elif not reversed and ascii:
            result = Shift.ascii_shift(message, shift, encrypted)
        else:
            result = Shift.basic_shift(message, shift, encrypted)
        # print result
        if encrypted:
            print("The encrypted message is:", result)
        else:
            print("The decrypted message is:", result)



