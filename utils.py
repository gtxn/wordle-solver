import re
import math

from global_vars import *

# Analysis


def get_n_highest_entropy(n, avail_words):
    if len(avail_words) < 2:
        return avail_words.pop()

    high_score_words = [''] * n
    high_score_entropy = [-1] * n

    for g_word in GUESS_ARR:
        entropy = calc_entropy(g_word, avail_words)

        i = n

        if entropy > high_score_entropy[i-1]:
            while i > 0 and entropy > high_score_entropy[i-1]:
                if i != n:
                    high_score_words[i] = high_score_words[i-1]
                    high_score_entropy[i] = high_score_entropy[i-1]

                i -= 1

            high_score_words[i] = g_word
            high_score_entropy[i] = entropy

    high_score = [{high_score_words[i]: high_score_entropy[i]}
                  for i in range(n)]

    return high_score

# Get state


def get_state(g_word, a_word):
    g_word, a_word = list(g_word), list(a_word)
    # 0 if not found, 1 if found but wrong pos, 2 if found and right pos
    state_arr = [0 for i in range(5)]
    for i, g_char in enumerate(g_word):
        ind_found = [m.start() for m in re.finditer(g_char, ''.join(a_word))]

        if i in ind_found:
            state_arr[i] = 2
        elif len(ind_found) != 0:
            state_arr[i] = 1

    return state_arr


def calc_entropy(word, avail_words):
    avail_words_set = set(avail_words)

    entropy_summation = 0

    for state, word_list in STATE_MAP[word].items():
        new_list_set = set(word_list) & avail_words_set

        if len(new_list_set) == 0:
            continue

        # Px calculates the probability this state occurs
        px = len(new_list_set) / len(avail_words)

        # Information calculates number of bits of information this state has
        information = math.log(1/px, 2)

        single_entropy = px * information
        entropy_summation += single_entropy

    return entropy_summation


def get_guess(avail_words):
    if len(avail_words) < 2:
        return avail_words.pop(), None
    elif len(avail_words) == len(GUESS_ARR):
        return 'soare', 5.9

    guess = ''
    high_entropy = -1

    for g_word in GUESS_ARR:
        entropy = calc_entropy(g_word, avail_words)
        if entropy > high_entropy:
            guess = g_word
            high_entropy = entropy

    return guess, high_entropy

# State is a STRING


def state_to_wordle(state):
    wordle_arr = ["⬛", "🟧", "🟩"]
    fin_str = ''
    for num in state:
        fin_str += wordle_arr[int(num)]
    return fin_str
