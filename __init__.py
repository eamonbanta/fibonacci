import sys

import fibonacci


VALID_CHOICES = ('q', 'n', 'a', 't')
VALID_CHOICE_NAMES = [
    '(q)uit',
    '(n)aive (very slow for n > 40, exceeds recursion limit near n == 100)',
    '(a)rray',
    '(t)uple swap',
]

CHOICE_TO_METHOD = {
    'n': fibonacci.naive_fib,
    'a': fibonacci.array_fib,
    't': fibonacci.tuple_swap_fib,
}


def print_choice_list():
    print "Possible choices are:"
    for choice in VALID_CHOICE_NAMES:
        print choice


def main():
    print "How do you want to calculate the fibonacci numbers?"
    print_choice_list()
    choice_made = raw_input().strip()

    while choice_made not in VALID_CHOICES:
        print "Sorry, that's an invalid choice. Try again."
        print_choice_list()
        choice_made = raw_input().strip()

    if choice_made != 'q':
        print "Great! What fibonacci index do you want to calculate?"
        n = int(raw_input())

        print CHOICE_TO_METHOD[choice_made](n)

    return 0


if __name__ == "__main__":
    sys.exit(main())
