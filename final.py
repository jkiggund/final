import jeremysql

class Password:
    """
    Class to determine whether password fits correct parameters
    """
    SpecialSym =['$', '@', '#', '%']

    def __init__(self, sentence:str):
        self.sentence = sentence

    def length(self):
        
        if len(self.sentence) < 8:
            checker = False
            raise ValueError("Password is too short")
        
        else:
            checker = True

        return checker

    def numbers(self):
        
        if not any(char.isdigit() for char in self.sentence):
            checker = False
            raise ValueError('Password should have at least one numeral')

        else:
            checker = True

        return checker

    def upper(self):

        if not any(char.isupper() for char in self.sentence):
            checker = False
            raise ValueError("Password needs to be an upper level at least one ")

        else:  
            checker = True

        return checker

    def lower(self):

        if not any(char.islower() for char in self.sentence):
            checker = False
            raise ValueError("Passwords needs to be at least one lower")

        else:
            checker = True
        
        return checker
            

    def special(self):

        SpecialSym =['$', '@', '#', '%']

        if not any(char in SpecialSym for char in self.sentence):
            checker = False
            raise ValueError("Passwords need a special character")
       
        else:
            checker = True

        return checker

    def repr(self):
        return f"Your very weak password is set to {self.sentence}"

        
class Great_Password(Password):

    # based on password, number of characters makes it secure or super secure 
    
    def __init__(self, sentence: str): # inheriting passwords methods with only one new to print the username
        super().__init__(sentence)

    def length(self):
        
        if len(self.sentence) < 16:
            checker = False
        
        else:
            checker = True

        return checker

    def repr(self):
        return f"Your very strong password is set to {self.sentence}"

def main():

    # ask them for a password for their account - use the assignment to sentence 
    # ask them for a new for their account 
    # print out both using f strings

    sentence = input("what is the pass: ")

    # good password = Aaaaaa123@
    # bad password = sahk

    pass_sentence = Password(sentence)
    acct = Great_Password(sentence)

    if pass_sentence.numbers() and pass_sentence.lower() and pass_sentence.length() and pass_sentence.upper() and pass_sentence.special():
        pass_checker = 1
    else:
        print("false")


    if acct.numbers() and acct.lower() and acct.length() and acct.upper() and acct.special():
        pass_checker = 2
    else:
        print("Make it at least 16 characters to have a strong password and more options")


    if pass_checker == 1:
        print(pass_sentence.repr())
        jeremysql.menu_2()
        option = int(input("Enter your option: "))
        while option != 0:

            if option == 1:
                sq = '''SELECT * FROM bookstore'''
                all_books = jeremysql.cursor.execute(sq).fetchall()
                print(all_books)

            else: 
                print("Invalid option")

            print()
            jeremysql.menu_2()
            option = int(input("Enter your option: "))


    if pass_checker == 2:
        print(acct.repr())
        jeremysql.menu()
        option = int(input("Enter your option: "))
        while option != 0:

            if option == 1:
                sq = '''SELECT * FROM bookstore'''
                all_books = jeremysql.cursor.execute(sq).fetchall()
                print(all_books)

            elif option == 2:
                price = '''SELECT * FROM bookstore ORDER BY price'''
                price_books = jeremysql.cursor.execute(price).fetchall()
                print(price_books)

            elif option == 3:
                rating = '''SELECT * FROM bookstore ORDER BY rating'''
                rating_books = jeremysql.cursor.execute(rating).fetchall()
                print(rating_books)

            elif option == 4:
                title = '''SELECT * FROM bookstore ORDER BY title'''
                title_books = jeremysql.cursor.execute(title).fetchall()
                print(title_books)

            elif option == 5:
                author = '''SELECT * FROM bookstore ORDER BY author'''
                author_books = jeremysql.cursor.execute(author).fetchall()
                print(author_books)

            else: 
                print("Invalid option")

            print()
            jeremysql.menu()
            option = int(input("Enter your option: "))
    
if __name__ == "__main__":
    main()



