import random

class Help:
    @staticmethod
    def generate_email():
        return f"OSneg7_{random.randint(100, 999)}@gmail.com"

    @staticmethod
    def generate_incorrect_email():
        return f"OSneg7_{random.randint(100, 999)}"