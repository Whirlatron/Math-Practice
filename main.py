import random
import time

def generateproblem():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    
    p = '%i * %i' % (a, b)
    s = a * b
    return (p, s)

def main():
    probs = 0
    cprobs = 0
    start = time.time()
    while True:
        p, s = generateproblem()
        print(p)
        i = input('>>>')
        if i.lower() in ('stop', 'exit'):
            break
        try:
            if int(i) == s:
                print('Correct!')
                cprobs += 1
            else:
                print('Wrong!')
        except ValueError:
            print('Invalid answer.')
        probs += 1
    end = time.time()

    elapsed = round(end-start, 2)
    percent = round(cprobs / probs * 100, 2)
    persec = round(probs / elapsed, 2)

    print(f'You got {cprobs} problems right out of {probs}')
    print(f'Your accuracy was {percent}%')
    print(f'You practiced for {elapsed} seconds.')
    print(f'You completed {persec} problems per second')


if __name__ == '__main__':
    main()