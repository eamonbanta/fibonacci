import sys


VALID_CHOICES = {
    'q': '(q)uit',
}


def main():
    print "How do you want to calculate the fibonacci numbers?"
    print "Possible choices are:"
    print "(q)uit"

    fib_type = raw_input().strip()

    while fib_type not in VALID_CHOICES:
        print "Sorry, that's an invalid choice. Try again."
        print "Possible choices are:"
        print "(q)uit"
        fib_type = raw_input().strip()

    if fib_type != 'q':
        print "Great!"


    return 0

if __name__ == "__main__":
    sys.exit(main())
