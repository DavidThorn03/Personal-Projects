;class UserInput:

    @staticmethod
    def input_yn(prompt): # method to get user input where answers are yes or no
        f_answer = ["y", "yes"]
        s_answer = ["n", "no"]
        return UserInput.input_option_boolean(f_answer, s_answer, prompt)

    @staticmethod
    def input_option(answers, options, prompt): # method to get user input with multiple possible answers
        fail_prompt = "Incorrect input. " + prompt
        while True:
            user_input = input(prompt).lower().strip() # removes whitespace at start or end of string
            for index, row in enumerate(answers):
                if user_input in row:
                    print(options[index])
                    return options[index]

                prompt = fail_prompt

    @staticmethod
    def input_option_boolean(f_answers, s_answers, prompt): # method to get user input with 2 possible answers
        answers = [f_answers, s_answers]
        options = [True, False]
        return UserInput.input_option(answers, options, prompt)

    @staticmethod
    def input_number(prompt):
        fail_prompt = "Non number input", prompt
        while True:
            num = input(prompt).strip()
            if num.isdigit():
                return int(num)
            else:
                prompt = fail_prompt