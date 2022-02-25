from multiprocessing.sharedctypes import Value
from global_vars import *
from utils import *


def state_inp_to_str(state_inp):
    state_str = ''
    for ch in state_inp:
        state_str += str((['b', 'y', 'g'].index(ch)))

    return state_str


def get_state_input():
    valid = False

    while not valid:
        valid = True
        state_inp = input(
            "Fill in colours in the following format: b for black, y for yellow and g for green. For example, if a word had no correct letters, the input would be 'bbbbb': ").strip().lower()

        if len(state_inp) != 5:
            print("Please make sure exactly 5 colours were put.")
            valid = False

        for ch in state_inp:
            if ch not in 'byg':
                print("Only letters b, y, and g are allowed")
                valid = False

        print()

    state_str = state_inp_to_str(state_inp)
    return state_str


def get_confirm(msg):
    yes_no = input(
        f"{msg} (y/n): ").strip().lower()

    if yes_no == 'y':
        return True
    elif yes_no == 'n':
        return False

    print("Invalid input.")
    get_confirm(msg)


print('='*9)

rnd = 1
did_win = False
avail_words = GUESS_ARR

while rnd <= 5 and not did_win:
    guess_rec, entropy = get_guess(avail_words)
    print(f"Recommended word: {guess_rec.upper()}")

    did_follow_rec = get_confirm('Did you follow the recommended word?')
    if not did_follow_rec:
        guess = input("What word did you input: ")
    else:
        guess = guess_rec

    did_win = get_confirm('Did you win?')

    if did_win:
        break

    print()
    state = get_state_input()

    avail_words = set(STATE_MAP[guess][state]) & set(avail_words)

    print("---")
    rnd += 1

if did_win:
    print('Congrats! You won!')
else:
    print('No... Sorry about that. Better luck next time!')
