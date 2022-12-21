import string
import random

class random_pass:
    def __init__(self, length) -> None:
        self.length = length
        print(f'Your password is {self.main()}')
        
    def main(self) -> str:
        self.password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(self.length))
        return self.password
    
if __name__ == '__main__':
    length = int(input('Enter the length of the password: '))
    random_pass(length)
