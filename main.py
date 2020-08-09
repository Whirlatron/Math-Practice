import random

def generateproblem():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    
    p = '%i * %i' % (a, b)
    s = a * b
    return (p, s)

def main():
    while True:
        p, s = generateproblem()
        print(p)
        i = input('>>>')
        if i.lower() in ('stop', 'exit'):
            break
        try:
            if int(i) == s:
                print('Correct!')
            else:
                print('WRONG!')
        except ValueError:
            print('Invalid answer.')

if __name__ == '__main__':
    main()