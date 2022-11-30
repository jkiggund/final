
class Password:
    """
    Class to determine whether password fits correct parameters
    """
    SpecialSym =['$', '@', '#', '%']
    checker = True

    def __init__(self, sentence:str):
        self.sentence = sentence

    def length(self, sentence:str):

        self.sentence = sentence
        
        if len(self.sentence) < 8:
            self.checker = False
            raise ValueError("Password is too short")
        
        else:
            self.checker = True

    def numbaz(self, sentence:str):
        
        if not any(char.isdigit() for char in sentence):
            self.checker = False
            raise ValueError('Password should have at least one numeral')

        else:
            self.checker = True

    def uppa(self, sentence:str):

        if not any(char.isupper() for char in sentence):
            self.checker = False
            raise ValueError("Password needs to be an upper level at least one ")

        else:  
            self.checker = True

    def lowwa(self, sentence:str):

        if not any(char.islower() for char in sentence):
            self.checker = False
            raise ValueError("Passwords needs to be at least one lower")

        else:
            self.checker = True
            

    def special(self, sentence:str):

        SpecialSym =['$', '@', '#', '%']

        if not any(char in SpecialSym for char in sentence):
            raise ValueError("Passwords need a special character")
       
        else:
            self.checker = True

    def bigPass(self):
        return f"Your password is set to {self.sentence}"

        
class Account(Password):
    
    def __init__(self, sentence: str): # inheriting passwords methods with only one new to print the username
        super().__init__(sentence)

        self.sentence = sentence

    def bigUser(self):
        return f"Your username is set to {self.sentence}"

def main(sentence:str):

    sentence = input("what is the pass")

    if Password(sentence) == True:
        print("good")
    
if __name__ == "__main__":
    main()



