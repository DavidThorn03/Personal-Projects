from Substitution import Substitution as s
from UserInput import UserInput as ui


options = ["c", "e"]
answers = [["c", "caesar"],
           ["e", "encryption"]]
prompt = "Is the code a Caesar cipher (C) or encryption(E)? "

cipher = ui.input_option(answers, options, prompt)

if cipher == "c":
    c.run()
elif cipher == "e":
    e.run()