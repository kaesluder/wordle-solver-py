import pytest
from wordle_solver.words import *

def test_words_loads_wordlist():

    result = load_words()
    assert result 

def test_load_words_word_length_works():

    word5 = load_words(letter_count=5)[0]
    word6 = load_words(letter_count=6)[0]

    assert len(word5) == 5
    assert len(word6) == 6

def test_load_words_returns_none():
    result = load_words(letter_count=256)

    assert result is None

def test_random_word_returns_word():

    word_list = load_words()
    test_word = random_word(word_list)

    assert test_word.isalpha()
    assert len(test_word) == 5

def test_frequency_table_build():

    word_list = load_words()
    frequency_table = build_letter_frequency_table(word_list)

    assert frequency_table 
    assert len(frequency_table.keys()) == 26

    # print(frequency_table.total())

def test_fscore_returns_correct_value():
    word_list = ["AAAAA", "BBBCC"]
    frequency_table = build_letter_frequency_table(word_list)

    assert frequency_table["A"] == 5
    assert frequency_table["B"] == 3

def test_word_fscore_returns_correct_value():
    word_list = ["AAAAA", "BBBCC"]
    frequency_table = build_letter_frequency_table(word_list)

    fscore = word_fscore("AABBB", frequency_table)

    assert fscore == 19 

def test_word_uscore_returns_correct_value():

    assert word_uscore("A") == 1
    assert word_uscore("AB") == 2
    assert word_uscore("ABCDE") == 5

def test_starter_word_score_returns_correct_value():
    word_list = ["A", "AB", "ABCDE", "AAAAA"]
    frequency_table = build_letter_frequency_table(word_list)
    sorted_words = sort_by_starter_score(word_list, frequency_table)

    print(sorted_words)

    assert sorted_words == ['ABCDE', 'AB', 'AAAAA', 'A']



def test_filter_list_by_excudes():
    word_list = ["A", "AB", "ABCDE", "AAAAA"]
    exclude_set = set(["B"])
    filtered = filter_list_by_excludes(word_list, exclude_set)

    assert filtered == ["A", "AAAAA"]

def test_word_matched_mask():

    assert word_matches_mask("AAAAA", "A----")
    assert not word_matches_mask("AAAAA", "-B---")

def test_filter_by_mask():
    word_list = ["ABCDE", "BBBBB", "AAAAA"]
    mask1 = "A----"
    mask2 = "-B---"
    mask3 = "AB---"

    assert filter_for_mask(word_list, mask1) == ["ABCDE", "AAAAA"]


def test_build_mask_by_matching():
    word_list = ["ABCDE", "BBBBB", "AAAAA"]

    assert build_mask_by_matching(word_list[0], word_list[1]) == "-B---"

def test_build_mask_by_weak_match():
    result = build_mask_by_weak_match("ABCDE", "EXXXX")
    
    assert  result == "----E"

def test_filter_chain():
    wl = load_words()
    ft = build_letter_frequency_table(wl)
    sorted_words = sort_by_starter_score(wl, ft)
    #pprint(sorted_words[0:10])
    filtered = filter_for_mask(sorted_words, "A-----")
    #pprint(filtered[0:10])
    target = "PUIST"
    # print("Target: ", target)
    g, y, b = score_words_masks("RAISE", target)
    print(g, y, b)

    assert g == "--IS-"
    assert y == "-----"
    assert b == {'R', 'E', 'A'}

    list2 = filter_down(wl, g, y, b)
    #print(list2[:10])
    assert target in list2
    sorted_words = sort_by_starter_score(list2, ft)
    print(sorted_words)
    assert target in sorted_words
    g, y, b = score_words_masks("NOISY", target)
    print(g, y, b)
    list3 = filter_down(list2, g, y, b)
    print(sort_by_starter_score(list3, ft))

    g, y, b = score_words_masks("MUIST", target)
    print(g, y, b)
    list4 = filter_down(list3, g, y, b)
    print(sort_by_starter_score(list4, ft))

def test_filter_chain2():
    wl = load_words()
    ft = build_letter_frequency_table(wl)
    sorted_words = sort_by_starter_score(wl, ft)
    #pprint(sorted_words[0:10])
    target = "PUIST"
    # print("Target: ", target)
    g, y, b = score_words_masks("MOUND", target)
    assert g == "-----"
    assert y == "--U--"
    assert b == {'M', 'O', 'D', 'N'}
    print(g, y, b)
    list2 = sort_by_starter_score(filter_down(wl, g, y, b), ft)
    print(len(list2))
    print(list2[:10])
    g, y, b = score_words_masks("SERAU", target)
    print(g, y, b)
    list3 = sort_by_starter_score(filter_down(list2, g, y, b), ft)
    print(len(list3))
    print(list3[:10])

    g, y, b = score_words_masks("LITUS", target)
    print(g, y, b)
    list3 = sort_by_starter_score(filter_down(list3, g, y, b), ft)
    print(len(list3))
    print(list3[:10])

    g, y, b = score_words_masks("SUITY", target)
    print(g, y, b)
    list3 = sort_by_starter_score(filter_down(list3, g, y, b), ft)
    print(len(list3))
    print(list3[:10])







    assert True 






    

    

    assert True












    








