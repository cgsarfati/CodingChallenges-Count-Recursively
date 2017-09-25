"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

"""


def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    # BASE CASE -- if empty list
    if not lst:
        return 0

    # PROGRESSION: for each recursion, continually slice the list by removing
    # the first item until base case reached (empty list)
    # when base reached, counting occurs (1+0=1, then 1+1=2, then 1+2=3, etc)
    return 1 + count_recursively(lst[1:])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"
