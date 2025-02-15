import random
import string


class Gen_Pass():
    def __init__(self, length, use_upper=True, use_digits=True, use_special=True):
        self.length = length
        self.use_upper = use_upper
        self.use_digits = use_digits
        self.use_special = use_special

    def generate(self):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase if self.use_upper else ""
        digits = string.digits if self.use_digits else ""
        special = string.punctuation if self.use_special else ""
        chars = lower + upper + digits + special

        if not chars:
            raise ValueError("No characters to choose from")
        
        return "".join(random.choice(chars) for _ in range(self.length))
    
    def save_pass(self, password, filename="password.txt"):
        with open(filename, "a") as f:
            f.write(password + "\n")

        print("password saved to", filename)






    