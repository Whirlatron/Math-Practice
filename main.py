import random

def main():
    while True:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        s = a * b
        print('%i * %i' % (a, b))
        i = input('>>>')
        if int(i) == s:
            print('Correct!')
        else:
            print('WRONG!')

if __name__ == '__main__':
    main()