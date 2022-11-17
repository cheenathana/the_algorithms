from unicodedata import normalize
from collections import Counter

def is_anagram(s1, s2):
    # Creates a default dict with character and its count
    s1_dd = Counter(normalize('NFKD', s1.lower().replace(" ", "")).encode('ascii', 'ignore'))
    s2_dd = Counter(normalize('NFKD', s2.lower().replace(" ", "")).encode('ascii', 'ignore'))

    for key in s1_dd:
        if s1_dd[key] != s2_dd.get(key, 0):
            return False

    return True
        
