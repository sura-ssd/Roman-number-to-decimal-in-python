""" I = 1; V = 5; X = 10; L = 50; C = 100; D = 500; M = 1000"""


class NumberNotValid(Exception):
    pass


def user_input():
    while True:
        try:
            user_num = input('Enter a Roman numeral between 1 and 3,999: ')
            char_check = [char for char in user_num]
            for char in char_check:
                if char not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
                    raise NumberNotValid
            else:
                return user_num

        except NumberNotValid:
            print("Your number is not valid. Try again, using only the "
                  "following characters: 'I', 'V', 'X', 'L', 'C', 'D', 'M'.\n")


class RomanToDecimal:
    def __init__(self):
        self.num = user_input()
        self.rom_val = {'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000}

    def calc(self):
        int_val = 0
        for i in range(len(self.num)):
            if i > 0 and self.rom_val[self.num[i]] \
                         > self.rom_val[self.num[i-1]]:
                int_val += self.rom_val[self.num[i]] \
                           - 2 * self.rom_val[self.num[i-1]]
            else:
                int_val += self.rom_val[self.num[i]]
        print(self.num, '=', int_val)


def main():
    RomanToDecimal().calc()
    input()


if __name__ == '__main__':
    main()




