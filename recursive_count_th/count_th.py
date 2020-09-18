'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    """
    Base Case
    """
    if len(word) == 0 or len(word) == 1:
        return 0
    """
    The letters T and H 
    would be the first two
    elements of a word
    """
    
    if word[0] == 't' and word[1] == 'h':
        return 1 + count_th(word[2:])
    else:
        return 0 + count_th(word[1:])