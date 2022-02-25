import random

from utils import *
from global_vars import *


def main():
    print('Starting game')
    print('='*10)

    answer_word = random.choice(ANS_ARR)
    print(f'Answer word: {answer_word}')
    print('---')

    avail_words = ANS_ARR

    round_num = 1
    won = False

    while not won and round_num <= 5:
        print(f"Round number {round_num}")
        print(f"{len(avail_words)} words to choose from")

        guess_word, entropy = get_guess(avail_words)

        print(f"Guessed: {guess_word} || Entropy: {entropy}")

        state = ''.join(map(str, get_state(guess_word, answer_word)))
        state_wordle_style = state_to_wordle(state)
        print(state_wordle_style)

        avail_words = set(STATE_MAP[guess_word][state]) & set(avail_words)
        
        if guess_word == answer_word:
            won = True
            break

        print('---')

        round_num += 1

    if won:
        print(f"Won in {round_num} rounds")
    else:
        print(f"Lost to word {answer_word}")


if __name__ == "__main__":
    main()
