def is_palindrome_v2(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>> is_palindrome_v2('dented')
    False
    """
    return reverse(s) == s

def reverse(s):
    """ (str) -> str

    Return a reversed version of s.

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """

    rev = ''

    # For each char in s , add to the begging of rev
    for ch in s:
        rev = ch + rev

    return rev
