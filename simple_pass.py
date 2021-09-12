import sys
import random

def main():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'

    try:
        amount_of_characters = int(sys.argv[1])
        if amount_of_characters < 1:
            print('Error on input: ' + str(amount_of_characters))
            print('Number of characters should be a positive integer.')
            exit(1)

        for _ in range(amount_of_characters):
            print(characters[random.randrange(len(characters))], end='')

        print()
    except ValueError as e:
        print(e.args[0])
        print('Number of characters should be a positive integer.')
        sys.exit(1)

if __name__ == '__main__':
    main()