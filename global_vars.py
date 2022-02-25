import json

# Get answers and guesses
f_ans = open('./wordlists/answers.txt')
f_guess = open('./wordlists/guesses.txt')

ANS_ARR = f_ans.read().strip().split('\n')
GUESS_ARR = ANS_ARR + f_guess.read().strip().split('\n')

# Get statemap
STATEMAP_PATH = './outputs/statemap.json'

with open(STATEMAP_PATH) as f:
    print('Loading statemap...')
    STATE_MAP = json.load(f)
    print('Statemap loaded')

