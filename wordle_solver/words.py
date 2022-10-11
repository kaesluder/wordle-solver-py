from collections import Counter
from pprint import pprint 
import random


DEFAULT_WORD_FILE = "/usr/share/dict/words"

def load_words(letter_count = 5, filename=DEFAULT_WORD_FILE):
    """
    Load a list of words from a file, filter by letter_count, and 
    check case. Return word_list. 
    """

    word_list = []

    with open(filename) as file:
        while (line := file.readline().rstrip()):
            if len(line) == letter_count and line.isalpha():
                word_list.append(line.upper())

    # pprint(word_list[0:10])
    
    if word_list:
        return word_list
    else:
        return None 

def random_word(word_list):
    """
    Return a random word from the word_list.
    """

    return random.choice(word_list)

def build_letter_frequency_table(word_list):
    """Build a frequency table of all words in word_list."""

    frequency_table = Counter()

    for word in word_list:
        frequency_table.update(list(word))
    
    # pprint(frequency_table)
    return frequency_table

def word_fscore(word, ft):
    """
    Score the word based on its letter frequencies."""

    score_list = [ft[letter] for letter in word]
    return sum(score_list)

def word_uscore(word):
    """
    Score the word based on number of unique letters."""

    return len(set(list(word)))

def starter_word_score(word, ft):
    """
    Good starter words have a high number of unique characters 
    and high fscores."""

    return (word_uscore(word), word_fscore(word, ft))

def sort_by_starter_score(word_list, ft):
    """
    Sort word_list by starter score.
    """
    
    # curry our starter_word_score function
    f = lambda w: starter_word_score(w, ft)
    sorted_list = sorted(word_list, reverse=True, key=f)
    return sorted_list 

def filter_list_by_excludes(word_list, exclude_set):
    # exclude black characters 

    filtered = [word for word in word_list if not exclude_set.intersection(set(list(word)))]
    return filtered 

def filter_list_by_includes(word_list, include_set):
    # filter for words containing yellow characters

    filtered = [word for word in word_list if include_set.issubset(set(list(word)))]
    return filtered 

def word_matches_mask(word, mask):
    
    for pair in zip(word, mask):
        if pair[1].isalpha() and not pair[1] == pair[0]:
            return False
    return True 

def filter_for_mask(word_list, mask):
    #match greens

    filtered = [w for w in word_list if word_matches_mask(w, mask)]
    return filtered 

def filter_against_mask(word_list, mask):
    # exclude yellows

    filtered = [w for w in word_list if not word_matches_mask(w, mask)]
    return filtered 




def build_mask_by_matching(word1, word2):
    # mask for green letters

    mask_list = []
    for a, b in zip(word1, word2):
        if a == b:
            mask_list.append(a)
        else:
            mask_list.append("-")
    return "".join(mask_list)

def build_mask_by_weak_match(word1, target_word):
    # mask for yellow letters

    mask_list = []
    for a,b in zip(word1, target_word):
        if (a != b) and (a in target_word):
            mask_list.append(a)
        else:
            mask_list.append("-")
    return "".join(mask_list)

    





def score_words(word, target_word):
    "Score words by green, yellow, red letters."

    green_score = 0
    yellow_score = 0
    for a, b in zip(word, target_word):
        if a == b:
            green_score += 1
        elif a in target_word:
            yellow_score += 1
    return (green_score, yellow_score)

def score_words_masks(word, target_word):

    green_mask = build_mask_by_matching(word, target_word)
    yellow_mask = build_mask_by_weak_match(word, target_word)
    blacks = set(list(word)) - set(list(target_word))

    return (green_mask, yellow_mask, blacks)

def best_match(word, word_list, prior_list):
    best_score = None
    best_word = None
    for word2 in word_list:
        if word2 in prior_list:
            continue # skip words we've seen before.
        else:
            word2_score = score_words(word2, word)
            if word2_score > best_score:
                best_score = word2_score
                best_word = word2
    
    return best_word

def mask_score(mask):
    return len([a for a in mask if a.isalpha()])

def mask_to_set(mask):
    return set([a for a in mask if a.isalpha()])


def filter_down(word_list, green_mask, yellow_mask, black_list):
    new_list = list(word_list)
    if mask_score(green_mask):
        new_list = filter_for_mask(new_list, green_mask)
    if mask_score(yellow_mask):
        new_list = filter_against_mask(new_list, yellow_mask)
        new_list = filter_list_by_includes(new_list, mask_to_set(yellow_mask))
    
    if len(black_list) > 0:
        new_list = filter_list_by_excludes(new_list, black_list)

    return new_list 
    

    
    















