import sys


VALID_CHOICES = {
    'q': '(q)uit',
}


def print_choice_list():
    print "Possible choices are:"
    for choice in VALID_CHOICES.values():
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
        print "Great!"

    return 0


if __name__ == "__main__":
    sys.exit(main())
