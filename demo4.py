class checkpasswordstrength:
    def __init__(self):
        self.password=input("Enter password:")
    def checkstrength(self):
            if len(self.password)<8:
                return "password is weak.it should have at least minimum length of 8 character"
            if not any(char.upper() for char in self.password):
                return "password is weak.it should contain at least one uppercase letter"
            if not any(char.lower() for char in self.password):
                return "password is weak.it should contain at least one lowercase letter"
            if not any(num.isdigit() for num in self.password):
                return "password is weak.it should contain at least one number"
            special="!@#$%^&*()_+=-{}'|:<>?/.,;[]\`~"
            if not any(char in special for char in self.password):
                return "password is weak.it should contain at least special symbol"
            return "password is strong"
obj=checkpasswordstrength()
result=obj.checkstrength()
print(result)
